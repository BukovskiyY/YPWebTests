import pytest
from faker import Faker
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


@pytest.fixture
def password():
    faker = Faker()
    password = faker.password()
    return password
