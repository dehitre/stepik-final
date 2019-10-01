from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PSW = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PSW_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.XPATH,"//button[@name='registration_submit']")



class ProductPageLocators:
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # popup with The shellcoder's handbook has been added to your basket text
    POPUP_SUCCESS = (By.XPATH, '//div[@id="messages"]/div[1]')
    PRODUCT_ADDED = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    PRODUCT_TO_ADD = (By.CSS_SELECTOR, '.product_main>h1')

    # popup with Your basket now qualifies for the Deferred benefit offer offer
    POPUP_WITH_PRICE = (By.XPATH, '//div[contains(@class,"alert-info")]')
    ADDED_PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"alert-info")]/div/p/strong')
    ACTUAL_PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[1]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//div[contains(@class,'basket-mini')]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_ELEMENTS = (By.CSS_SELECTOR, ".basket-items")
