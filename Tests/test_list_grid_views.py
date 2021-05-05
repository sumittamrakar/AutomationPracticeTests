import unittest
from selenium import webdriver
from Pages.homePage import HomePage
from Pages.dressesPage import DressesPage 
from Data.utilities import TestData
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

    def test_list_view(self):
        """
        Verify list view works as expected.
        """
        driver = self.driver

        home_page = HomePage(driver)
        home_page.click_dresses_tab()

        dresses_page = DressesPage(driver)
        dresses_page.click_list_view()

        view_local_storage = driver.execute_script("return localStorage.getItem('display')")

        self.assertEqual(json.loads(view_local_storage), "list")

    def test_grid_view(self):
        """
        Verify grid view works as expected.
        """
        driver = self.driver

        home_page = HomePage(driver)
        home_page.click_dresses_tab()
        dresses_page = DressesPage(driver)
        dresses_page.click_grid_view()

        view_local_storage = driver.execute_script("return localStorage.getItem('display')")

        self.assertEqual(json.loads(view_local_storage), "grid")

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()