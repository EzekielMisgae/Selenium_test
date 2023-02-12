# import unittest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time


# class TestGojoWebsite(unittest.TestCase):
#     def setUp(self):
#         try:
#             links = ['Sign-in', 'Get Started', 'About Gojo_Afalagi', 'About me']
#             for link in links:
#                 start_time = time.time()
#                 page = self.driver.find_element_by_link_text(link)
#                 page.click()
#                 end_time = time.time()
#                 print("{} loaded in {} seconds".format(link, end_time - start_time))
#                 self.pages_title.append(self.driver.title)
#         except Exception as e:
#             print("Error:", e)

#     def test_login_success(self):
#         try:
#             self.driver.find_element_by_class("getstarted scrollto").click()
#             self.driver.find_element_by_name("username").send_keys("example")
#             self.driver.find_element_by_name("password").send_keys("example_password")
#             self.driver.find_element_by_class("btn login_btn").click()

#             # Verify that the user is logged in by checking if the logout button is visible
#             logout_button = self.driver.find_element_by_id("logout")
#             assert logout_button.is_displayed()

#             print("Congratulations, you are successfully signed in.")

#         except Exception as e:
#             print("Error, login failed:", e)

#     def test_page_navigation(self):
#         try:
#             links = ['Sign-in', 'Get Started', 'About Gojo_Afalagi', 'About me']
#             for link in links:
#                 start_time = time.time()
#                 page = self.driver.find_element_by_link_text(link)
#                 page.click()
#                 end_time = time.time()
#                 print("{} loaded in {} seconds".format(link, end_time - start_time))
#                 self.pages_title.append(self.driver.title)
#         except Exception as e:
#             print("Error:", e)
            

#     def test_page_titles(self):

#         if len(set(self.pages_title)) == 4:
#             print("All 4 page titles are different.")
#         else:
#             print("Page titles are not different.")

#         if __name__ == "__main__":
#             unittest.main(argv=[''], exit=False)




# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# def open_browser():
#     # Open Chrome webdriver
#     driver = webdriver.Chrome(executable_path='./chromedriver')
#     return driver

# def navigate_to_website(driver):
#     # Go to the website link
#     driver.get("https://gojo.herokuapp.com/")
#     # Wait for 5 seconds
#     time.sleep(5)

# def login(driver):
#     # Login using username and password
#     driver.find_element(By.ID, "sign-in").click()
#     username = driver.find_element(By.ID, "username")
#     password = driver.find_element(By.ID, "password")
#     username.send_keys("check")
#     password.send_keys("check")
#     driver.find_element(By.XPATH, "//input[@value='Login']").click()
#     # Wait for 5 seconds
#     time.sleep(5)

# def go_to_about_me(driver):
#     # Find the text 'About Me' in the navbar and click on it
#     driver.find_element(By.LINK_TEXT, "About Me").click()
#     # Wait for 5 seconds
#     time.sleep(5)

# def go_to_home(driver):
#     # Find the text 'Home' in the navbar and click on it
#     driver.find_element(By.LINK_TEXT, "Home").click()
#     # Wait for 5 seconds
#     time.sleep(5)

# def sign_out(driver):
#     # Find the text 'Sign Out' in the navbar and click on it
#     driver.find_element(By.LINK_TEXT, "Sign Out").click()
#     # Wait for 5 seconds
#     time.sleep(5)

# def close_browser(driver):
#     # Close the browser
#     driver.quit()

# if __name__ == "__main__":
#     driver = open_browser()
#     navigate_to_website(driver)
#     login(driver)
#     go_to_about_me(driver)
#     go_to_home(driver)
#     sign_out(driver)
#     close_browser(driver)

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# class TestGojoWebsite(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path='./chromedriver')

#     def test_login(self):
#         driver = self.driver
#         driver.get("https://gojo.herokuapp.com/")
#         time.sleep(5)
#         driver.find_element(By.ID, "sign-in").click()
#         username = driver.find_element(By.ID, "username")
#         password = driver.find_element(By.ID, "password")
#         username.send_keys("check")
#         password.send_keys("check")
#         driver.find_element_by_xpath("//input[@value='Login']").click()
#         time.sleep(5)
#         self.assertIn("Gojo", driver.title)

#     def test_about_me(self):
#         driver = self.driver
#         driver.find_element(By.LINK_TEXT, "About Me").click()
#         time.sleep(5)
#         self.assertIn("About Me", driver.title)

#     def test_home(self):
#         driver = self.driver
#         driver.find_element(By.LINK_TEXT, "Home").click()
#         time.sleep(5)
#         self.assertIn("Gojo", driver.title)

#     def test_sign_out(self):
#         driver = self.driver
#         driver.find_element(By.LINK_TEXT, "Sign Out").click()
#         time.sleep(5)
#         self.assertIn("Gojo", driver.title)

#     def tearDown(self):
#         self.driver.close()

# if __name__ == '__main__':
#     unittest.main()



# # Open Chrome webdriver
# def open_browser():
#     driver = webdriver.Chrome(executable_path='./chromedriver')
#     return driver

# # Go to the website link
# def navigate_to_website(driver):
#     driver.get("https://gojo.herokuapp.com/")
#     time.sleep(10)

# # Login using username and password
# def login(driver):
#     driver.find_element(By.ID, "sign-in").click()
#     username = driver.find_element(By.ID, "username")
#     password = driver.find_element(By.ID, "password")
#     username.send_keys("check")
#     password.send_keys("check")
#     driver.find_element_by_xpath("//input[@value='Login']").click()
#     time.sleep(10)

# # Find the text 'About Me' in the navbar and click on it
# def go_to_about_me(driver):
#     driver.find_element(By.LINK_TEXT, "About Me").click()
#     time.sleep(10)

# # Find the text 'Home' in the navbar and click on it
# def go_to_home(driver):
#     driver.find_element(By.LINK_TEXT, "Home").click()
#     time.sleep(10)

# # Find the text 'Sign Out' in the navbar and click on it
# def sign_out(driver):
#     driver.find_element(By.LINK_TEXT, "Sign Out").click()
#     time.sleep(10)

# # Main function
# def main():
#     driver = open_browser()
#     navigate_to_website(driver)
#     login(driver)
#     go_to_about_me(driver)
#     go_to_home(driver)
#     sign_out(driver)

# if __name__ == "__main__":
#     main()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Firefox()

# driver.get("https://gojo.herokuapp.com/login")

# # link = driver.find_element_by_class_name("scrollto")
# # link.click()
# driver.maximize_window()
# driver.find_element_by_id("username").send_keys("abebe")
# driver.find_element_by_id("password").send_keys("abebe")
# driver.find_element_by_id("sign-in").click()

# try:
#     element = WebDriverWait(driver, 15).until(
#         EC.presence_of_all_elements_located((By.ID, "Sign-in"))
#     )
#     element.Click()
# except:
#     driver.quit()
