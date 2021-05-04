from selenium.common.exceptions import NoSuchElementException

class AccountPage():
    def __init__(self, driver):
        self.driver = driver

        self.signOut_button_selector = "a.logout"
        self.sign_in_navigation_selector = "a.login"

    def click_signOut(self):
        self.driver.find_element_by_css_selector(self.signOut_button_selector).click()

    def check_sign_in_exists(self):
        try:
            self.driver.find_element_by_css_selector(self.sign_in_navigation_selector)
        except NoSuchElementException:
            return False
        return True