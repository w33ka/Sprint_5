from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, ProfilePageLocators, LoginPageLocators


class TestStellarBurgersLogOut:
    def test_logout(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_TEXT))
        driver.find_element(*LoginPageLocators.LOGIN_TEXT).is_displayed()
