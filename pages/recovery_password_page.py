import allure
import urls

from pages.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordPageLocators


class RecoveryPasswordPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Восстановление пароля')
    def open_page_recovery_password(self):
        self.open_url(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_FORGOT_PASSWORD)

    @allure.step('Заполнить поле Email')
    def input_email(self):
        self.click_element(RecoveryPasswordPageLocators.PLACEHOLDER_EMAIL)
        email_input = self.wait_and_find_element(RecoveryPasswordPageLocators.PLACEHOLDER_EMAIL)
        email_input.send_keys('o.terekhova@ya.ru')

    @allure.step('Заполнить поле Пароль')
    def input_password(self):
        self.click_element(RecoveryPasswordPageLocators.PLACEHOLDER_PASSWORD)
        password_input = self.wait_and_find_element(RecoveryPasswordPageLocators.PLACEHOLDER_PASSWORD)
        password_input.send_keys('123456')

    @allure.step('Клик на кнопку Восстановить')
    def click_button_recovery(self):
        button_recovery = self.wait_and_find_element(RecoveryPasswordPageLocators.BUTTON_RECOVERY)
        button_recovery.click()
        self.wait_and_find_element(RecoveryPasswordPageLocators.BUTTON_SAVE)

    @allure.step('Клик на значок видимости пароля')
    def click_sign_eye(self):
        sign_eye = self.wait_and_find_element(RecoveryPasswordPageLocators.SIGN_EYE)
        sign_eye.click()

    @allure.step('Проверяем, что поле Пароль стало активным')
    def check_password_field(self):
        if 'input_status_active' in self.wait_and_find_element(RecoveryPasswordPageLocators.FIELD_PASSWORD_NO_ACTIVE).get_attribute('class'):
            return True
        else:
            return False
