from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.tile_selector = "img[title='Blouse']"
        self.search_box_id = "search_query_top"
        self.search_button_name = "submit_search"
        self.searched_titles = "//*[@id='center_column']/ul/li/div/div[2]/h5/a"
        self.proceed_to_checkout = "//span[contains(text(), 'Proceed to checkout')]"
        self.cart_quantity_selector = ".ajax_cart_quantity"
        self.more_view_selector = "a.product-name[title='Blouse']"
        self.input_quantity_id = "quantity_wanted"
        self.add_to_cart_button_id = "add_to_cart"
        self.sign_in_button_selector = "a.login"

        self.shopping_cart_block_selector = "a[title='View my shopping cart']"
        self.remove_icon_selector = "a.ajax_cart_block_remove_link"
        self.shopping_cart_empty_label_selector = ".ajax_cart_no_product"
        self.dresses_tab_xpath= "//div[@id='block_top_menu']/ul/li/a[@title='Dresses']"

    def is_shopping_cart_empty(self):
        is_empty = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.shopping_cart_empty_label_selector))).is_displayed()
        return is_empty

    def remove_item_from_cart(self):
        cart_summary = self.driver.find_element_by_css_selector(self.shopping_cart_block_selector)
        hover = ActionChains(self.driver).move_to_element(cart_summary)
        hover.perform()

        wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.remove_icon_selector))).click()

    def click_dresses_tab(self):
        self.driver.find_element_by_xpath(self.dresses_tab_xpath).click()

    def click_more(self):
        self.driver.find_element_by_css_selector(self.more_view_selector).click()

    def set_quantity(self, quantity):
        self.driver.find_element_by_id(self.input_quantity_id).clear()
        self.driver.find_element_by_id(self.input_quantity_id).send_keys(quantity)

    def click_add_to_cart(self):
        self.driver.find_element_by_id(self.add_to_cart_button_id).click()
        self.driver.find_element_by_xpath(self.proceed_to_checkout).click()

    def get_cart_quantity(self):
        count = self.driver.find_element_by_css_selector(self.cart_quantity_selector).text
        return count

    def hover_over_tile(self):
        tile = self.driver.find_element_by_css_selector(self.tile_selector)
        hover = ActionChains(self.driver).move_to_element(tile)
        hover.perform()

    def enter_search_text(self, search_text):
        self.driver.find_element_by_id(self.search_box_id).clear()
        self.driver.find_element_by_id(self.search_box_id).send_keys(search_text)

    def click_search_button(self):
        self.driver.find_element_by_name(self.search_button_name).click()

    def click_sign_in(self):
        self.driver.find_element_by_css_selector(self.sign_in_button_selector).click()

    def validate_search_results(self, search_text ):
        listSearchText = self.driver.find_elements_by_xpath(self.searched_titles)
        
        # Obtain all the search result items 
        converted_list = [x.text.lower() for x in listSearchText]
        
        # Check if the all the search result items contain the search text 
        isPresent = all(search_text.lower() in s for s in converted_list)

        return isPresent
            