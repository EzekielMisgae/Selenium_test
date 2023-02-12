from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')
driver.get("https://gojo.herokuapp.com")

wait = WebDriverWait(driver, 10)
sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "Sign-in")))
sign_in_button.click()

# Login code here
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_field.send_keys("check")
password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_field.send_keys("Pass4321")
click_sign_in = wait.until(EC.element_to_be_clickable((By.ID, "sign-in")))
click_sign_in.click()
# Wait for the About Me button to be visible
about_me_button = wait.until(EC.element_to_be_clickable((By.ID, "about")))
about_me_button.click()

# Wait for the Home button to be visible
home_button = wait.until(EC.element_to_be_clickable((By.ID, "home")))
home_button.click()

# Wait for the Sign Out button to be visible
sign_out_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "logout")))
sign_out_button.click()

driver.close()





# # Wait for 10 seconds
# time.sleep(10)

# # Login using username and password
# driver.find_element(By.ID, "sign-in").click()
# username = driver.find_element(By.ID, "username")
# password = driver.find_element(By.ID, "password")
# username.send_keys("check")
# password.send_keys("check")
# driver.find_element_by_xpath("//input[@value='Login']").click()

# # Wait for 10 seconds
# time.sleep(10)

# # Find the text 'About Me' in the navbar and click on it
# driver.find_element(By.LINK_TEXT, "About Me").click()

# # Wait for 10 seconds
# time.sleep(10)

# # Find the text 'Home' in the navbar and click on it
# driver.find_element(By.LINK_TEXT, "Home").click()

# # Wait for 10 seconds
# time.sleep(10)

# # Find the text 'Sign Out' in the navbar and click on it
# driver.find_element(By.LINK_TEXT, "Sign Out").click()

# # Wait for 10 seconds
# time.sleep(10)

# # Close the tab
# driver.close()