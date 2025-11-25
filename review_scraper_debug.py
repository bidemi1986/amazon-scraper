import os
import pickle
import time
import json
import random
import traceback
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================
# CONFIG
# ============================================
SEARCH_TERM = "playstation 5"
MAX_PRODUCTS = 5
OUTPUT_JSON = "reviews.json"
OUTPUT_EXCEL = "reviews.xlsx"
COOKIE_FILE = "amazon_cookies.pkl"
PROFILE_PATH = "/Users/biddyvadr/Library/Application Support/Google/Chrome/SeleniumDummy"


def log(msg):
    print(f"[LOG] {msg}")


# ============================================
# UTILITIES
# ============================================
def sleep_random(a=1, b=3):
    t = random.uniform(a, b)
    log(f"Sleeping {t:.2f} sec")
    time.sleep(t)


def find_first(driver, selectors, description="element"):
    """
    Try multiple selectors and return the first valid element.
    Log every attempt.
    """
    log(f"Finding {description}... trying selectors:")
    for sel in selectors:
        log(f" └── trying: {sel}")
        try:
            if sel.startswith("/") or sel.startswith("("):
                el = driver.find_element(By.XPATH, sel)
            else:
                el = driver.find_element(By.CSS_SELECTOR, sel)
            log(f"[✓] {description} found using: {sel}")
            return el
        except Exception as e:
            log(f"[x] Selector failed: {sel} → {e}")
            continue

    log(f"[✗] FAILED to find {description}")
    return None


# ============================================
# REVIEW SELECTORS
# ============================================
REVIEW_CONTAINER = "div[data-hook='review']"
TITLE_SELECTORS = [
    "a[data-hook='review-title']",
    "span[data-hook='review-title']",
    "//a[@data-hook='review-title']",
    "//span[@data-hook='review-title']",
]
RATING_SELECTORS = [
    "i[data-hook='review-star-rating'] span",
    "//i[@data-hook='review-star-rating']//span",
]
BODY_SELECTORS = [
    "span[data-hook='review-body']",
    "//span[@data-hook='review-body']",
]


# ============================================
# SCRAPE ALL REVIEWS FOR A PRODUCT
# ============================================
def scrape_reviews(driver):
    reviews = []
    page_num = 1

    while True:
        log(f"--- Scraping Review Page {page_num} ---")
        log(f"URL: {driver.current_url}")

        sleep_random(1, 2)

        containers = driver.find_elements(By.CSS_SELECTOR, REVIEW_CONTAINER)
        log(f"[+] Found {len(containers)} review containers")

        for c in containers:
            log("Extracting one review...")

            title = find_first(c, TITLE_SELECTORS, "review title")
            rating = find_first(c, RATING_SELECTORS, "review rating")
            body = find_first(c, BODY_SELECTORS, "review text")

            reviews.append({
                "title": title.text.strip() if title else "",
                "rating": rating.text.strip() if rating else "",
                "text": body.text.strip() if body else "",
            })

        # pagination
        log("Looking for NEXT button...")
        next_buttons = driver.find_elements(By.CSS_SELECTOR, "li.a-last a")
        log(f"Next buttons found: {len(next_buttons)}")

        if not next_buttons:
            log("[✓] LAST PAGE reached.")
            break

        try:
            log("Scrolling into next button...")
            driver.execute_script("arguments[0].scrollIntoView();", next_buttons[0])
            sleep_random(1, 2)
            log("Clicking next page...")
            next_buttons[0].click()
            sleep_random(2, 3)
            page_num += 1
        except Exception as e:
            log(f"[!] Could NOT click next page → {e}")
            log(traceback.format_exc())
            break

    log(f"[✓] TOTAL REVIEWS SCRAPED: {len(reviews)}")
    return reviews



PRODUCT_LINK_SELECTORS = [
    "h2 a",
    "a.a-link-normal.s-no-outline",
    "a.a-link-normal",
    "a.s-link-style",
    "a.a-text-normal",
    "div.a-section a",
    "a[href*='/dp/']",
    "a[href*='/gp/']",
]

def find_product_link(card):
    for sel in PRODUCT_LINK_SELECTORS:
        try:
            el = card.find_element(By.CSS_SELECTOR, sel)
            href = el.get_attribute("href")
            if href and ("/dp/" in href or "/gp/" in href):
                log(f"[✓] Found product link using: {sel}")
                return href
        except:
            continue

    log("[x] Failed to extract product link for this card.")
    return None

# ============================================
# MAIN SCRAPER
# ============================================
def scrape_amazon():
    log("Launching Chrome with profile...")

    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 12)

    try:
        log("Opening Amazon homepage...")
        driver.get("https://www.amazon.com/")
        log(f"Page loaded, URL: {driver.current_url}")
        sleep_random()

        # Load cookies if present
        if os.path.exists(COOKIE_FILE):
            log("Loading cookies...")
            with open(COOKIE_FILE, "rb") as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                cookie.pop("sameSite", None)
                driver.add_cookie(cookie)
            log("Reloading page with cookies...")
            driver.get("https://www.amazon.com/")
            sleep_random(1, 3)

        # Search
        log("Locating search box...")
        search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search.clear()
        search.send_keys(SEARCH_TERM)
        sleep_random()
        search.send_keys(Keys.RETURN)
        log("Search submitted")

        # Wait for results
        log("Waiting for results...")
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
        ))
        sleep_random(2, 4)
        log("Search results loaded")

        # Collect product links
        log("Finding product cards...")
        product_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        log(f"Found product cards: {len(product_cards)}")

        product_links = []
        for idx, card in enumerate(product_cards[:MAX_PRODUCTS]):
            log(f"Extracting link for product #{idx + 1}...")
            try:
                href = find_product_link(card)
                if href:
                    product_links.append(href)
                    log(f" [✓] Valid product link collected: {href}")
                else:
                    log(" [x] Skipped product — no valid link found")
            except Exception as e:
                log(f"[!] Error extracting link: {e}")
                log(traceback.format_exc())
                continue

        log(f"TOTAL VALID PRODUCT LINKS: {len(product_links)}")

        all_reviews = []

        # Visit each product
        for link in product_links:
            log("----------------------------------------")
            log(f"[>] Opening product: {link}")
            log("----------------------------------------")

            driver.execute_script("window.open(arguments[0]);", link)
            driver.switch_to.window(driver.window_handles[-1])
            log(f"New tab opened, URL: {driver.current_url}")
            sleep_random(2, 4)

            # Reviews tab
            try:
                log("Finding reviews link...")
                footer = find_first(driver,
                                    [
                                        "//div[@id='reviews-medley-footer']//a",
                                        "#reviews-medley-footer a",
                                    ],
                                    "reviews link"
                                    )

                if not footer:
                    log("[x] NO REVIEW LINK FOUND → Skipping product")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue

                review_url = footer.get_attribute("href")
                log(f"Review page URL: {review_url}")

                driver.get(review_url)
                log(f"Loaded review page: {driver.current_url}")
                sleep_random(2, 4)

                product_reviews = scrape_reviews(driver)
                all_reviews.extend(product_reviews)

            except Exception as e:
                log(f"[!] Error scraping reviews: {e}")
                log(traceback.format_exc())

            log("Closing product tab...")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep_random(1, 3)

        # Save output
        log("Saving JSON + Excel...")
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(all_reviews, f, indent=4)

        pd.DataFrame(all_reviews).to_excel(OUTPUT_EXCEL, index=False)

        log(f"[✓] Saved {len(all_reviews)} reviews TOTAL")

    finally:
        driver.quit()
        log("Driver closed")


if __name__ == "__main__":
    scrape_amazon()
