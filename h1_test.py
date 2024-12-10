from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Function to test the page and generate the result
def test_page(url, testcase):
    result = {"page_url": url, "testcase": testcase, "passed/fail": "", "comments": ""}
    
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the URL
        driver.get(url)

        # Wait for the H1 tag to be present
        h1_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # If we find the H1 tag, test is passed
        result["passed/fail"] = "passed"
        result["comments"] = f"H1 tag found: {h1_tag.text}"

    except Exception as e:
        # If any exception occurs, test fails
        result["passed/fail"] = "fail"
        result["comments"] = str(e)

    finally:
        # Close the driver after use
        driver.quit()
    
    return result

# Create a list to hold all test results
test_results = []

# Define the list of test cases (URLs and test case names)
test_cases = [
    {"url": "https://www.alojamiento.io/property/campo-lindo-apartment/BC-1935047", "testcase": "H1"},
    # Add more test cases here if needed
]

# Loop over each test case and run the tests
for case in test_cases:
    result = test_page(case["url"], case["testcase"])
    test_results.append(result)

# Convert the list of test results into a DataFrame (table format)
df = pd.DataFrame(test_results)

# Save the results to an Excel file
df.to_excel("test_report.xlsx", index=False)

print("H1 Test report generated successfully!")
