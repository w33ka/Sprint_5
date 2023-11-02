from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegPageLocators, MainPageLocators, LoginPageLocators


faker = Faker()


class TestStellarBurgersRegistration:

    def test_registration_success(self, driver):
        email = faker.email()
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTR_BUTTON).click()
        driver.find_element(*RegPageLocators.NAME_FIELD).send_keys('Vika')
        driver.find_element(*RegPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegPageLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*RegPageLocators.REG_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.REGISTR_BUTTON))
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))

        driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON).is_displayed()

    def test_registration_with_short_password_not_success(self, driver):
        email = faker.email()

        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTR_BUTTON).click()
        driver.find_element(*RegPageLocators.NAME_FIELD).send_keys('Vika')
        driver.find_element(*RegPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegPageLocators.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*RegPageLocators.REG_BUTTON).click()

        assert driver.find_element(*RegPageLocators.PASS_INCORRECT_TEXT).text == 'Некорректный пароль'
