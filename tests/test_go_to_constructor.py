from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, ProfilePageLocators


class TestStellarBurgersGoToConstructor:

    def test_go_to_constructor_button_constructor(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_BURGER_TEXT))

        driver.find_element(*MainPageLocators.CREATE_BURGER_TEXT).is_displayed()

    def test_go_to_constructor_button_logo(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_BURGER_TEXT))

        driver.find_element(*MainPageLocators.CREATE_BURGER_TEXT).is_displayed()
