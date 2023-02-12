# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class TestGojoApp(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome('./chromedriver')
#         self.driver.get("https://gojo.herokuapp.com")
#     def test_login_and_navigate(self):
#         wait = WebDriverWait(self.driver, 10)

#         # Login
#         try:
#             sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "Sign-in")))
#             sign_in_button.click()
#             time.sleep(4)
#             print("Sign In button clicked")
#         except Exception as e:
#             print("Sign In button not found:", e)

#         # Login fields
#         try:
#             username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
#             username_field.send_keys("check")
#             password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
#             password_field.send_keys("Pass4321")
#             click_sign_in = wait.until(EC.element_to_be_clickable((By.ID, "sign-in")))
#             click_sign_in.click()
#             time.sleep(4)
#             print("Login successful")
#         except Exception as e:
#             print("Login fields not found:", e)

#         # Wait for the About Me button to be visible
#         try:
#             about_me_button = wait.until(EC.element_to_be_clickable((By.ID, "search")))
#             about_me_button.click()
#             wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
#             time.sleep(4)
#             print("About Me button clicked")
#         except Exception as e:
#             print("About Me button not found:", e)

#         # Wait for the Home button to be visible
#         try:
#             home_button = wait.until(EC.element_to_be_clickable((By.ID, "home")))
#             home_button.click()
#             time.sleep(4)
#             print("Home button clicked")
#         except Exception as e:
#             print("Home button not found:", e)

#         # Wait for the Sign Out button to be visible
#         try:
#             sign_out_button = wait.until(EC.element_to_be_clickable((By.ID, "logout")))
#             sign_out_button.click()
#             time.sleep(4)
#             print("Sign Out button clicked")
#         except Exception as e:
#             print("Sign Out button not found:", e)

#     def tearDown(self):
#         self.driver.close()
# if __name__ == '__main__':
#         unittest.main()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class TestGojoApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://gojo.herokuapp.com")
        
    def login(self):
        wait = WebDriverWait(self.driver, 10)
        
        # Login
        sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "Sign-in")))
        sign_in_button.click()
        
        # Login fields
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("check")
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("Pass4321")
        click_sign_in = wait.until(EC.element_to_be_clickable((By.ID, "sign-in")))
        click_sign_in.click()
        time.sleep(5)

    def test_search(self):
        self.login()
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the search button to be visible
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_button.click()
        
        # Wait for the submit button to be visible
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
        time.sleep(5)
        driver.quit()
        
    def test_home(self):
        self.login()
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the search button to be visible
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_button.click()
        
        # Wait for the submit button to be visible
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the home button to be visible
        home_button = wait.until(EC.element_to_be_clickable((By.ID, "home")))
        home_button.click()
        time.sleep(5)
        
    def test_logout(self):
        self.login()
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the sign out button to be visible
        sign_out_button = wait.until(EC.element_to_be_clickable((By.ID, "logout")))
        sign_out_button.click()
        time.sleep(5)
        
    def tearDown(self):
        self.driver.close()


    test_search()
    test_home()

# if __name__ == '__main__':
#         unittest.main()