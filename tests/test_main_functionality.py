import allure
import urls

from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на "Конструктор"')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_order_feed()
        main_page.click_constructor()
        assert main_page.get_current_url() == urls.UrlStBurgers.URL

    @allure.description('Переход по клику на "Лента Заказов"')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_order_feed()
        assert main_page.get_current_url() == urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_ORDER_FEED


    @allure.description('При клике на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_show_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_ingredient()
        assert main_page.get_text_ingredient_details() == 'Детали ингредиента'

    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_details_close_on_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_ingredient()
        main_page.click_close_cross_details_ingredient()
        assert main_page.get_text_filling_main_page() == 'Начинки'

    @allure.description('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.add_ingredient_to_constructor()
        assert main_page.get_text_counter_ingredient() == '2'

    @allure.description('Авторизованный пользователь может оформить заказ')
    def test_log_in_user_write_up_order(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        login_page.log_in_user()
        main_page.click_personal_account()
        main_page.write_up_order()
        assert main_page.get_text_your_order_is_cooking() == 'Ваш заказ начали готовить'

