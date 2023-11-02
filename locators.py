from selenium.webdriver.common.by import By


class MainPageLocators:
    # локаторы на главной странице
    PERSONAL_PAGE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кликабельный текст Личный Кабинет
    LOGIN_IN_ACC = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка Оформить заказ(после логина)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка Конструктор
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # кликабельное лого
    CREATE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")  # Текст соберите бургер
    BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']")  # кнопка булки
    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']")  # нопка соусы
    FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # кнопка начинки
    CONSTR_ACTIVE_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # активная кнопка конструктора


class LoginPageLocators:
    # локаторы на странице логина
    REGISTR_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # кликабельный текст регистрации
    EMAIL_FIELD = (By.XPATH, "//input[@name= 'name']")  # поле логин
    PASSWORD_FIELD = (By.XPATH, "//input[@name= 'Пароль']")  # поле пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    CURRENT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # кликабельный текст восстановления пароля
    LOGIN_TEXT = (By.XPATH, "//h2[text()='Вход']")  # надпись Вход


class RegPageLocators:
    # локаторы на странице регистрации
    NAME_FIELD = (By.XPATH, "(//input[@name= 'name'])[1]")  # поле Имя
    EMAIL_FIELD = (By.XPATH, "(//input[@name= 'name'])[2]")  # поле Email
    PASSWORD_FIELD = (By.XPATH, "//input[@name= 'Пароль']")  # поле Пароль
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")  # кликабельный текст "Войти" на форме регистрации
    PASS_INCORRECT_TEXT = (By.XPATH, "//p[text()='Некорректный пароль']")  # текст при пароле меньше 6 символов


class CurrentPassLocators:
    # локаторы на странице восстановить пароль
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")  # кнопка Войти


class ProfilePageLocators:
    # локаторы в личном кабинете (после авторизации)
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")  # кнопка Профиль в лк
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка Выход в лк
