from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_info_popups(self):
        self.should_be_name_popup()
        self.should_be_correct_product_name()
        self.should_be_price_popup()
        self.should_be_correct_price()

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        button.click()

    def should_be_name_popup(self):
        assert self.is_element_present(*ProductPageLocators.POPUP_SUCCESS)

    def should_be_correct_product_name(self):
        product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED)
        product_to_add = self.browser.find_element(*ProductPageLocators.PRODUCT_TO_ADD)
        assert self.is_text_of_two_elem_similar(product_added,product_to_add)

    def should_be_price_popup(self):
        assert self.is_element_present(*ProductPageLocators.POPUP_WITH_PRICE)

    def should_be_correct_price(self):
        product_added = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        product_to_add = self.browser.find_element(*ProductPageLocators.ACTUAL_PRODUCT_PRICE)
        assert self.is_text_of_two_elem_similar(product_added, product_to_add)



