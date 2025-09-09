from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

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
driver.get("https://uat.skyeairops.tech/operator/cod")
time.sleep(2)

# Print the page title
print(driver.title)

username = driver.find_element(By.ID, value="emailId")
username.send_keys("atul.tiwari@skyeair.tech")
time.sleep(2)

# Password field
password = driver.find_element(By.ID, value="floatingPassword")
password.send_keys("Atul@123")
time.sleep(2)

# Login 
Login = driver.find_element(By.XPATH, '//button[@type="submit"]')
Login.click()
time.sleep(3)

element = driver.find_element(By.XPATH, "//mat-icon[text()='keyboard_arrow_down']")
element.click()
print("Clicked")
time.sleep(3)

element = driver.find_element(By.XPATH, "//button[contains(., 'Schedule Flight Via Excel')]")
element.click()
print(" Schedule Flight Via Excel ")
time.sleep(3)

# element = driver.find_element(By .XPATH, "//select[@aria-label='Select Organization'])[1]")
# element.click()
# print("Client Selected")
# time.sleep(5)
# Wait for the dropdown to be present
wait = WebDriverWait(driver, 4)
dropdown_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Select Organization']"))
)
# time.sleep(3)

# Wrap the element with Select class
select = Select(dropdown_element)
# time.sleep(3)

# Select the Flipkart option by visible text
select.select_by_visible_text("Flipkart -- Flipkart-00001")
# time.sleep(3)



wait = WebDriverWait(driver, 4)

# Wait for all dropdowns to appear
dropdowns = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "select")))

# Loop through to find the one with the hub
target_hub_code = "HB089"
hub_select = None

for dropdown in dropdowns:
    select = Select(dropdown)
    # time.sleep(5)
    for option in select.options:
        if target_hub_code in option.text:
            hub_select = select
            break
    if hub_select:
        break

if hub_select:
    for option in hub_select.options:
        if target_hub_code in option.text:
            hub_select.select_by_visible_text(option.text.strip())
            print(f"✅ Selected hub: '{option.text.strip()}'")
            # time.sleep(5)
            break
else:
    print(f"❌ Hub with code {target_hub_code} not found in any dropdown.")



# Locate the input element
# excel = driver.find_element(By.XPATH, "//input[@id='uploadImage']")

# # Upload file instead of clicking
# excel.send_keys(r"C:\Users\Skyeair-User\Downloads\4 june.xlsx")

# print("Uploaded Excel file.")
# time.sleep(5)  

# wait = WebDriverWait(driver, 10)
# amount_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='0' and @type='number']")))
# print("amount")
# amount_input.clear()
# amount_input.send_keys("100")


print("⏳ Waiting for amount input to appear...")

wait = WebDriverWait(driver, 60)  # give more time after upload
amount_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='0' and @type='number']"))
)

print("✅ Amount input found")
amount_input.clear()
amount_input.send_keys("100")

schedule_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Schedule Flight']")
schedule_btn.click()
time.sleep(15)
