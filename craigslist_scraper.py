import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_craigslist(url="https://tricities.craigslist.org/search/apa"):
    headers = {'User-Agent': 'Mozilla/5.0'} 
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    listings = soup.find_all("li", class_="cl-static-search-result")

    rows = []

    for listing in listings:
        try:
            title = listing.find('div', class_="title").text
            price = listing.find('div', class_="price").text
            loc_tag = listing.find('div', class_="location")
            location = loc_tag.get_text(strip=True) if loc_tag else None
            link = listing.find('a')['href']
            rows.append([title, price, location, link])
        except Exception as e:
            print("Skipping listing due to error:", e)
    return rows

def save_to_csv(rows, filename='rentals.csv'):
    try:
        with open(filename, 'x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Price', 'Location', 'Link'])
            writer.writerows(rows)
    except FileExistsError:
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

if __name__ == '__main__':
    listings = scrape_craigslist()
    save_to_csv(listings)
    print(f"✅ Scraped and saved {len(listings)} listings at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")