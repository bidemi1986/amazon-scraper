import os
import json
import shutil
from pathlib import Path

# -------------------------
# CONFIG
# -------------------------

MAC_USER = os.getenv("USER")  # macOS username
CHROME_PATH = f"/Users/{MAC_USER}/Library/Application Support/Google/Chrome"
REAL_PROFILE = os.path.join(CHROME_PATH, "Default")          # your main profile
DUMMY_PROFILE = os.path.join(CHROME_PATH, "SeleniumDummy")   # new fake profile

# Files to remove from dummy (sensitive)
SENSITIVE_FILES = [
    "Cookies",
    "History",
    "History Provider Cache",
    "Login Data",
    "Login Data For Account",
    "Web Data",
    "Top Sites",
    "Visited Links",
    "Favicons",
]

SENSITIVE_DIRS = [
    "Session Storage",
    "GPUCache",
    "Network",
    "Extension State",
    "Platform Notifications",
]

# -------------------------
# HELPER FUNCTIONS
# -------------------------

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def safe_remove(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
        except:
            pass
    elif os.path.isdir(path):
        try:
            shutil.rmtree(path)
        except:
            pass


def write_json(path, content_dict):
    with open(path, "w") as f:
        json.dump(content_dict, f, indent=2)


# -------------------------
# MAIN LOGIC
# -------------------------

def create_dummy_chrome_profile():
    print("➡️  Creating Selenium dummy Chrome profile...")

    # 1. Ensure real profile exists
    if not os.path.isdir(REAL_PROFILE):
        raise Exception(f"Chrome profile not found: {REAL_PROFILE}")

    # 2. Create destination folder
    ensure_folder(DUMMY_PROFILE)

    # 3. Copy entire profile first
    print("➡️  Copying base files from real Chrome profile...")
    shutil.copytree(REAL_PROFILE, DUMMY_PROFILE, dirs_exist_ok=True)

    # 4. Remove sensitive files
    print("➡️  Removing sensitive data...")

    for fname in SENSITIVE_FILES:
        safe_remove(os.path.join(DUMMY_PROFILE, fname))

    for dname in SENSITIVE_DIRS:
        safe_remove(os.path.join(DUMMY_PROFILE, dname))

    # 5. Modify Preferences
    print("➡️  Writing Selenium-safe Preferences...")

    pref_path = os.path.join(DUMMY_PROFILE, "Preferences")
    preferences = {}

    if os.path.exists(pref_path):
        with open(pref_path, "r") as f:
            try:
                preferences = json.load(f)
            except:
                preferences = {}

    # Inject WebAuthn + password manager disable flags
    preferences.update({
        "credentials_enable_service": False,
        "profile": {
            "password_manager_enabled": False
        },
        "webauthn": {
            "touch_to_authenticate_enabled": False
        }
    })

    write_json(pref_path, preferences)

    # 6. Modify Local State (Chrome reads fingerprint settings here)
    print("➡️  Writing Local State file...")

    local_state_path = os.path.join(CHROME_PATH, "Local State")

    local_state = {}
    if os.path.exists(local_state_path):
        with open(local_state_path, "r") as f:
            try:
                local_state = json.load(f)
            except:
                local_state = {}

    # Ensure WebAuthn and Password Manager disabled in Local State too
    local_state.update({
        "webauthn": {
            "touch_to_authenticate_enabled": False
        },
        "profile": {
            "password_manager_enabled": False
        },
        "credentials_enable_service": False,
    })

    write_json(os.path.join(DUMMY_PROFILE, "Local State"), local_state)

    print("✅ DONE!")
    print("Your dummy Selenium Chrome profile is ready at:")
    print(f"➡️  {DUMMY_PROFILE}")
    print("\nUse it in Selenium with:")
    print(
        f'chrome_options.add_argument("--user-data-dir={DUMMY_PROFILE}")'
    )


if __name__ == "__main__":
    create_dummy_chrome_profile()
