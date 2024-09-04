from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators:
    PLACEHOLDER_EMAIL = (By.NAME, "name")
    PLACEHOLDER_PASSWORD = (By.NAME, 'Введите новый пароль')
    BUTTON_RECOVERY = (By.XPATH, ".//button[text() = 'Восстановить']")
    BUTTON_SAVE = (By.XPATH, ".//button[text() = 'Сохранить']")
    SIGN_EYE = (By.XPATH, ".//div[contains(@class, 'icon-action')]")
    FIELD_PASSWORD_NO_ACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div')
