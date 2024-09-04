import allure


from pages.base_page import BasePage
from urls import UrlStBurgers
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators

class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Stellar burgers')
    def open_page(self):
        self.open_url(UrlStBurgers.URL)

    @allure.step('Открытие страницы Лента Заказов')
    def open_page_order_feed(self):
        self.open_url(UrlStBurgers.URL + UrlStBurgers.URL_ORDER_FEED)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_personal_account(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT).click()

    @allure.step('Клик по кнопке Конструктор')
    def click_constructor(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Клик по кнопке Лента Заказов')
    def click_order_feed(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_ORDER_FEED).click()

    @allure.step('Клик по кнопке Начинки')
    def click_filling(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_FILLING).click()

    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.wait_and_find_element(MainPageLocators.INGREDIENT_BUN).click()

    @allure.step('Получить текст с окна деталей ингредиентов')
    def get_text_ingredient_details(self):
        return self.get_text_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Закрыть окно деталей ингредиентов по клику на крестик')
    def click_close_cross_details_ingredient(self):
        self.wait_and_find_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_CROSS).click()

    @allure.step('Получить текст с окна деталей ингредиентов')
    def get_text_filling_main_page(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_FILLING)
        return self.get_text_element(MainPageLocators.BUTTON_FILLING)

    @allure.step('Добавить ингредиент в Конструктор')
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(self.wait_and_find_element(MainPageLocators.INGREDIENT_BUN),
                           self.wait_and_find_element(MainPageLocators.CONSTRUCTOR))

    @allure.step('Добавить мясо в Конструктор')
    def add_ingredient_to_constructor_with_filling(self):
        self.drag_and_drop(self.wait_and_find_element(MainPageLocators.INGREDIENT_BUN),
                           self.wait_and_find_element(MainPageLocators.CONSTRUCTOR))
        self.click_filling()
        self.drag_and_drop(self.wait_and_find_element(MainPageLocators.INGREDIENT_MEAT),
                           self.wait_and_find_element(MainPageLocators.CONSTRUCTOR))

    @allure.step('Получить текст со счетчика ингредиентов')
    def get_text_counter_ingredient(self):
        return self.get_text_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создание заказа')
    def write_up_order(self):
        self.open_page()
        self.add_ingredient_to_constructor()
        write_up_order = self.wait_and_find_element(MainPageLocators.BUTTON_WRITE_UP_ORDER)
        write_up_order.click()

    @allure.step('Создание заказа c начинкой')
    def write_up_order_with_filling(self):
        self.open_page()
        self.add_ingredient_to_constructor_with_filling()
        write_up_order = self.wait_and_find_element(MainPageLocators.BUTTON_WRITE_UP_ORDER)
        write_up_order.click()
        return self.wait_and_find_element(OrderFeedLocators.NUMBER_ORDER_INFO)

    @allure.step('Получить текст с окна оформления заказа "Ваш заказ начали готовить"')
    def get_text_your_order_is_cooking(self):
        return self.get_text_element(MainPageLocators.YOUR_ORDER_IS_COOKING)
