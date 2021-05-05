import unittest
from selenium import webdriver
from Pages.authenticationPage import AuthenticationPage
from Pages.homePage import HomePage
from Pages.accountPage import AccountPage 
from Data.utilities import TestData

class SignOutTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a new chrome session
        cls.driver = webdriver.Chrome(executable_path=TestData.DRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def setUp(self):
        driver = self.driver
        driver.get(TestData.URL)

    # Test to verify that the Sign-out works
    def test_sign_out(self):
        """
        Verify user is signed out when clicking sign out.
        """
        driver = self.driver

        # Sign in using valid credentials
        home = HomePage(driver)
        home.click_sign_in()
        authentication = AuthenticationPage(driver)
        authentication.enter_emailAdress(TestData.VALID_USERNAME)
        authentication.enter_password(TestData.VALID_PASSWORD)
        authentication.click_signIn()
        
        # Sign out and verify sign in button appears
        accountPage = AccountPage(driver)
        accountPage.click_signOut()

        self.assertTrue(accountPage.check_sign_in_exists())

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()