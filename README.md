# Vacation Rental Home Page Automation Testing

## Description
This project automates the testing of a vacation rental details page to validate essential elements and functionality for SEO optimization. The script checks for the following test cases:

- **H1 tag existence**: Ensures the presence of the H1 tag on the page.
- **HTML tag sequence**: Verifies the correct sequence of header tags (`H1-H6`).
- **Image alt attribute**: Checks if all images have an `alt` attribute for SEO purposes.
- **URL status code**: Verifies that all internal URLs are working and not returning a 404 status code.
- **Currency filter functionality**: Tests the currency filter to ensure property tiles reflect the currency change.
- **Scrape and record data**: Scrapes the page for relevant information (SiteURL, CampaignID, SiteName, Browser, CountryCode, IP) and stores the results in an Excel file.

## Requirements

- **Python version**: 3.x
- **Libraries**:
    - `Selenium`: For browser automation.
    - `Pandas`: For data manipulation and storing results in Excel.
    - `openpyxl`: For Excel file support in Pandas.
    - `webdriver-manager`: For managing the WebDriver installation.

To install the required libraries, run:

```bash
pip install -r requirements.txt
