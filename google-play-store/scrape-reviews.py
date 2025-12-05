#!/usr/bin/env python3
"""
Google Play Store Review Scraper
Fetches reviews using multiple sorting methods and saves to JSON and CSV formats
"""

import json
import pandas as pd
from google_play_scraper import Sort, reviews
from datetime import datetime
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class GooglePlayReviewScraper:
    """Scraper for Google Play Store reviews with multiple sorting options"""
    
    def __init__(self, app_id, reviews_per_sort=200, lang='en', country='us'):
        """
        Initialize the scraper
        
        Args:
            app_id (str): Google Play Store app ID (e.g., 'com.example.app')
            reviews_per_sort (int): Number of reviews to fetch per sorting method
            lang (str): Language code for reviews
            country (str): Country code for reviews
        """
        self.app_id = app_id
        self.reviews_per_sort = reviews_per_sort
        self.lang = lang
        self.country = country
        self.all_reviews = []
        
    def log(self, message, level="INFO"):
        """Print formatted log messages"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
        
    def fetch_reviews_by_sort(self, sort_type, sort_name):
        """
        Fetch reviews with a specific sorting method
        
        Args:
            sort_type: Sort enum value (Sort.NEWEST, Sort.MOST_RELEVANT, Sort.RATING)
            sort_name (str): Human-readable name for logging
            
        Returns:
            list: List of review dictionaries
        """
        self.log(f"Fetching {self.reviews_per_sort} reviews sorted by {sort_name}...")
        
        try:
            result, continuation_token = reviews(
                self.app_id,
                lang=self.lang,
                country=self.country,
                sort=sort_type,
                count=self.reviews_per_sort
            )
            
            # Add metadata to each review
            for review in result:
                review['sort_method'] = sort_name
                review['fetched_at'] = datetime.now().isoformat()
                
            self.log(f"✓ Successfully fetched {len(result)} reviews ({sort_name})")
            return result
            
        except Exception as e:
            self.log(f"✗ Error fetching reviews ({sort_name}): {str(e)}", "ERROR")
            return []
    
    def fetch_all_reviews(self):
        """Fetch reviews using all sorting methods"""
        self.log("=" * 60)
        self.log(f"Starting review scraping for app: {self.app_id}")
        self.log("=" * 60)
        
        # Fetch reviews with different sorting methods
        newest_reviews = self.fetch_reviews_by_sort(Sort.NEWEST, "NEWEST")
        relevant_reviews = self.fetch_reviews_by_sort(Sort.MOST_RELEVANT, "MOST_RELEVANT")
        rating_reviews = self.fetch_reviews_by_sort(Sort.RATING, "RATING")
        
        # Combine all reviews
        self.all_reviews = newest_reviews + relevant_reviews + rating_reviews
        
        # Remove duplicates based on reviewId
        unique_reviews = {}
        for review in self.all_reviews:
            review_id = review.get('reviewId')
            if review_id and review_id not in unique_reviews:
                unique_reviews[review_id] = review
        
        self.all_reviews = list(unique_reviews.values())
        
        self.log("=" * 60)
        self.log(f"Total unique reviews collected: {len(self.all_reviews)}")
        self.log("=" * 60)
        
        return self.all_reviews
    
    def prepare_dataframe(self):
        """Convert reviews to a pandas DataFrame with selected fields"""
        if not self.all_reviews:
            self.log("No reviews to process", "WARNING")
            return None
        
        # Extract important fields for sentiment analysis
        processed_reviews = []
        for review in self.all_reviews:
            processed_reviews.append({
                'review_id': review.get('reviewId'),
                'user_name': review.get('userName'),
                'rating': review.get('score'),
                'review_text': review.get('content'),
                'thumbs_up_count': review.get('thumbsUpCount', 0),
                'review_created_version': review.get('reviewCreatedVersion'),
                'at': review.get('at'),
                'reply_content': review.get('replyContent'),
                'replied_at': review.get('repliedAt'),
                'sort_method': review.get('sort_method'),
                'fetched_at': review.get('fetched_at')
            })
        
        df = pd.DataFrame(processed_reviews)
        
        # Sort by rating and thumbs up count for better analysis
        df = df.sort_values(by=['rating', 'thumbs_up_count'], ascending=[True, False])
        
        return df
    
    def save_to_json(self, filename=None):
        """Save reviews to JSON file"""
        if not self.all_reviews:
            self.log("No reviews to save", "WARNING")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"google_play_reviews_{self.app_id}_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.all_reviews, f, indent=2, ensure_ascii=False, default=str)
            
            self.log(f"✓ Saved {len(self.all_reviews)} reviews to {filename}")
            return filename
            
        except Exception as e:
            self.log(f"✗ Error saving JSON: {str(e)}", "ERROR")
            return None
    
    def save_to_csv(self, filename=None):
        """Save reviews to CSV file"""
        df = self.prepare_dataframe()
        
        if df is None or df.empty:
            self.log("No reviews to save", "WARNING")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"google_play_reviews_{self.app_id}_{timestamp}.csv"
        
        try:
            df.to_csv(filename, index=False, encoding='utf-8')
            self.log(f"✓ Saved {len(df)} reviews to {filename}")
            return filename
            
        except Exception as e:
            self.log(f"✗ Error saving CSV: {str(e)}", "ERROR")
            return None
    
    def get_review_statistics(self):
        """Generate basic statistics about the reviews"""
        if not self.all_reviews:
            return None
        
        df = self.prepare_dataframe()
        
        stats = {
            'total_reviews': len(df),
            'average_rating': df['rating'].mean(),
            'rating_distribution': df['rating'].value_counts().to_dict(),
            'reviews_with_replies': len(df[df['reply_content'].notna()]),
            'total_thumbs_up': df['thumbs_up_count'].sum(),
            'reviews_by_sort_method': df['sort_method'].value_counts().to_dict()
        }
        
        self.log("=" * 60)
        self.log("REVIEW STATISTICS")
        self.log("=" * 60)
        self.log(f"Total Reviews: {stats['total_reviews']}")
        self.log(f"Average Rating: {stats['average_rating']:.2f}/5.0")
        self.log(f"Rating Distribution: {stats['rating_distribution']}")
        self.log(f"Reviews with Developer Replies: {stats['reviews_with_replies']}")
        self.log(f"Total Thumbs Up: {stats['total_thumbs_up']}")
        self.log("=" * 60)
        
        return stats


def main():
    """Main execution function"""
    # Priority order for APP_ID:
    # 1. Command line argument
    # 2. Environment variable from .env file
    # 3. Error if neither is provided
    
    APP_ID = None
    
    # Check command line argument first
    if len(sys.argv) > 1:
        APP_ID = sys.argv[1]
    # Then check environment variable
    elif os.getenv('APP_ID'):
        APP_ID = os.getenv('APP_ID')
    else:
        print("\n" + "=" * 60)
        print("ERROR: No APP_ID provided!")
        print("=" * 60)
        print("\nPlease provide an APP_ID using one of these methods:")
        print("  1. Command line: python scrape-reviews.py com.your.app.id")
        print("  2. .env file: Create a .env file with APP_ID=com.your.app.id")
        print("\nExample .env file content:")
        print("  APP_ID=com.whatsapp")
        print("=" * 60 + "\n")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("GOOGLE PLAY STORE REVIEW SCRAPER")
    print("=" * 60)
    print(f"App ID: {APP_ID}")
    print("=" * 60 + "\n")
    
    # Initialize scraper
    scraper = GooglePlayReviewScraper(
        app_id=APP_ID,
        reviews_per_sort=200,  # Fetch 200 reviews per sorting method
        lang='en',
        country='us'
    )
    
    # Fetch all reviews
    reviews_data = scraper.fetch_all_reviews()
    
    if not reviews_data:
        print("\n[ERROR] No reviews were fetched. Please check the app ID and try again.")
        sys.exit(1)
    
    # Save to both formats
    json_file = scraper.save_to_json()
    csv_file = scraper.save_to_csv()
    
    # Display statistics
    stats = scraper.get_review_statistics()
    
    print("\n" + "=" * 60)
    print("SCRAPING COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"JSON file: {json_file}")
    print(f"CSV file: {csv_file}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
