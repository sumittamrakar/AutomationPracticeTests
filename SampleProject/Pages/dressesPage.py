class DressesPage:

    def __init__(self, driver):
        self.driver = driver

        self.view_list_id = "list"
        self.view_grid_id = "grid"

    def click_list_view (self):
        self.driver.find_element_by_id(self.view_list_id).click();

    def click_grid_view (self):
        self.driver.find_element_by_id(self.view_grid_id).click();
