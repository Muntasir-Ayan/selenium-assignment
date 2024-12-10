from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # Initialize WebDriver
    driver = webdriver.Chrome()
    
    # Navigate to the URL
    url = "https://www.alojamiento.io/property/campo-lindo-apartment/BC-1935047"
    driver.get(url)
    driver.maximize_window()

    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "js-currency-sort-footer")))

    # Locate the currency dropdown
    currency_dropdown = driver.find_element(By.ID, "js-currency-sort-footer")
    action = ActionChains(driver)
    action.move_to_element(currency_dropdown).perform()  # Ensure dropdown is visible

    # Click the dropdown to expand it
    driver.execute_script("arguments[0].click();", currency_dropdown)
    time.sleep(1)  # Allow time for the dropdown to expand

    # Fetch <li> elements in the dropdown
    li_elements = driver.find_elements(By.XPATH, "//*[@id='js-currency-sort-footer']//ul[@class='select-ul']//li")

    print(f"Number of <li> elements: {len(li_elements)}")

    # Iterate and click each currency option
    for i in range(len(li_elements)):
        # Refetch the list of <li> elements
        li_elements = driver.find_elements(By.XPATH, "//*[@id='js-currency-sort-footer']//ul[@class='select-ul']//li")

        # Scroll the current element into view to make it interactable
        driver.execute_script("arguments[0].scrollIntoView(true);", li_elements[i])

        # Extract the currency text
        li_text = driver.execute_script("return arguments[0].querySelector('div.option > p').innerText;", li_elements[i])
        currency_symbol = li_text.split()[0]  # Extract the currency symbol (e.g., "$", "£", "€")
        print(f"Clicking on: {li_text.strip()}")

        # Click the currency option using JavaScript to avoid interactability issues
        driver.execute_script("arguments[0].click();", li_elements[i])
        
        # Wait for the page to update
        time.sleep(3)  # Adjust based on the site's responsiveness

        # Locate the default price element
        default_price_element = driver.find_element(By.ID, "js-default-price")
        
        # Extract the text from the default price element
        default_price_text = default_price_element.text
        print(f"Current default price: {default_price_text}")

        # Optionally, you could implement additional logic to verify if the currency reflects correctly

finally:
    # Close the browser
    driver.quit()
