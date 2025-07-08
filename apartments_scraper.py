from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import csv

# config setup
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_apartments(url="https://www.apartments.com/johnson-city-tn/"):
    driver.get(url)
    time.sleep(3)
    listings = driver.find_elements(By.CLASS_NAME, 'placard')
    for listing in listings:
        try:
            title = listing.find_element(By.CLASS_NAME, "property-title").text.strip()
            price = listing.find_element(By.CLASS_NAME, "property-pricing").text.strip()
            address = listing.find_element(By.CLASS_NAME, "property-address").text.strip()
            bed_bath = listing.find_element(By.CLASS_NAME, "property-beds").text.strip()
            link = listing.find_element(By.CLASS_NAME, "property-link").get_attribute("href")
        except NoSuchElementException:
            continue
    print(f"{title}, {price}, {address}, {bed_bath}, {link}")

scrape_apartments()

driver.quit()
print("✅ Scraping completed. Data saved to apartments_data.csv")