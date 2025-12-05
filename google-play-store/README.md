# Google Play Store Review Scraper

A comprehensive Python scraper for collecting Google Play Store reviews using multiple sorting methods. Perfect for sentiment analysis and customer feedback analysis.

## Features

✅ **Multiple Sorting Methods**: Fetches reviews using three different sorting strategies:

- **NEWEST**: Most recent reviews
- **MOST_RELEVANT**: Most helpful/relevant reviews
- **RATING**: Reviews sorted by rating

✅ **Dual Output Formats**: Saves data in both JSON and CSV formats

✅ **Automatic Deduplication**: Removes duplicate reviews based on review ID

✅ **Rich Metadata**: Includes timestamps, sort method, ratings, thumbs up counts, and more

✅ **Detailed Logging**: Real-time progress updates and statistics

✅ **Review Statistics**: Automatic generation of review analytics including:

- Total review count
- Average rating
- Rating distribution
- Reviews with developer replies
- Total engagement (thumbs up)

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

### 3. Configure App ID

Create a `.env` file in the `google-play-store` directory:

```bash
cp .env.example .env
```

Then edit `.env` and set your app ID:

```env
APP_ID=com.your.app.id
```

## Usage

The scraper supports **three ways** to specify the App ID (in priority order):

### Method 1: Command Line Argument (Highest Priority)

```bash
python scrape-reviews.py <APP_ID>
```

**Example:**

```bash
python scrape-reviews.py com.whatsapp
```

### Method 2: Environment Variable (.env file)

Create a `.env` file with:

```env
APP_ID=com.whatsapp
```

Then run:

```bash
python scrape-reviews.py
```

### Method 3: Error if Neither Provided

If you don't provide an APP_ID via command line or `.env` file, you'll get a helpful error message.

### Finding App IDs

The App ID is the package name found in the Google Play Store URL:

```
https://play.google.com/store/apps/details?id=com.whatsapp
                                              ^^^^^^^^^^^^
                                              This is the App ID
```

**Popular App ID Examples:**

- WhatsApp: `com.whatsapp`
- Instagram: `com.instagram.android`
- Spotify: `com.spotify.music`
- TikTok: `com.zhiliaoapp.musically`
- Netflix: `com.netflix.mediaclient`

## Output Files

The scraper generates two files with timestamps:

### 1. JSON File

**Format**: `google_play_reviews_{APP_ID}_{TIMESTAMP}.json`

Contains complete review data with all metadata:

```json
[
  {
    "reviewId": "...",
    "userName": "John Doe",
    "score": 5,
    "content": "Great app!",
    "thumbsUpCount": 42,
    "reviewCreatedVersion": "2.24.23.78",
    "at": "2024-12-02 17:58:36",
    "replyContent": null,
    "repliedAt": null,
    "sort_method": "NEWEST",
    "fetched_at": "2025-12-04T09:25:18.043250"
  }
]
```

### 2. CSV File

**Format**: `google_play_reviews_{APP_ID}_{TIMESTAMP}.csv`

Structured data perfect for analysis with columns:

- `review_id`
- `user_name`
- `rating`
- `review_text`
- `thumbs_up_count`
- `review_created_version`
- `at` (review date)
- `reply_content`
- `replied_at`
- `sort_method`
- `fetched_at`

## Configuration

You can customize the scraper by modifying the `GooglePlayReviewScraper` initialization:

```python
scraper = GooglePlayReviewScraper(
    app_id="com.example.app",
    reviews_per_sort=200,  # Number of reviews per sorting method
    lang='en',             # Language code
    country='us'           # Country code
)
```

### Parameters

- **`app_id`** (str): Google Play Store app package ID
- **`reviews_per_sort`** (int): Number of reviews to fetch per sorting method (default: 200)
- **`lang`** (str): Language code for reviews (default: 'en')
- **`country`** (str): Country code for reviews (default: 'us')

## Example Output

```
============================================================
GOOGLE PLAY STORE REVIEW SCRAPER
============================================================
App ID: com.whatsapp
============================================================

[2025-12-04 09:25:14] [INFO] Starting review scraping for app: com.whatsapp
[2025-12-04 09:25:14] [INFO] Fetching 200 reviews sorted by NEWEST...
[2025-12-04 09:25:16] [INFO] ✓ Successfully fetched 200 reviews (NEWEST)
[2025-12-04 09:25:16] [INFO] Fetching 200 reviews sorted by MOST_RELEVANT...
[2025-12-04 09:25:18] [INFO] ✓ Successfully fetched 200 reviews (MOST_RELEVANT)
[2025-12-04 09:25:18] [INFO] Fetching 200 reviews sorted by RATING...
[2025-12-04 09:25:20] [INFO] ✓ Successfully fetched 200 reviews (RATING)
[2025-12-04 09:25:20] [INFO] Total unique reviews collected: 569

============================================================
REVIEW STATISTICS
============================================================
Total Reviews: 569
Average Rating: 3.72/5.0
Rating Distribution: {5: 325, 1: 126, 4: 45, 3: 37, 2: 36}
Reviews with Developer Replies: 0
Total Thumbs Up: 3897652
============================================================

============================================================
SCRAPING COMPLETED SUCCESSFULLY!
============================================================
JSON file: google_play_reviews_com.whatsapp_20251204_092520.json
CSV file: google_play_reviews_com.whatsapp_20251204_092520.csv
============================================================
```

## Use Cases

### 1. Sentiment Analysis

The collected reviews are perfect for sentiment analysis:

- Rating distribution shows overall sentiment
- Review text can be analyzed with NLP tools
- Thumbs up counts indicate review helpfulness

### 2. Product Feedback

- Identify common issues from low-rated reviews
- Find feature requests from user feedback
- Track sentiment changes over time

### 3. Competitive Analysis

- Compare your app reviews with competitors
- Benchmark ratings and engagement
- Identify differentiating features

## Tips for Better Results

1. **Adjust `reviews_per_sort`**: Increase for more comprehensive data (max ~200 per request)
2. **Multiple Languages**: Run the scraper with different `lang` codes to get international feedback
3. **Regular Scraping**: Schedule periodic scraping to track sentiment trends over time
4. **Combine with Analysis**: Use pandas, matplotlib, or sentiment analysis libraries to visualize the data

## Troubleshooting

### No reviews fetched

- Verify the App ID is correct
- Check if the app has reviews in the specified language/country
- Try with a popular app first (e.g., `com.whatsapp`)

### Rate Limiting

- The scraper includes natural delays between requests
- If you encounter issues, reduce `reviews_per_sort`

## Dependencies

- `google-play-scraper` (v1.2.7+): For fetching reviews from Google Play Store
- `pandas` (v2.0+): For data manipulation and CSV export
- `python-dotenv` (v1.0+): For loading environment variables from .env file

## License

This scraper is for educational and research purposes. Please respect Google Play Store's terms of service and rate limits.

## Author

Created for sentiment analysis and customer feedback research.

---

**Happy Scraping! 🚀**
