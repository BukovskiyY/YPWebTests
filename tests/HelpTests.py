import allure

from core.BaseTest import browser
from pages.AdvertisementCabinet import AdvertisementCabinetHelper
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocators

BASE_URL = 'https://ok.ru/help'


@allure.suite("Проверка скролла на странице помощи")
@allure.title("Проверка открытия страницы 'Рекламный кабинет' после скролла")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelper(browser)
