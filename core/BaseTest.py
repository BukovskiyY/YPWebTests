from faker import Faker
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def mail_login():
    faker = Faker()
    login = faker.email()
    return login
