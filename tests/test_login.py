from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, CurrentPassLocators, RegPageLocators


class TestStellarBurgersLogIn:

    def test_login_from_main_page(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_IN_ACC).click()
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('VikaAnaneva1999@gmail.com')
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON).is_displayed()

    def test_login_from_personal_acc_page(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('VikaAnaneva1999@gmail.com')
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON).is_displayed()

    def test_login_from_registration_page(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTR_BUTTON).click()
        driver.find_element(*RegPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('VikaAnaneva1999@gmail.com')
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON).is_displayed()

    def test_login_from_password_recovery_page(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_IN_ACC).click()
        driver.find_element(*LoginPageLocators.CURRENT_PASSWORD).click()
        driver.find_element(*CurrentPassLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('VikaAnaneva1999@gmail.com')
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON).is_displayed()


