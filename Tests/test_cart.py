from selenium import webdriver
import unittest
from Pages.homePage import HomePage 
from Data.utilities import TestData
from time import sleep

class ShoppingCartTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new chrome session
        cls.driver = webdriver.Chrome(executable_path=TestData.DRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        driver = self.driver
        driver.get(TestData.URL)

    def test_add_to_shopping_cart(self):
        """
        Verify products added to the cart have correct quantity.
        """
        driver = self.driver
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