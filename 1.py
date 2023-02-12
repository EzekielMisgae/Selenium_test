import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestGojoWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://gojo.herokuapp.com")

    def test_login(self):
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

    def test_navigate_to_search(self):
        # self.test_login()
        wait = WebDriverWait(self.driver, 10)
        # Wait for the search button to be visible
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_button.click()
        
        # Wait for the submit button to be visible
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
        time.sleep(5)

    def test_navigate_to_home(self):
        self.test_login()
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the search button to be visible
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_button.click()
        
        # Wait for the submit button to be visible
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
        
        # Wait for the home button to be visible
        home_button = wait.until(EC.element_to_be_clickable((By.ID, "home")))
        home_button.click()
        time.sleep(5)

    def test_navigate_to_home(self):
        self.test_login()
        wait = WebDriverWait(self.driver, 10)

        # Wait for the sign out button to be visible
        sign_out_button = wait.until(EC.element_to_be_clickable((By.ID, "logout")))
        sign_out_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()