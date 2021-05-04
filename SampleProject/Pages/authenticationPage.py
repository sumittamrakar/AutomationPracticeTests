class AuthenticationPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_address_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.sign_in_button_id = "SubmitLogin"

    def enter_emailAdress (self, emailAddress):
        self.driver.find_element_by_id(self.email_address_textbox_id).clear()
        self.driver.find_element_by_id(self.email_address_textbox_id).send_keys(emailAddress)

    def enter_password (self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_signIn (self):
        self.driver.find_element_by_id(self.sign_in_button_id).click()