import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import MainPageLocators, LoginPageLocators


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome()
    options.add_argument("--windows-size=1200,600")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get('https://stellarburgers.nomoreparties.site')

    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*MainPageLocators.LOGIN_IN_ACC).click()
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('VikaAnaneva1999@gmail.com')
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123456')
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    return driver
