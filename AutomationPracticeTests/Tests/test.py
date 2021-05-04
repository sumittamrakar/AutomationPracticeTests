from selenium import webdriver
import time
import unittest
import re
from AutomationPracticeTests.Pages.authenticationPage import AuthenticationPage
from AutomationPracticeTests.Pages.homePage import HomePage 
from AutomationPracticeTests.Pages.accountPage import AccountPage
from AutomationPracticeTests.Pages.dressesPage import DressesPage
import xlrd
import json
from time import sleep

class AutomationPracticeTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new chrome session
        cls.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Various sign in tests using data-driven approach
    def test_authentication_invalid(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")

        home = HomePage(driver)
        home.click_sign_in()

        workbook = xlrd.open_workbook("AutomationPracticeTests/Data/data.xls")
        sheet = workbook.sheet_by_name("Sheet1")

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

    # Sign-out works
    def test_signout(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        accountPage = AccountPage(driver)

        accountPage.click_signOut()
        self.assertTrue(accountPage.check_sign_in_exists())

    # Search results match the search criteria
    def test_valid_search_results(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")

        home = HomePage(driver)
        search_text = "shirt"
        home.enter_search_text(search_text)
        home.click_search_button()

        result = home.validate_search_results(search_text)
        self.assertTrue(result)

    # List view and Grid view work as expected
    def test_list_view(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?id_category=8&controller=category")
        dresses_page = DressesPage(driver)
        dresses_page.click_list_view()

        view_local_storage = driver.execute_script("return localStorage.getItem('display')")

        self.assertEqual(json.loads(view_local_storage), "list")

    # List view and Grid view work as expected
    def test_grid_view(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?id_category=8&controller=category")
        dresses_page = DressesPage(driver)
        dresses_page.click_grid_view()

        view_local_storage = driver.execute_script("return localStorage.getItem('display')")

        self.assertEqual(json.loads(view_local_storage), "grid")
    
    # Website cookies work as expected
    def test_cookie_value_notEmpty(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        cookie = driver.get_cookie("PrestaShop-a30a9934ef476d11b6cc3c983616e364")
        cookie_value = cookie['value']

        self.assertNotEqual(cookie_value, None)

    #The basic cart functionality works. 
    #This is the ability to add and remove things from the cart and the correctness of the cart after various operations 
    def test_shopping_cart_add_multiple_products(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
    
        home = HomePage(driver)
        home.hover_over_tile()

        quantity = 5
        home.click_more()
        home.set_quantity(quantity)
        home.click_add_to_cart()

        sleep(1)

        driver.refresh()
        cart_quantity = int(home.get_cart_quantity())
        self.assertEqual(quantity, cart_quantity)

        home.remove_item_from_cart()

        sleep(1)

        self.assertTrue(home.is_shopping_cart_empty())

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()