import allure


import urls
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Личный кабинет')
    def open_page_login(self):
        self.open_url(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_LOGIN)

    @allure.step('Открытие страницы Регистрации')
    def open_page_registration(self):
        self.open_url(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_REGISTRATION)

    @allure.step('Открытие страницы Личного кабинета')
    def open_page_personal_account(self):
        self.open_url(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_ACCOUNT)

    @allure.step('Открытие страницы Восстановление пароля')
    def open_page_recovery_password(self):
        self.open_url(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_FORGOT_PASSWORD)

    @allure.step('Заполнить поле Email')
    def input_email(self):
        email_input = self.wait_and_find_element(LoginPageLocators.LOGIN_EMAIL)
        email_input.send_keys('o.terekhova@ya.ru')

    @allure.step('Заполнить поле Пароль')
    def input_password(self):
        password_input = self.wait_and_find_element(LoginPageLocators.LOGIN_PASSWORD)
        password_input.send_keys('123456')

    @allure.step('Клик на кнопку Войти')
    def click_button_entrance(self):
        button_entrance = self.wait_and_find_element(LoginPageLocators.LOGIN_BUTTON_ENTRANCE)
        button_entrance.click()

    @allure.step('Клик на Восстановить пароль')
    def click_recovery_password(self):
        recovery_password = self.wait_and_find_element(LoginPageLocators.LOGIN_RECOVERY_PASSWORD)
        recovery_password.click()

    @allure.step('Авторизация пользователя')
    def log_in_user(self):
        self.open_page_login()
        self.input_email()
        self.input_password()
        self.click_button_entrance()


