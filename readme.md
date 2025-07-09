# Real Estate Rental Listings Scraper & Dashboard

This project collects real estate rental listings from two different platforms using two distinct web scraping techniques. The data collected is intended for analytics and dashboarding in Power BI, enabling users to analyze rental market trends based on real-time listing data.

---

## Overview
The project consists of two independent web scrapers:

1. **Craigslist Scraper** – Uses `requests` and `BeautifulSoup` to extract data from Craigslist.
2. **Apartments.com Scraper** – Uses `Selenium` to extract data from JavaScript-heavy pages on Apartments.com.

Both scrapers store the collected data into CSV files for further analysis.

---

## Scraper 1: Craigslist (Static Website)
### Scraping Technique: `requests` + `BeautifulSoup`
Craigslist uses static HTML pages which are ideal for lightweight web scraping. This scraper sends an HTTP request to the rental listings page, parses the HTML content, and extracts key information like:
- Title
- Price
- Date Posted
- Link to Listing

**Advantages:**
- Fast and efficient
- Low resource usage
- Minimal anti-bot protections

**Use Case:**
Ideal for scraping basic information from pages that don't require JavaScript to load content.

---

## Scraper 2: Apartments.com (Dynamic Website)
### Scraping Technique: `Selenium`
Apartments.com relies heavily on JavaScript to render property listings. To handle this, the scraper uses Selenium to simulate a real web browser that can wait for content to load and interact with the page if necessary. It extracts:
- Property Title
- Address
- Price Range
- Bed/Bath Count
- Listing URL

**Advantages:**
- Capable of interacting with JavaScript-rendered content
- Supports pagination and element interaction (e.g., clicking "Next")

**Use Case:**
Best suited for scraping complex or interactive web pages that render data dynamically.

---

## Output
Both scrapers save the extracted data as CSV files (`craigslist_data.csv` and `apartments_data.csv`). These can be imported into Power BI or any other analytics platform for visualization and trend analysis.

---

## Dashboard Integration
The project is designed with future integration into Power BI dashboards. Users can:
- Analyze rental price trends by city or neighborhood
- Compare listings across platforms
- Monitor real estate availability over time

---

## Ethical Use & Disclaimer
This project is for **educational and personal use only**. Please ensure compliance with each website's Terms of Use and `robots.txt` policies. Avoid high-frequency scraping to prevent overloading servers or violating usage terms.

---

## Future Enhancements
- Automate daily scraping with Airflow or Windows Task Scheduler
- Normalize and merge datasets from both platforms
- Add additional sources (e.g., Zillow, Facebook Marketplace)
- Push data to a centralized database or cloud storage

