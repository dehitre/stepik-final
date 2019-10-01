from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        psw = self.browser.find_element(*LoginPageLocators.REG_PSW)
        psw_confirm = self.browser.find_element(*LoginPageLocators.REG_PSW_CONFIRM)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        email_field.send_keys(email)
        psw.send_keys(password)
        psw_confirm.send_keys(password)
        reg_button.click()


