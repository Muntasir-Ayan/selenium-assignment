# Vacation Rental Home Page Automation Testing

## Description
This project automates the testing of a vacation rental details page to validate essential elements and functionality for SEO optimization. The script checks for the following test cases:

- **H1 tag existence**: Ensures the presence of the H1 tag on the page.
- **HTML tag sequence**: Verifies the correct sequence of header tags (`H1-H6`).
- **Image alt attribute**: Checks if all images have an `alt` attribute for SEO purposes.
- **URL status code**: Verifies that all internal URLs are working and not returning a 404 status code.
- **Currency filter functionality**: Tests the currency filter to ensure property tiles reflect the currency change.
- **Scrape and record data**: Scrapes the page for relevant information (SiteURL, CampaignID, SiteName, Browser, CountryCode, IP) and stores the results in an Excel file.


# Prerequisites

Before getting started, ensure the following tools are installed on your system:

- **Python 3.7 or later**  
  Download and install Python from the official website: [python.org/downloads](https://www.python.org/downloads/)

- **Google Chrome**  
  Download the latest version of Chrome here: [google.com/chrome](https://www.google.com/chrome/)


## Requirements

- **Libraries**:
    - `Selenium`: For browser automation.
    - `Pandas`: For data manipulation and storing results in Excel.
    - `openpyxl`: For Excel file support in Pandas.
    - `webdriver-manager`: For managing the WebDriver installation.
 ---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Muntasir-Ayan/selenium-assignment.git
   cd selenium-assignment


2. **Create and activate a virtual environment**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
3. **Install project dependencies**:
   ```bash
    pip install -r requirements.txt
## Running Test Script
1. **Run all Script at once**:
   ```bash
    python main.py
   ```
2. **Or, Individually run each file**:
    ```bash
    python h1_test.py
## Test Report
- The test results are saved in an Excel file named test_report.xlsx.

- Each execution generates a new sheet in the file.

## Contributing

Contributions are welcome! Please follow these steps:

- Fork the repository.

- Create a new feature branch (git checkout -b feature-name).

- Commit your changes (git commit -m 'Add feature').

- Push to the branch (git push origin feature-name).

- Open a pull request.

## Contact

For any inquiries or support, feel free to contact:

Name: Muntasir Ayan

Email: mjayan439@gmail.com

