import allure
from core.BaseTest import browser, mail_login, password
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода и восстановления после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser, mail_login, password):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(mail_login)
    for _ in range(3):
        LoginPage.type_password(password)
        LoginPage.click_login()

    LoginPage.click_recovery()
