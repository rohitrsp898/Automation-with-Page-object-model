from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.verficationErrors = []
        self.driver.maximize_window()

    
    def test_01_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage=HomePage(self.driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)
        print("Test_01 Completed")

    def test_02_login_invalid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(self.driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = login.check_invalid_username_message()
        # message = self.driver.find_element_by_xpath("//*[@id='spanMessage']").text
        self.assertEqual(message, "Invalid credentials")
        print("Test_02 Completed")


    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
        


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/roprajap/Desktop/Py_unittest_POM/Sample_unittest/Reports'))









