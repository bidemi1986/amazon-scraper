# Apple App Store Review Scraper

A comprehensive Python scraper for collecting Apple App Store reviews from multiple countries. Perfect for sentiment analysis and customer feedback analysis.

## Features

✅ **Multi-Country Support**: Fetch reviews from multiple countries simultaneously

- US, UK, Canada, Australia, Germany, France, Japan, and more

✅ **Dual Output Formats**: Saves data in both JSON and CSV formats

✅ **Automatic Deduplication**: Removes duplicate reviews across countries

✅ **Rich Metadata**: Includes:

- User ratings and review text
- Review titles and dates
- Developer responses
- Country of origin
- Edit status

✅ **Detailed Logging**: Real-time progress updates and statistics

✅ **Review Statistics**: Automatic generation of analytics including:

- Total review count
- Average rating
- Rating distribution
- Reviews with developer responses
- Reviews by country
- Edited reviews count

## Installation

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure App Details

Create a `.env` file in the `apple-app-store` directory:

```bash
cp .env.example .env
```

Then edit `.env` and set your app details:

```env
APP_NAME=whatsapp-messenger
APP_ID=310633997
COUNTRIES=us,gb,ca
```

## Usage

The scraper supports **three ways** to specify the app (in priority order):

### Method 1: Command Line Arguments (Highest Priority)

```bash
python scrape-reviews.py <APP_NAME> <APP_ID> [COUNTRIES]
```

**Example:**

```bash
python scrape-reviews.py whatsapp-messenger 310633997 us,gb,ca
```

### Method 2: Environment Variable (.env file)

Create a `.env` file with:

```env
APP_NAME=whatsapp-messenger
APP_ID=310633997
COUNTRIES=us,gb,ca
```

Then run:

```bash
python scrape-reviews.py
```

### Method 3: Error if Neither Provided

If you don't provide app details via command line or `.env` file, you'll get a helpful error message.

## Finding App Name and App ID

The App Name and App ID are found in the App Store URL:

```
https://apps.apple.com/us/app/whatsapp-messenger/id310633997
                                  ^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^
                                  This is APP_NAME     This is APP_ID
```

**Popular App Examples:**

| App       | APP_NAME           | APP_ID    |
| --------- | ------------------ | --------- |
| WhatsApp  | whatsapp-messenger | 310633997 |
| Instagram | instagram          | 389801252 |
| TikTok    | tiktok             | 835599320 |
| Spotify   | spotify-music      | 324684580 |
| Netflix   | netflix            | 363590051 |
| YouTube   | youtube            | 544007664 |
| Facebook  | facebook           | 284882215 |

## Country Codes

Common country codes for the `COUNTRIES` parameter:

| Country       | Code | Country        | Code |
| ------------- | ---- | -------------- | ---- |
| United States | us   | United Kingdom | gb   |
| Canada        | ca   | Australia      | au   |
| Germany       | de   | France         | fr   |
| Japan         | jp   | China          | cn   |
| India         | in   | Brazil         | br   |
| Mexico        | mx   | Spain          | es   |
| Italy         | it   | Netherlands    | nl   |

## Output Files

The scraper generates two files with timestamps:

### 1. JSON File

**Format**: `app_store_reviews_{APP_ID}_{TIMESTAMP}.json`

Contains complete review data with all metadata:

```json
[
  {
    "userName": "John Doe",
    "rating": 5,
    "title": "Great app!",
    "review": "This app is amazing and works perfectly.",
    "date": "2024-12-04",
    "isEdited": false,
    "developerResponse": {
      "body": "Thank you for your feedback!",
      "modified": "2024-12-05"
    },
    "country": "us",
    "fetched_at": "2025-12-05T03:37:00.000000"
  }
]
```

### 2. CSV File

**Format**: `app_store_reviews_{APP_ID}_{TIMESTAMP}.csv`

Structured data perfect for analysis with columns:

- `user_name`
- `rating`
- `title`
- `review_text`
- `date`
- `is_edited`
- `developer_response`
- `developer_response_date`
- `country`
- `fetched_at`

## Configuration

You can customize the scraper by modifying the initialization:

```python
scraper = AppleAppStoreReviewScraper(
    app_name="whatsapp-messenger",
    app_id="310633997",
    countries=['us', 'gb', 'ca'],  # List of country codes
    reviews_count=200  # Reviews per country
)
```

### Parameters

- **`app_name`** (str): App name slug from App Store URL
- **`app_id`** (str): Numeric App Store ID
- **`countries`** (list): List of country codes (default: ['us'])
- **`reviews_count`** (int): Number of reviews per country (default: 200)

## Example Output

```
============================================================
APPLE APP STORE REVIEW SCRAPER
============================================================
App Name: whatsapp-messenger
App ID: 310633997
Countries: US, GB, CA
============================================================

[2025-12-05 03:37:00] [INFO] Starting review scraping for app: whatsapp-messenger
[2025-12-05 03:37:00] [INFO] Fetching reviews from US...
[2025-12-05 03:37:05] [INFO] ✓ Successfully fetched 200 reviews from US
[2025-12-05 03:37:05] [INFO] Fetching reviews from GB...
[2025-12-05 03:37:10] [INFO] ✓ Successfully fetched 200 reviews from GB
[2025-12-05 03:37:10] [INFO] Fetching reviews from CA...
[2025-12-05 03:37:15] [INFO] ✓ Successfully fetched 200 reviews from CA
[2025-12-05 03:37:15] [INFO] Total unique reviews collected: 585

============================================================
REVIEW STATISTICS
============================================================
Total Reviews: 585
Average Rating: 4.2/5.0
Rating Distribution: {5: 350, 4: 120, 3: 65, 2: 30, 1: 20}
Reviews with Developer Response: 45
Reviews by Country: {'us': 195, 'gb': 198, 'ca': 192}
Edited Reviews: 12
============================================================

============================================================
SCRAPING COMPLETED SUCCESSFULLY!
============================================================
JSON file: app_store_reviews_310633997_20251205_033715.json
CSV file: app_store_reviews_310633997_20251205_033715.csv
============================================================
```

## Use Cases

### 1. Sentiment Analysis

- Rating distribution shows overall sentiment
- Review text can be analyzed with NLP tools
- Developer responses indicate engagement

### 2. International Feedback

- Compare sentiment across different countries
- Identify region-specific issues
- Track global vs local trends

### 3. Competitive Analysis

- Compare your app reviews with competitors
- Benchmark ratings and response rates
- Identify differentiating features

### 4. Product Feedback

- Identify common issues from low-rated reviews
- Find feature requests from user feedback
- Track sentiment changes over time

## Tips for Better Results

1. **Multiple Countries**: Fetch from 3-5 countries for diverse feedback
2. **Regular Scraping**: Schedule periodic scraping to track trends
3. **Combine with Analysis**: Use pandas, matplotlib, or sentiment analysis libraries
4. **Developer Responses**: Track response rate to gauge customer engagement
5. **Compare Platforms**: Use alongside Google Play scraper for complete picture

## Troubleshooting

### No reviews fetched

- Verify the APP_NAME and APP_ID are correct
- Check the app exists in the specified countries
- Try with a popular app first (e.g., WhatsApp)

### Slow Performance

- Reduce the number of countries
- Decrease `reviews_count` per country
- The API has natural rate limits

### Dependency Conflicts

- The scraper uses older versions of requests/urllib3
- This is required by the app-store-scraper library
- Use a virtual environment to isolate dependencies

## Dependencies

- `app-store-scraper` (v0.3.5+): For fetching reviews from Apple App Store
- `pandas` (v2.0+): For data manipulation and CSV export
- `python-dotenv` (v1.0+): For loading environment variables from .env file

## Differences from Google Play Scraper

| Feature            | Apple App Store   | Google Play Store                    |
| ------------------ | ----------------- | ------------------------------------ |
| Identifier         | APP_NAME + APP_ID | APP_ID (package name)                |
| Sorting            | By country        | By method (newest, relevant, rating) |
| Developer Response | Included          | Included                             |
| Max Reviews        | ~200 per country  | ~200 per sort method                 |

## License

This scraper is for educational and research purposes. Please respect Apple's terms of service and rate limits.

## Author

Created for sentiment analysis and customer feedback research.

---

**Happy Scraping! 🍎**
