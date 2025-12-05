#!/usr/bin/env python3
"""
Apple App Store Review Scraper
Fetches reviews from multiple countries and saves to JSON and CSV formats
Uses app-store-web-scraper library
"""

import json
import pandas as pd
from app_store_web_scraper import AppStoreEntry
from datetime import datetime
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AppleAppStoreReviewScraper:
    """Scraper for Apple App Store reviews with multi-country support"""
    
    def __init__(self, app_id, countries=['us'], reviews_count=200):
        """
        Initialize the scraper
        
        Args:
            app_id (str): Apple App Store app ID (numeric)
            countries (list): List of country codes to fetch reviews from
            reviews_count (int): Number of reviews to fetch per country
        """
        self.app_id = app_id
        self.countries = countries
        self.reviews_count = reviews_count
        self.all_reviews = []
        
    def log(self, message, level="INFO"):
        """Print formatted log messages"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
        
    def fetch_reviews_by_country(self, country):
        """
        Fetch reviews from a specific country
        
        Args:
            country (str): Country code (e.g., 'us', 'gb', 'ca')
            
        Returns:
            list: List of review dictionaries
        """
        self.log(f"Fetching reviews from {country.upper()}...")
        
        try:
            entry = AppStoreEntry(app_id=self.app_id, country=country)
            reviews_list = []
            
            # Fetch reviews using the entry (limit manually)
            count = 0
            for review in entry.reviews():
                if count >= self.reviews_count:
                    break
                    
                review_dict = {
                    'review_id': review.id,
                    'user_name': review.user_name,
                    'rating': review.rating,
                    'title': review.title,
                    'review': review.content,  # Use 'content' instead of deprecated 'review'
                    'date': str(review.date) if review.date else None,
                    'developer_response': getattr(review, 'developer_response', None),
                    'country': country,
                    'fetched_at': datetime.now().isoformat()
                }
                reviews_list.append(review_dict)
                count += 1
            
            self.log(f"✓ Successfully fetched {len(reviews_list)} reviews from {country.upper()}")
            return reviews_list
            
        except Exception as e:
            self.log(f"✗ Error fetching reviews from {country.upper()}: {str(e)}", "ERROR")
            return []
    
    def fetch_all_reviews(self):
        """Fetch reviews from all specified countries"""
        self.log("=" * 60)
        self.log(f"Starting review scraping for App ID: {self.app_id}")
        self.log(f"Countries: {', '.join([c.upper() for c in self.countries])}")
        self.log("=" * 60)
        
        # Fetch reviews from each country
        for country in self.countries:
            country_reviews = self.fetch_reviews_by_country(country)
            self.all_reviews.extend(country_reviews)
        
        # Remove duplicates based on review_id
        unique_reviews = {}
        for review in self.all_reviews:
            review_id = review.get('review_id')
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
                'review_id': review.get('review_id'),
                'user_name': review.get('user_name'),
                'rating': review.get('rating'),
                'title': review.get('title'),
                'review_text': review.get('review'),
                'date': review.get('date'),
                'developer_response': review.get('developer_response'),
                'country': review.get('country'),
                'fetched_at': review.get('fetched_at')
            })
        
        df = pd.DataFrame(processed_reviews)
        
        # Sort by rating and date for better analysis
        if 'date' in df.columns and not df['date'].isna().all():
            df = df.sort_values(by=['rating', 'date'], ascending=[True, False])
        else:
            df = df.sort_values(by=['rating'], ascending=[True])
        
        return df
    
    def save_to_json(self, filename=None):
        """Save reviews to JSON file"""
        if not self.all_reviews:
            self.log("No reviews to save", "WARNING")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"app_store_reviews_{self.app_id}_{timestamp}.json"
        
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
            filename = f"app_store_reviews_{self.app_id}_{timestamp}.csv"
        
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
            'average_rating': df['rating'].mean() if 'rating' in df.columns else 0,
            'rating_distribution': df['rating'].value_counts().to_dict() if 'rating' in df.columns else {},
            'reviews_with_developer_response': len(df[df['developer_response'].notna()]) if 'developer_response' in df.columns else 0,
            'reviews_by_country': df['country'].value_counts().to_dict() if 'country' in df.columns else {}
        }
        
        self.log("=" * 60)
        self.log("REVIEW STATISTICS")
        self.log("=" * 60)
        self.log(f"Total Reviews: {stats['total_reviews']}")
        self.log(f"Average Rating: {stats['average_rating']:.2f}/5.0")
        self.log(f"Rating Distribution: {stats['rating_distribution']}")
        self.log(f"Reviews with Developer Response: {stats['reviews_with_developer_response']}")
        self.log(f"Reviews by Country: {stats['reviews_by_country']}")
        self.log("=" * 60)
        
        return stats


def main():
    """Main execution function"""
    # Priority order for APP configuration:
    # 1. Command line arguments
    # 2. Environment variables from .env file
    # 3. Error if neither is provided
    
    APP_ID = None
    COUNTRIES = ['us']  # Default to US
    
    # Check command line arguments first
    if len(sys.argv) > 1:
        APP_ID = sys.argv[1]
        if len(sys.argv) > 2:
            COUNTRIES = sys.argv[2].split(',')
    # Then check environment variables
    elif os.getenv('APP_ID'):
        APP_ID = os.getenv('APP_ID')
        if os.getenv('COUNTRIES'):
            COUNTRIES = os.getenv('COUNTRIES').split(',')
    else:
        print("\n" + "=" * 60)
        print("ERROR: No APP_ID provided!")
        print("=" * 60)
        print("\nPlease provide APP_ID using one of these methods:")
        print("  1. Command line: python scrape-reviews.py <APP_ID> [COUNTRIES]")
        print("     Example: python scrape-reviews.py 310633997 us,gb,ca")
        print("\n  2. .env file: Create a .env file with:")
        print("     APP_ID=310633997")
        print("     COUNTRIES=us,gb,ca  # Optional, defaults to 'us'")
        print("\nHow to find APP_ID:")
        print("  URL: https://apps.apple.com/us/app/whatsapp-messenger/id310633997")
        print("       APP_ID: 310633997 (the numeric ID at the end)")
        print("\nPopular App IDs:")
        print("  WhatsApp: 310633997")
        print("  Instagram: 389801252")
        print("  TikTok: 835599320")
        print("  Spotify: 324684580")
        print("=" * 60 + "\n")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("APPLE APP STORE REVIEW SCRAPER")
    print("=" * 60)
    print(f"App ID: {APP_ID}")
    print(f"Countries: {', '.join(COUNTRIES)}")
    print("=" * 60 + "\n")
    
    # Initialize scraper
    scraper = AppleAppStoreReviewScraper(
        app_id=APP_ID,
        countries=COUNTRIES,
        reviews_count=200  # Fetch 200 reviews per country
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
