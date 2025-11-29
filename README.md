# Amazon Scraper

A Python-based Amazon review scraper using Selenium and BeautifulSoup.

## Getting Started

### Clone the Repository

To pull this project to your local machine, run:

```bash
git clone https://github.com/bidemi1986/amazon-scraper.git
cd amazon-scraper
```

### Prerequisites

- Python 3.8 or higher
- Chrome browser installed

### Installation

1. **Set up a Python virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory with your Amazon credentials:

   ```env
   AMAZON_EMAIL=your_amazon_email
   AMAZON_PASSWORD=your_amazon_password
   USER=your_system_username
   ```

   > ⚠️ **Security Note**: The `.env` file contains sensitive credentials and is already included in `.gitignore` to prevent accidental commits. Never share or commit this file to version control.

### Usage

1. **Login and save cookies**:
   ```bash
   python amazon-login/login_amazon2.py
   ```

2. **Create a dummy Chrome profile** (modify the profile location for Windows or older macOS if needed):
   ```bash
   python amazon-login/create_dummy_chrome_profile.py
   ```

3. **Run the review scraper**:
   ```bash
   python review_scraper_debug.py
   ```

## Project Structure

- `app.py` - Main application entry point
- `review_scraper.py` - Core review scraping functionality
- `review_scraper_debug.py` - Debug version of the scraper
- `get_cookies.py` - Cookie management utilities
- `parse_cookies.py` - Cookie parsing utilities
- `amazon-login/` - Amazon login and Chrome profile setup
  - `login_amazon2.py` - Login script to save cookies
  - `create_dummy_chrome_profile.py` - Chrome profile setup
- `search_and_review/` - Search and review extraction functionality
  - `extract_reviews.py` - Review extraction script

## License

See [LICENSE](LICENSE) file for details.
