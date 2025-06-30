from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome Options for Allowing Notification
chrome_options = Options()      
prefs = {
    "profile.default_content_setting_values.notifications": 1  # 1 = Allow, 2 = Block
}
chrome_options.add_experimental_option("prefs", prefs)
# Launch Chrome with options        
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# Open the target URL
driver.get("https://www.skyeair.tech/")
# // print the page title
print("Page Title:", driver.title)
assert "Sky" in driver.title or "Air" in driver.title  # Adjust based on
time.sleep(7)


# Home Page
print(" Page loaded successfully.")

# close the Popup
try:
    close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
    close_popup.click()
    print("Popup closed successfully.")
except Exception as e:
    print("No popup found or failed to close:", e)

# Scroll to the bottom of the page to ensure all elements are loaded
import time

scroll_pause_time = 2  # seconds

# Get the total scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down by window height
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(scroll_pause_time)

    # Calculate new scroll height
    new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")

    if new_height >= last_height:
        break


FAQ = driver.find_element(By.XPATH, '//span[text()="What is Skye Air and how does drone delivery work?"]')
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", FAQ)
time.sleep(1)
driver.execute_script("arguments[0].click();", FAQ)
print("FAQ button clicked.")
time.sleep(2)

FAQ1 = driver.find_element(By.XPATH, '//span[text()="Which areas or cities in India does Skye Air currently operate in?"]')
FAQ1.click()
print("FAQ Button two..")
time.sleep(2)


FAQ2 = driver.find_element(By.XPATH, '//span[text()="What types of goods can be delivered using Skye Air drones?"]')
FAQ2.click()
print("FAQ Button Three...")
time.sleep(2)

# driver.quit()  # Close the browser after completion
# print("Browser closed.")



