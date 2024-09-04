import allure

import urls

from pages.base_page import BasePage
from locators.registration_locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Регистрации')
    def open_page_registration(self):
        self.open_url(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_REGISTRATION)

    @allure.step('Заполнить поле Имя')
    def input_name(self):
        name_input = self.wait_and_find_element(RegistrationPageLocators.REG_NAME)
        name_input.send_keys('Olga')

    @allure.step('Заполнить поле Email')
    def input_email(self):
        email_input = self.wait_and_find_element(RegistrationPageLocators.REG_EMAIL)
        email_input.send_keys('o.terekhova@ya')

    @allure.step('Заполнить поле Пароль')
    def input_password(self):
        password_input = self.wait_and_find_element(RegistrationPageLocators.REG_PASSWORD)
        password_input.send_keys('123456')

    @allure.step('Клик на кнопку Зарегистрироваться')
    def registration_button(self):
        registration_button = self.wait_and_find_element(RegistrationPageLocators.REG_BUTTON)
        registration_button.click()

    @allure.step('Регистрация нового пользователя')
    def create_new_user(self):
        self.open_page_registration()
        self.input_name()
        self.input_email()
        self.input_password()
        self.registration_button()



