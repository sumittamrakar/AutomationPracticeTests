import unittest
from selenium import webdriver
from Pages.homePage import HomePage
from Data.utilities import TestData

class SearchResultsTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a new chrome session
        cls.driver = webdriver.Chrome(executable_path=TestData.DRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def setUp(self):
        driver = self.driver
        driver.get(TestData.URL)

    def test_search_results(self):
        """
        Verify all the search results contain the search text.
        """
        driver = self.driver

        home = HomePage(driver)
        search_text = "shirt"
        home.enter_search_text(search_text)
        home.click_search_button()

        result = home.validate_search_results(search_text)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()