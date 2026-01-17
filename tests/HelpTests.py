import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinet import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite("Проверка скролла на странице помощи")
@allure.title("Проверка открытия страницы 'Рекламный кабинет' после скролла")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
