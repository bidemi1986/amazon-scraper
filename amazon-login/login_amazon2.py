from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import time
import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# ---------------------------------------
# PART 1 — Create a safe dummy Chrome profile
# ---------------------------------------

def ensure_dummy_profile(path):
    """
    Create a dummy profile directory with settings that disable passkeys & password manager.
    """

    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)

    pref_file = path / "Default" / "Preferences"
    pref_file.parent.mkdir(parents=True, exist_ok=True)

    if not pref_file.exists():
        print("Creating dummy Chrome profile with passkey-disabled preferences...")

        prefs = {
            "webauthn": {
                "enable_soft_authenticator": False
            },
            "credentials_enable_service": False,
            "profile": {"password_manager_enabled": False},
            "payment_method": {"user_data": "[]"}
        }

        pref_file.write_text(json.dumps(prefs))
    else:
        print("Dummy profile already exists →", pref_file)


# ---------------------------------------
# PART 2 — Helper Functions
# ---------------------------------------

def find_by_xpath_any(driver, xpaths, timeout=20):
    for path in xpaths:
        try:
            return WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
        except:
            pass
    raise Exception("No matching element found.")


def click_by_xpath_any(driver, xpaths, timeout=20):
    for path in xpaths:
        try:
            el = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, path))
            )
            el.click()
            return
        except:
            pass
    raise Exception("No clickable element found.")



# ---------------------------------------
# PART 3 — Amazon Login With Forced Passkey Popup Blocked
# ---------------------------------------

def login_and_save_cookies(email, password, cookies_file="amazon_cookies.pkl"):

    dummy_profile_path = "/Users/biddyvadr/Library/Application Support/Google/Chrome/SeleniumDummy"

    ensure_dummy_profile(dummy_profile_path)

    chrome_options = Options()

    chrome_options.add_argument(f"--user-data-dir={dummy_profile_path}")

    # Critical passkey popup blockers:
    chrome_options.add_argument("--disable-webauthn")
    chrome_options.add_argument("--disable-features=WebAuthentication,WebAuthnUI,WebAuthnConditionalUI")
    chrome_options.add_experimental_option("prefs", {
        "webauthn.enable_soft_authenticator": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })

    # Stability settings
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        # Inject JS early to override navigator.credentials.get() which triggers passkeys
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                    navigator.credentials.get = () => {
                        console.warn("Passkey prompt blocked by automation script.");
                        return new Promise(() => {}); // Hang forever so no popup
                    };
                """
            }
        )

        # --- Open Amazon ---
        driver.get("https://www.amazon.com/")
        print("Opened Amazon homepage")
        time.sleep(2)

        account_menu = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "nav-link-accountList"))
        )
        ActionChains(driver).move_to_element(account_menu).perform()
        time.sleep(1)

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "nav-flyout-accountList"))
        )

        click_by_xpath_any(driver, [
            "//a[@data-nav-role='signin']",
            "//a[contains(@class,'nav-action-signin-button')]",
            "//span[text()='Sign in']/ancestor::a",
        ])
        print("Clicked Sign-in")

        email_input = find_by_xpath_any(driver, [
            "//input[@type='email']",
            "//input[contains(@id,'email')]",
            "//input[@name='email']"
        ])
        email_input.send_keys(email)
        print("Entered Email")

        click_by_xpath_any(driver, [
            "//input[@type='submit']",
        ])
        print("Clicked Continue")
        time.sleep(2)

        # --- Password ---
        password_input = find_by_xpath_any(driver, [
            "//input[@type='password']",
            "//input[contains(@id,'password')]",
        ])
        password_input.send_keys(password)
        print("Entered Password")

        click_by_xpath_any(driver, [
            "//input[@id='signInSubmit']",
            "//input[@value='Sign in']"
        ])
        print("Clicked Sign In")

        # Verify login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        print("Login successful")

        # Save cookies
        cookies = driver.get_cookies()
        pickle.dump(cookies, open(cookies_file, "wb"))
        print(f"Cookies saved → {cookies_file}")

    except Exception as error:
        print("\n❌ LOGIN FAILED:", error)
        driver.save_screenshot("login_error.png")
        print("Saved screenshot → login_error.png")

    finally:
        driver.quit()



# ---------------------------------------
# MAIN
# ---------------------------------------

if __name__ == "__main__":
    email = os.getenv("AMAZON_EMAIL")
    password = os.getenv("AMAZON_PASSWORD")

    if not email or not password:
        raise ValueError("Set AMAZON_EMAIL and AMAZON_PASSWORD in .env")

    login_and_save_cookies(email, password)
