"""
Main web scraping script
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging
from typing import List, Dict
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebScraper:
    """A simple web scraper for educational purposes"""
    
    def __init__(self, base_url: str = "http://books.toscrape.com/"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a webpage"""
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def scrape_books(self, max_pages: int = 1) -> List[Dict]:
        """Scrape book information from the website"""
        all_books = []
        
        for page_num in range(1, max_pages + 1):
            if page_num == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}catalogue/page-{page_num}.html"
            
            soup = self.fetch_page(url)
            if not soup:
                continue
            
            books = self.extract_books_from_page(soup)
            all_books.extend(books)
            
            logger.info(f"Page {page_num}: Found {len(books)} books")
            time.sleep(1)  # Be polite to the server
        
        return all_books
    
    def extract_books_from_page(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract book data from a single page"""
        books = []
        
        for article in soup.find_all('article', class_='product_pod'):
            try:
                title = article.h3.a['title']
                price = article.find('p', class_='price_color').text
                availability = article.find('p', class_='instock availability').text.strip()
                rating = article.p['class'][1]  # Extract rating from class names
                
                books.append({
                    'title': title,
                    'price': price,
                    'availability': availability,
                    'rating': rating
                })
            except (AttributeError, KeyError) as e:
                logger.warning(f"Error parsing book: {e}")
                continue
        
        return books
    
    def save_to_csv(self, data: List[Dict], filename: str = "scraped_data.csv"):
        """Save scraped data to CSV file"""
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        logger.info(f"Data saved to {filename}")
        return df

def main():
    """Main function to run the scraper"""
    logger.info("Starting web scraper...")
    
    # Initialize scraper
    scraper = WebScraper()
    
    # Scrape data (limit to 2 pages for demo)
    logger.info("Scraping book data...")
    books_data = scraper.scrape_books(max_pages=2)
    
    if books_data:
        # Save and display results
        df = scraper.save_to_csv(books_data, "books_data.csv")
        
        # Print summary
        logger.info(f"Scraping completed successfully!")
        logger.info(f"Total books scraped: {len(books_data)}")
        logger.info(f"Sample data:\n{df.head().to_string()}")
    else:
        logger.error("No data was scraped")
        sys.exit(1)

if __name__ == "__main__":
    main()
