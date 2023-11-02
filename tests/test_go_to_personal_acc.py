from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, ProfilePageLocators


class TestStellarBurgersGoToPersonalProfile:

    def test_go_to_personal_profile(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*ProfilePageLocators.PROFILE_BUTTON).is_displayed()

