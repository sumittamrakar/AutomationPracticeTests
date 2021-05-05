import unittest
from selenium import webdriver
from Pages.homePage import HomePage 
from Data.utilities import TestData

class SignInTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a new chrome session
        cls.driver = webdriver.Chrome(executable_path=TestData.DRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_cookies_value_not_Empty(self):
        """
            Verify website cookies have a value.
        """
        driver = self.driver
        driver.get(TestData.URL)

        cookie = driver.get_cookie("PrestaShop-a30a9934ef476d11b6cc3c983616e364")
        cookie_value = cookie['value']

        self.assertNotEqual(cookie_value, None)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()