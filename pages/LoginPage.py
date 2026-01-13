from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_EMAIL = (By.ID, 'field_email')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    # LOGIN_BY_QR_CODE = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    # RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    # REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    # VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    # MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    # YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    # OTHER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')
    ERROR_TEXT = (By.CSS_SELECTOR, "span[class*='LoginForm-module__error']")


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_EMAIL)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        # self.find_element(LoginPageLocators.LOGIN_BY_QR_CODE)
        # self.find_element(LoginPageLocators.RESTORE_LINK)
        # self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        # self.find_element(LoginPageLocators.VK_BUTTON)
        # self.find_element(LoginPageLocators.MAIL_BUTTON)
        # self.find_element(LoginPageLocators.YANDEX_BUTTON)
        # self.find_element(LoginPageLocators.OTHER_BUTTON)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return  self.find_element(LoginPageLocators.ERROR_TEXT).text

    def send_login(self, mail_login):
        self.find_element(LoginPageLocators.LOGIN_EMAIL).send_keys(mail_login)
