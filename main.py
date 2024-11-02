from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Wait for the username field to load and enter the username
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username.send_keys("*************")  # Replace with your LinkedIn username
time.sleep(5)

# Enter the password
password = driver.find_element(By.ID, "password")
password.send_keys("***********")  # Replace with your LinkedIn password
time.sleep(5)

# Click the 'Sign in' button
sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
sign_in_button.click()

# Wait for the homepage to load after logging in
WebDriverWait(driver, 10).until(
    EC.title_contains("Feed")
)

# Continue with the rest of your script
elem = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')  # Adjust as necessary
elem.clear()
elem.send_keys("amazon talent acquisition @ Hyderabad")
elem.send_keys(Keys.RETURN)

# Ensure the results are loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'search-results')]"))
)

# Optional: Check if "No results found" is present
assert "No results found." not in driver.page_source

# Wait for visibility or interactions as needed
time.sleep(12)

# Close the driver
driver.close()
