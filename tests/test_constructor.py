from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators


class TestStellarBurgersConstructor:
    def test_constructor_go_to_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_BURGER_TEXT))
        driver.find_element(*MainPageLocators.SAUCES_BUTTON).click()
        driver.find_element(*MainPageLocators.BUNS_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTR_ACTIVE_BUTTON).text == 'Булки'

    def test_constructor_go_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_BURGER_TEXT))
        driver.find_element(*MainPageLocators.SAUCES_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTR_ACTIVE_BUTTON).text == 'Соусы'

    def test_constructor_go_to_fillings(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_BURGER_TEXT))
        driver.find_element(*MainPageLocators.FILLINGS_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTR_ACTIVE_BUTTON).text == 'Начинки'
