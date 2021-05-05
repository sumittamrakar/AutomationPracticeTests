from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

class AccountPage():
    def __init__(self, driver):
        self.driver = driver

        self.signOut_button_selector = "a.logout"
        self.sign_in_navigation_selector = "a.login"

    def click_signOut(self):
        self.driver.find_element_by_css_selector(self.signOut_button_selector).click()

    def check_sign_in_exists(self):
        try:
            wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sign_in_navigation_selector)))
        except NoSuchElementException:
            return False
        return True