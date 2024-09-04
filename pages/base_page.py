import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Найти элементы')
    def find_elements(self, args):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(args))
        return self.driver.find_elements(*args)

    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.wait_and_find_element(locator).click()

    @allure.step('Возвращение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получить текст элемента')
    def get_text_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).text

    @allure.step('Передать текст в элемент')
    def put_text_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step('Переместить элемент')
    def drag_and_drop(self, element, target):
        return AC(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Ожидание определенной страницы')
    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))