from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_HISTORY_ORDERS = (By.XPATH, ".//a[text() = 'История заказов']")
    ACCOUNT_BUTTON_EXIT = (By.XPATH, ".//button[text() = 'Выход']")
    ACCOUNT_LAST_ORDER = By.XPATH, ".//ul[contains(@class, 'OrderHistory_list__')]/li[last()]//p[contains(@class, 'digits')]"

