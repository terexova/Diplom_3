from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, ".//input[@name='name']")
    LOGIN_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_BUTTON_ENTRANCE = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_ENTRANCE = (By.XPATH, ".//h2[text() = 'Вход']")
    LOGIN_RECOVERY_PASSWORD = (By.XPATH, ".//a[text() = 'Восстановить пароль']")