import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestGojoWebsite(unittest.TestCase):

    def setUp(self):   #Setting up Chrome driver, navigating to website, and maximizing window for testing.
        self.driver = webdriver.Chrome()
        self.driver.get("http://gojo.herokuapp.com")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_navigate_to_search(self):   #Navigates to search page after logging in and clicks search and submit buttons with wait times.
        self.test_login()
        # Wait for the search button to be visible
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_button.click()
        time.sleep(1)
        submit_button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
        time.sleep(3)

    def test_navigate_to_home(self):  #Navigates to home page after logging in.
        self.test_login()
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, "profile")))
        search_button.click()
        time.sleep(3)
        home_button = self.wait.until(EC.element_to_be_clickable((By.ID, "home")))
        home_button.click()
        time.sleep(3)

    def test_sign_out(self): #Test sign-out functionality by logging in, waiting 2 secs, and clicking logout button.
        self.test_login()
        time.sleep(2)
        sign_out_button = self.wait.until(EC.element_to_be_clickable((By.ID, "logout")))
        sign_out_button.click()

    def test_post_homes(self):  #Code waits for "post_homes" button to be clickable and then clicks it, with waits in between.
        time.sleep(5)
        post_homes_button = self.wait.until(EC.element_to_be_clickable((By.ID, "post_homes")))
        post_homes_button.click()
        time.sleep(3)

    def test_login(self):
        # Login
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "Sign-in")))
        sign_in_button.click()

        # Login fields
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("check")
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("Pass4321")
        click_sign_in = self.wait.until(EC.element_to_be_clickable((By.ID, "sign-in")))
        click_sign_in.click()

    def tearDown(self): #Closes each test/func after completion.
        self.driver.close()

def test_suite(): #Creating a test suite for TestGojoWebsite by adding 4 test cases
    suite = unittest.TestSuite()
    suite.addTest(TestGojoWebsite("test_navigate_to_search"))
    suite.addTest(TestGojoWebsite("test_navigate_to_home"))
    suite.addTest(TestGojoWebsite("test_sign_out"))
    suite.addTest(TestGojoWebsite("test_post_homes")) #Fails since there is no element by ID called "post_homes" in the first page.
    return suite

if __name__ == "__main__": # Runs test suite with verbosity 2 via unittest TextTestRunner if module is executed as main program.
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite())