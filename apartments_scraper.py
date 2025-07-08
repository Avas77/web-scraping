from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from save_to_csv import save_to_csv

# config setup
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_apartments(url="https://www.apartments.com/johnson-city-tn/"):
    driver.get(url)
    time.sleep(3)
    listings = driver.find_elements(By.CLASS_NAME, 'placard')
    rows = []
    for listing in listings:
        try:
            title = listing.find_element(By.CLASS_NAME, "property-title").text.strip()
            price = listing.find_element(By.CLASS_NAME, "property-pricing").text.strip()
            address = listing.find_element(By.CLASS_NAME, "property-address").text.strip()
            bed_bath = listing.find_element(By.CLASS_NAME, "property-beds").text.strip()
            link = listing.find_element(By.CLASS_NAME, "property-link").get_attribute("href")
            rows.append([title, price, address, bed_bath, link])
        except NoSuchElementException:
            continue
    return rows

if __name__ == '__main__':
    listings = scrape_apartments()
    save_to_csv(listings, ["Title", "Price", "Address", "Bed Bath", "Link"], "apartments_data.csv")
    driver.quit()
    print("✅ Scraping completed. Data saved to apartments_data.csv")