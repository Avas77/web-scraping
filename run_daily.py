import schedule
import time
from scraper import scrape_craigslist, save_to_csv

def job():
    print("🔄 Running scheduled job...")
    listings = scrape_craigslist()
    save_to_csv(listings)
    print("✅ Job done!")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)