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

    def test_navigate_to_search_and_search(self):   #Navigates to search page after logging in and clicks search and submit buttons with wait times.
        self.test_login()
        # Wait for the search button to be visible
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_button.click()
        self.assertEqual(self.driver.current_url, 'https://gojo.herokuapp.com/search/')
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
        self.assertEqual(self.driver.current_url, 'https://gojo.herokuapp.com/search/')
        time.sleep(3)

    def test_navigate_to_home(self):  #Navigates to home page after logging in.
        self.test_login()
        self.wait.until(EC.element_to_be_clickable((By.ID, "profile"))).click()
        self.assertEqual(self.driver.current_url, 'https://gojo.herokuapp.com/profile')
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.ID, "home"))).click()
        self.assertEqual(self.driver.current_url, 'https://gojo.herokuapp.com/homePage')
        time.sleep(3)

    def test_sign_out(self): #Test sign-out functionality by logging in, waiting 2 secs, and clicking logout button.
        self.test_login()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout"))).click()

    def test_post_homes(self):  #Code waits for "post_homes" button to be clickable and then clicks it, with waits in between.
        self.test_login()
        self.wait.until(EC.element_to_be_clickable((By.ID, "post_home"))).click()
        self.assertEqual(self.driver.current_url, 'https://gojo.herokuapp.com/create/')
        time.sleep(3)

    def test_login(self):
        # Login
        self.wait.until(EC.element_to_be_clickable((By.ID, "Sign-in"))).click()

        # Login fields
        self.wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("check")
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Pass4321")
        self.wait.until(EC.element_to_be_clickable((By.ID, "sign-in"))).click()
        self.assertEqual(self.driver.current_url, 'https://gojo.herokuapp.com/homePage')
        time.sleep(2)

    def tearDown(self): #Closes each test/func after completion.
        self.driver.close()

def test_suite(): #Creating a test suite for TestGojoWebsite by adding 4 test cases
    suite = unittest.TestSuite()
    suite.addTest(TestGojoWebsite("test_navigate_to_search_and_search"))
    suite.addTest(TestGojoWebsite("test_navigate_to_home"))
    suite.addTest(TestGojoWebsite("test_sign_out"))
    suite.addTest(TestGojoWebsite("test_post_homes")) #Fails since there is no element by ID called "post_homes" in the first page.
    return suite

if __name__ == "__main__": # Runs test suite with verbosity 2 via unittest TextTestRunner if module is executed as main program.
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite())