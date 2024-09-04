import allure

from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на последний заказ')
    def click_last_order(self):
        last_order = self.wait_and_find_element(OrderFeedLocators.LAST_ORDER)
        last_order.click()

    @allure.step('Получить окно с информацией по заказу')
    def get_window_with_order_details(self):
        return self.find_element(OrderFeedLocators.WINDOW_ORDER)

    @allure.step('Получить список всех заказов в ленте')
    def get_order(self):
        order = self.find_elements(OrderFeedLocators.NUMBER_ORDER)
        for order_list in order:
            order_text = order_list.text
            return order_text

    @allure.step('Получить количество заказов за все время')
    def get_counter_orders_all_time(self):
        return self.get_text_element(OrderFeedLocators.ALL_TIME_ORDER)

    @allure.step('Получить количество заказов за сегодня')
    def get_counter_orders_today(self):
        return self.get_text_element(OrderFeedLocators.TODAY_ORDER)

    @allure.step('Получить номер заказа при окне заказа')
    def get_number_order_text_window(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(OrderFeedLocators.NUMBER_ORDER_INFO).text != '9999')
        new_number = self.wait_and_find_element(OrderFeedLocators.NUMBER_ORDER_INFO)
        new_number_info = new_number.text
        return int(new_number_info)

    @allure.step('Получить номер заказа в разделе "В работе"')
    def get_number_order_text_is_working(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(OrderFeedLocators.NUMBER_ORDER_IS_WORKING).text != 'Все текущие заказы готовы!')
        new_number = self.wait_and_find_element(OrderFeedLocators.NUMBER_ORDER_IS_WORKING)
        new_number_is_working = new_number.text
        return int(new_number_is_working)
