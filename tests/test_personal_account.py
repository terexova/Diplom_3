import allure

import urls
from conftest import driver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.registration_page import RegistrationPage


class TestPersonalAccount:

    @allure.title('Проверка: личный кабинет')
    @allure.description('Проверка перехода по клику Личный кабинет')
    def test_click_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_personal_account()
        assert main_page.get_current_url() == urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_LOGIN


    @allure.description('Проверка перехода в раздел История заказов')
    def test_click_history_orders(self, driver):
        reg_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        reg_page.create_new_user()
        login_page.log_in_user()
        main_page.click_personal_account()
        account_page.click_history_orders()
        assert account_page.get_current_url() == urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_HISTORY_ORDER

    @allure.description('Проверка выхода из Личного кабинета')
    def test_exit_personal_account(self, driver):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        login_page.log_in_user()
        main_page.click_personal_account()
        account_page.click_exit_personal_account()
        main_page.wait_url_to_be(urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_LOGIN)
        assert account_page.get_current_url() == urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_LOGIN
