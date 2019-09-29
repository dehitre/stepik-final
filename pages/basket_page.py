from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)


    def should_be_login_url(self):
        assert "basket" in self.browser.current_url

    def no_elements_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENTS)