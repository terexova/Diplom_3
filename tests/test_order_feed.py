import allure

from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed import OrderFeedPage
from pages.account_page import AccountPage


class TestOrderFeed:

    @allure.title('Проверка раздела Лента заказов')
    @allure.description('При клике на заказ, открывается всплывающее окно с деталями')
    def test_open_window_with_order_details(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.log_in_user()
        main_page.click_personal_account()
        main_page.write_up_order()
        main_page.open_page_order_feed()
        order_feed_page.click_last_order()
        assert order_feed_page.get_window_with_order_details().is_displayed()

    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_order_displayed_on_order_feed(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)

        login_page.log_in_user()
        main_page.click_personal_account()
        main_page.write_up_order()
        main_page.open_page()
        main_page.click_personal_account()
        account_page.click_history_orders()
        number_last_order_account = account_page.get_number_last_order_account()
        main_page.click_order_feed()
        number_last_order_feed = order_feed_page.get_order()
        assert number_last_order_account in number_last_order_feed

    @allure.description('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_create_order_counter_all_time_increase(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.log_in_user()
        main_page.click_personal_account()
        main_page.write_up_order()
        main_page.open_page_order_feed()
        counter_order_1 = order_feed_page.get_counter_orders_all_time()
        main_page.write_up_order()
        main_page.open_page_order_feed()
        counter_order_2 = order_feed_page.get_counter_orders_all_time()
        assert counter_order_1 != counter_order_2

    @allure.description('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_create_order_counter_today_increase(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.log_in_user()
        main_page.click_personal_account()
        main_page.write_up_order()
        main_page.open_page_order_feed()
        counter_order_1 = order_feed_page.get_counter_orders_today()
        main_page.write_up_order()
        main_page.open_page_order_feed()
        counter_order_2 = order_feed_page.get_counter_orders_today()
        assert counter_order_1 != counter_order_2

    @allure.description('После оформления заказа его номер появляется в разделе "В работе"')
    def test_number_order_in_working(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.log_in_user()
        main_page.click_personal_account()
        main_page.write_up_order_with_filling()
        number_1 = order_feed_page.get_number_order_text_window()
        main_page.open_page_order_feed()
        number_2 = order_feed_page.get_number_order_text_is_working()
        assert number_1 == number_2

