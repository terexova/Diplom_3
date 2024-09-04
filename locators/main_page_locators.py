from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUTTON_ORDER_FEED = (By.XPATH, ".//p[text() = 'Лента Заказов']")
    BUTTON_FILLING = (By.XPATH, ".//span[text() = 'Начинки']")

    INGREDIENT_BUN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']/preceding-sibling::div/p")
    INGREDIENT_MEAT = (By.XPATH, ".//img[@alt = 'Мясо бессмертных моллюсков Protostomia']/preceding-sibling::div/p")
    CONSTRUCTOR = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    INGREDIENT_COUNTER = (By.XPATH, "//*[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, 'counter__num')]")

    INGREDIENT_DETAILS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    INGREDIENT_DETAILS_CLOSE_CROSS = X_CLOSE_ING = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    BUTTON_WRITE_UP_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    YOUR_ORDER_IS_COOKING = (By.XPATH, ".//p[text() = 'Ваш заказ начали готовить']")
