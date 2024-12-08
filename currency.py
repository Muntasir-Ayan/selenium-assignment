from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Navigate to the property page
driver.get("https://www.alojamiento.io/property/campo-lindo-apartment/BC-1935047")  # Replace with actual URL

# Function to change the currency and verify that the property tile's price updates correctly
def change_currency_and_verify(currency_symbol):
    try:
        # Wait for the currency dropdown to be visible and clickable
        currency_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "js-currency-sort-footer"))
        )
        
        # Scroll the currency dropdown into view and click it
        driver.execute_script("arguments[0].scrollIntoView(true);", currency_dropdown)
        currency_dropdown.click()

        # Wait for the options to be visible in the dropdown
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='select-ul']//li"))
        )

        # Select the currency option from the dropdown by matching the currency symbol
        currency_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(., '{currency_symbol}')]"))
        )
        
        # Use ActionChains to click the option
        actions = ActionChains(driver)
        actions.move_to_element(currency_option).click().perform()

        # Wait for the property tile prices to update with the selected currency symbol
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class='property-tile']//span[@class='price']"), currency_symbol
            )
        )

        # Verify that the property tiles reflect the selected currency symbol
        property_tiles = driver.find_elements(By.XPATH, "//div[@class='property-tile']//span[@class='price']")
        
        for tile in property_tiles:
            price_text = tile.text
            assert currency_symbol in price_text, f"Price in tile does not display {currency_symbol}: {price_text}"
        print(f"Currency change to {currency_symbol} was successful.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Test: Verify currency change to USD
change_currency_and_verify("$")

# Test: Verify currency change to EUR
change_currency_and_verify("€")

# Test: Verify currency change to GBP
change_currency_and_verify("£")

# Test: Verify currency change to AED
change_currency_and_verify("د.إ.‏")

# Optionally, add a small delay to inspect results before quitting
time.sleep(3)

# Close the browser
driver.quit()
