from pythonjsonlogger import jsonlogger
from aiolimiter import AsyncLimiter
from urllib.parse import urlparse
import asyncio
import aiohttp
import logging
import time
from pprint import pprint as pp
import random
import aiofiles
import typer
from typing_extensions import Annotated
from pathlib import Path
import os
from bs4 import BeautifulSoup
from swiftshadow import QuickProxy
import pickle
import json
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytesseract
from PIL import Image
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
# Configures a json style logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

print(f"QuickProxy proxy",QuickProxy())
newproxy = QuickProxy()
valid_proxy = f"{newproxy.protocol}://{newproxy.ip}:{newproxy.port}"
print(f"valid_proxy...",valid_proxy)

async def HTTPClientDownloader(url, settings, cookies=None):
    max_tcp_connections = settings['max_tcp_connections']

    # uses the rate limiter
    async with settings["rate"]:

        # open a session to make the requests
        jar = aiohttp.CookieJar()
        if cookies:
            # Parse the URL to use as base for cookies
            from yarl import URL
            parsed_url = URL(url)
            
            for cookie in cookies:
                # Create a proper URL from the cookie domain
                cookie_domain = cookie['domain'].lstrip('.')  # Remove leading dot
                cookie_url = URL.build(scheme=parsed_url.scheme, host=cookie_domain)
                jar.update_cookies({cookie['name']: cookie['value']}, response_url=cookie_url)
        
        connector = aiohttp.TCPConnector(limit=max_tcp_connections)
        async with aiohttp.ClientSession(cookie_jar=jar, connector=connector) as session:
            start_time = time.perf_counter()  # Start timer

            proxy = settings.get('proxy')
            html = None

            # makes a GET request to the target website
            async with session.get(url, proxy=proxy, headers=settings['headers']) as response:
                html = await response.text()
                end_time = time.perf_counter()  # Stop timer
                elapsed_time = end_time - start_time  # Calculate time taken to get response
                status = response.status

                logger.info(
                    msg="Request complete.",
                    extra={
                        "status": status,
                        "url": url,
                        "elapsed_time": f"{elapsed_time:4f}",
                    }
                )

                # save the html in a cache folder if output_path is set
                if 'output_path' in settings:
                    loc = os.path.join(settings['cache_dir'], settings["output_path"])
                    async with aiofiles.open(loc, mode="w") as fd:
                        await fd.write(html)

            return html
        
async def dispatch(url, settings):
    await HTTPClientDownloader(url, settings)

# the location of where our async tasks are created and invoked
async def main(start_urls, settings):
    tasks = []
    for url in start_urls:
        task = asyncio.create_task(dispatch(url, settings))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    print(f"total requests", len(results))


def fetch_reviews(product_url, settings, cookies, pages=1):
    # Extract ASIN from product URL
    parsed = urlparse(product_url)
    path_parts = parsed.path.split('/')
    asin = None
    for i, part in enumerate(path_parts):
        if part == 'dp' and i + 1 < len(path_parts):
            asin = path_parts[i + 1]
            break
    if not asin:
        raise ValueError("Could not extract ASIN from URL")
    print(f"Extracted ASIN: {asin}")

    review_urls = []
    for page in range(1, pages + 1):
        review_url = f"https://www.amazon.com/product-reviews/{asin}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber={page}"
        review_urls.append(review_url)

    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"--user-agent={settings['headers']['user-agent']}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Add cookies
    driver.get("https://www.amazon.com")  # Navigate to domain first
    for cookie in cookies:
        try:
            driver.add_cookie({
                'name': cookie['name'],
                'value': cookie['value'],
                'domain': cookie['domain'],
                'path': cookie.get('path', '/'),
                'secure': cookie.get('secure', False),
                'httpOnly': cookie.get('httpOnly', False)
            })
        except Exception as e:
            print(f"Error adding cookie {cookie['name']}: {e}")

    all_reviews = []
    for i, url in enumerate(review_urls, 1):
        driver.get(url)
        time.sleep(5)  # Wait for JS to load
        screenshot_path = f'screenshot_page_{i}.png'
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
        # OCR text extraction
        try:
            img = Image.open(screenshot_path)
            ocr_text = pytesseract.image_to_string(img)
            print(f"OCR text preview: {ocr_text[:1000]}")
        except Exception as e:
            print(f"OCR failed: {e}")
        html = driver.page_source
        print(f"Fetched page {url}, HTML length: {len(html)}")
        print(f"HTML preview: {html[:2000]}")
        soup = BeautifulSoup(html, 'html.parser')
        reviews = soup.find_all("div", {"data-hook": "review"})
        print(f"Found {len(reviews)} review elements on page")
        if len(reviews) == 0:
            # Try alternative selectors
            reviews = soup.find_all("div", class_="a-section review")
            print(f"Alternative selector found {len(reviews)} review elements")
        for review in reviews:
            try:
                title_elem = review.find("a", {"data-hook": "review-title"})
                title = title_elem.text.strip() if title_elem else "No title"
                rating_elem = review.find("i", {"data-hook": "review-star-rating"})
                rating = rating_elem.text.strip().split()[0] if rating_elem else "No rating"
                text_elem = review.find("span", {"data-hook": "review-body"})
                text = text_elem.text.strip() if text_elem else "No text"
                all_reviews.append({
                    "title": title,
                    "rating": rating,
                    "text": text
                })
            except Exception as e:
                print(f"Error parsing review: {e}")
                continue
        time.sleep(1)  # Rate limit

    driver.quit()
    print(f"Total reviews extracted: {len(all_reviews)}")
    return all_reviews


# a cli interface to make the program user friendly
cli_app = typer.Typer()
@cli_app.command("amazon")
def amazon(
    url: Annotated[str, typer.Option("--url", "-u", help="url")],
    out: Annotated[str, typer.Option("--out", "-o", help="output path and file name")],
    use_cache: Annotated[bool, typer.Option(help="Read from the cached version of the page")] = False,
    max_tcp_connections: Annotated[int, typer.Option("--max-tcp-conn", help="max tcp connections")] = 1,
    rate: Annotated[int, typer.Option(help="num of requests per min")] = 1,
):
    def read_from_cache(file_path):
        html_content = None
        with open(file_path, "r") as file:
            html_content = file.read()
            # print(html_content)
            print("Fetching from cache")
        return html_content    


    # cache procedures
    host = urlparse(url).hostname
    directory = "cache"
    current_directory = Path.cwd()
    cache_dir = current_directory / directory / host
    cached_file = Path(cache_dir / out)


    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' # works!
    ]
    user_agent = random.choice(user_agents)
    settings = {
        "max_tcp_connections": max_tcp_connections,
        "proxies": [
           valid_proxy # "http://localhost:8765",
        ],

        "headers": {
            'user-agent': user_agent,
            'accept-language': 'en',
            'accept-encoding': 'gzip, deflate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        },
        "cache_dir": cache_dir,
        "output_path": out,
        "rate": AsyncLimiter(rate, 60), # 10 reqs/min
    }

    # make sure the cache directory exists
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True)

    # get the resulting HTML from the cache or make a GET request
    html = None
    if use_cache:
        html = read_from_cache(cached_file)
    else:
        # use the asyncio runtime to make a request
        asyncio.run(main([url], settings))
        # read the results from the cache folder
        html = read_from_cache(cached_file)

    # once you have the HTML you can parse the document to your liking
    # from here you can parse for the data you want
    soup = BeautifulSoup(html, 'html.parser')
    # the best seller items are fixed with this ID however it could change in the future
    items = soup.find_all("div", attrs={"id":'gridItemRoot'})
    print(items)



@cli_app.command("reviews")
def reviews(
    url: Annotated[str, typer.Option("--url", "-u", help="Product URL")],
    out: Annotated[str, typer.Option("--out", "-o", help="Output file base name")] = "reviews",
    pages: Annotated[int, typer.Option("--pages", help="Number of review pages to fetch")] = 1,
    max_tcp_connections: Annotated[int, typer.Option("--max-tcp-conn", help="max tcp connections")] = 1,
    rate: Annotated[int, typer.Option(help="num of requests per min")] = 1,
):
    # Load cookies, run login if needed
    try:
        with open("amazon_cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
        print(f"Loaded {len(cookies)} cookies")
    except FileNotFoundError:
        print("Cookies file not found. Running login script...")
        result = subprocess.run(["python", "login_amazon.py"], capture_output=True, text=True)
        print("Login script output:", result.stdout)
        if result.stderr:
            print("Login script errors:", result.stderr)
        try:
            with open("amazon_cookies.pkl", "rb") as f:
                cookies = pickle.load(f)
            print(f"Loaded {len(cookies)} cookies after login")
        except:
            print("Failed to load cookies after login.")
            return

    # Settings
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    ]
    user_agent = random.choice(user_agents)
    settings = {
        "max_tcp_connections": max_tcp_connections,
        "proxy": None,  # Disable proxy for reviews to avoid blocking
        "headers": {
            'user-agent': user_agent,
            'accept-language': 'en',
            'accept-encoding': 'gzip, deflate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        },
        "rate": AsyncLimiter(rate, 60),
    }

    # Fetch reviews
    all_reviews = fetch_reviews(url, settings, cookies, pages)

    # Save to JSON
    with open(f"{out}.json", "w", encoding="utf-8") as f:
        json.dump(all_reviews, f, ensure_ascii=False, indent=4)

    # Save to Excel
    df = pd.DataFrame(all_reviews)
    df.to_excel(f"{out}.xlsx", index=False)

    print(f"Saved {len(all_reviews)} reviews to {out}.json and {out}.xlsx")



if __name__ == '__main__':
    cli_app()
