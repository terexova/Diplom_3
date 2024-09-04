from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REG_NAME = (By.XPATH, ".//input[@name='name']")
    REG_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    REG_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    REG_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

