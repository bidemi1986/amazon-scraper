import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from swiftshadow import QuickProxy

# Proxy setup
newproxy = QuickProxy()
valid_proxy = f"{newproxy.protocol}://{newproxy.ip}:{newproxy.port}"
print(f"Using proxy: {valid_proxy}")

# Chrome options
options = Options()
# options.add_argument("--headless")  # Disable headless to see the browser
options.add_argument(f'--proxy-server={valid_proxy}')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# Disable proxy for webdriver manager
import os
os.environ['WDM_HTTP_PROXY'] = ''
os.environ['WDM_HTTPS_PROXY'] = ''

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Load Amazon
    driver.get("https://www.amazon.com/")
    print("Loaded Amazon homepage")

    # Click Sign in
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))).click()
    print("Clicked Sign in")

    # Enter email
    email = os.environ.get("AMAZON_EMAIL")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ap_email_login"))).send_keys(email)
    driver.find_element(By.CLASS_NAME, "a-button-input").click()
    print("Entered email")

    # Enter password
    password = os.environ.get("AMAZON_PASSWORD")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ap_password"))).send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()
    print("Entered password")

    # Wait for login
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
    print("Login successful")

    # Save cookies
    cookies = driver.get_cookies()
    with open("amazon_cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)
    print(f"Saved {len(cookies)} cookies to amazon_cookies.pkl")

finally:
    driver.quit()
    print("Driver closed")