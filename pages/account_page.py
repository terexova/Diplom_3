import allure


from pages.main_page import MainPage
from urls import UrlStBurgers
from locators.account_page_locators import AccountPageLocators


class AccountPage(MainPage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Личного кабинета')
    def open_page(self):
        self.open_url(UrlStBurgers.URL + UrlStBurgers.URL_ACCOUNT)

    @allure.step('Возвращение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Клик на История заказов')
    def click_history_orders(self):
        history_orders = self.wait_and_find_element(AccountPageLocators.ACCOUNT_HISTORY_ORDERS)
        history_orders.click()

    @allure.step('Клик на Выход из Личного кабинета')
    def click_exit_personal_account(self):
        exit_personal_account = self.wait_and_find_element(AccountPageLocators.ACCOUNT_BUTTON_EXIT)
        exit_personal_account.click()

    @allure.step('Получить номер последнего заказа из Личного кабинета')
    def get_number_last_order_account(self):
        return self.get_text_element(AccountPageLocators.ACCOUNT_LAST_ORDER)
