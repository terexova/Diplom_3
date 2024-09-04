from selenium.webdriver.common.by import By


class OrderFeedLocators:
    LAST_ORDER = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    WINDOW_ORDER = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    NUMBER_ORDER = (By.XPATH, "//div[@id='root']/div/main/div/div")
    ALL_TIME_ORDER = (By.XPATH, ".//p[text() = 'Выполнено за все время:']/following-sibling::p")
    TODAY_ORDER = (By.XPATH, ".//p[text() = 'Выполнено за сегодня:']/following-sibling::p")
    NUMBER_ORDER_INFO = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(@class, "
                                   "'text_type_digits-large')]")
    NUMBER_ORDER_IS_WORKING = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")