import unittest
from selenium import webdriver
import re
from Pages.authenticationPage import AuthenticationPage
from Pages.homePage import HomePage 
from Data.utilities import TestData
import xlrd
import json

class SignInTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a new chrome session
        cls.driver = webdriver.Chrome(executable_path=TestData.DRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def setUp(self):
        driver = self.driver
        driver.get(TestData.URL)

    # Test various sign in scenarios using data-driven approach
    def test_sign_in_scenarios(self):
        """
        1. Verify empty email and empty password displays correct error.
        2. Verify valid email and empty password displays correct error.
        3. Verify invalid email and valid password displays correct error.
        4. Verify unregistered email and valid password displays correct error.
        5. Verify valid email and invalid password displays correct error.
        6. Verify valid email and valid password displays welcome message.
        """
        driver = self.driver

        home = HomePage(driver)
        home.click_sign_in()

        workbook = xlrd.open_workbook(TestData.DATA_LOCATION)
        sheet = workbook.sheet_by_name(TestData.SHEET_NAME)

        authentication = AuthenticationPage(driver) 
        rowCount = sheet.nrows

        # Run all cases for sign in
        for row in range(2, rowCount): 
            username = sheet.cell_value(row, 1)
            password = sheet.cell_value(row, 2)
            expectedResult = sheet.cell_value(row, 3)
            authentication.enter_emailAdress(username)
            authentication.enter_password(password)

            authentication.click_signIn()

            pageSource = driver.page_source
            search_text = re.search(expectedResult, pageSource)
            self.assertNotEqual(search_text, None)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()