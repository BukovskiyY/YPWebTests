import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_EMAIL = (By.ID, 'field_email')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_BUTTON =  (By.XPATH, '//button[.//span[text()="Войти"]]')
    LOGIN_BY_QR_CODE = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    RESTORE_LINK = (By.XPATH, '//*[contains(@href, "anonymRecoveryStart")]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.CSS_SELECTOR, "span[class*='LoginForm-module__error']")
    GO_BACK_BUTTON = (By.XPATH, '//button[.//span[text()="Отмена"]]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_EMAIL)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_CODE)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return  self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле логин')
    def type_login(self, mail_login):
        self.find_element(LoginPageLocators.LOGIN_EMAIL).send_keys(mail_login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def type_password(self, password):
        self.find_element(LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_LINK).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
