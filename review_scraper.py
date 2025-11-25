import os
import pickle
import time
import json
import random
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


# ============================================
# DYNAMIC UTILITIES
# ============================================
def sleep_random(a=1, b=3):
    time.sleep(random.uniform(a, b))


def find_first(driver, selectors, description="element"):
    """
    Try multiple selectors and return the first valid element.
    `selectors` can be a list of CSS or XPath expressions.
    """
    for sel in selectors:
        try:
            if sel.startswith("/") or sel.startswith("("):  # XPath
                el = driver.find_element(By.XPATH, sel)
            else:
                el = driver.find_element(By.CSS_SELECTOR, sel)

            print(f"[✓] {description} found using: {sel}")
            return el
        except:
            continue

    print(f"[✗] {description} NOT found using provided selectors")
    return None


# ============================================
# REVIEW SELECTORS — merged IDE + dynamic
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

    while True:
        sleep_random(1, 2)

        containers = driver.find_elements(By.CSS_SELECTOR, REVIEW_CONTAINER)
        print(f"[+] Found {len(containers)} reviews")

        for c in containers:
            title = find_first(c, TITLE_SELECTORS, "review title")
            rating = find_first(c, RATING_SELECTORS, "review rating")
            body = find_first(c, BODY_SELECTORS, "review text")

            reviews.append({
                "title": title.text.strip() if title else "",
                "rating": rating.text.strip() if rating else "",
                "text": body.text.strip() if body else "",
            })

        # pagination
        next_buttons = driver.find_elements(By.CSS_SELECTOR, "li.a-last a")

        if not next_buttons:
            print("[✓] Reached last page of reviews")
            break

        try:
            driver.execute_script("arguments[0].scrollIntoView();", next_buttons[0])
            sleep_random(1, 2)
            next_buttons[0].click()
            sleep_random(2, 3)
        except:
            print("[!] Could not click next page")
            break

    return reviews


# ============================================
# MAIN SCRAPER
# ============================================
def scrape_amazon():
    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 12)

    try:
        # Load homepage
        driver.get("https://www.amazon.com/")
        sleep_random()

        # Load cookies (already logged in profile)
        if os.path.exists(COOKIE_FILE):
            with open(COOKIE_FILE, "rb") as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                cookie.pop("sameSite", None)
                driver.add_cookie(cookie)
            driver.get("https://www.amazon.com/")
            sleep_random(1, 3)

        # Search Box
        search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search.clear()
        search.send_keys(SEARCH_TERM)
        sleep_random()
        search.send_keys(Keys.RETURN)

        # Wait for results
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']")))
        sleep_random(2, 4)

        # Collect product links
        product_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        product_links = []

        for card in product_cards[:MAX_PRODUCTS]:
            try:
                link_el = card.find_element(By.CSS_SELECTOR, "h2 a")
                href = link_el.get_attribute("href")
                if "/dp/" in href or "/gp/" in href:
                    product_links.append(href)
            except:
                continue

        all_reviews = []

        # Visit each product
        for link in product_links:
            print(f"[>] Opening product: {link}")

            driver.execute_script("window.open(arguments[0]);", link)
            driver.switch_to.window(driver.window_handles[-1])
            sleep_random(2, 4)

            # Reviews tab
            try:
                footer = find_first(driver,
                    [
                        "//div[@id='reviews-medley-footer']//a",
                        "#reviews-medley-footer a",
                    ],
                    "reviews link"
                )

                if not footer:
                    print("No review link found, skipping product.")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue

                review_url = footer.get_attribute("href")
                driver.get(review_url)
                sleep_random(2, 4)

                # scrape reviews
                product_reviews = scrape_reviews(driver)
                all_reviews.extend(product_reviews)

            except Exception as e:
                print(f"[!] Error scraping reviews: {e}")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep_random(1, 3)

        # Save results
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(all_reviews, f, indent=4)

        pd.DataFrame(all_reviews).to_excel(OUTPUT_EXCEL, index=False)

        print(f"[✓] Saved {len(all_reviews)} total reviews")

    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_amazon()
