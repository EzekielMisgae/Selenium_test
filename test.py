import random
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebsiteNavigation(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_website_navigation(self):
        websites = ['https://www.python.org/', 'https://www.github.com/']
        website = random.choice(websites)
        self.driver.get(website)
        self.assertEqual(self.driver.current_url, website)
        
        self.driver.find_element_by_link_text('Downloads').click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website + 'downloads/')
        
        self.driver.back()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website)
        
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertTrue('Results for "selenium"' in self.driver.page_source)
        
        self.driver.find_element_by_link_text('Documentation').click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website + 'doc/')
        
        self.driver.back()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website)
        
        self.driver.find_element_by_link_text('About').click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website + 'about/')
        self.assertTrue('About' in self.driver.title)
        
        self.driver.back()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website)
        
        self.driver.find_element_by_link_text('Community').click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, website + 'community/')
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()