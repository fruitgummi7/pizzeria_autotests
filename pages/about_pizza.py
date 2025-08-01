import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class AboutPizza(BasePage):
    """Локаторы"""

    choose_bort = (By.XPATH, '//select[@id="board_pack"]')
    add_cart_button = (By.XPATH, '//button[@name="add-to-cart"]')
    go_cart = (By.XPATH, '(//a[contains(text(), "Корзина")])[1]')
    descr = (By.XPATH, '//li[@id="tab-title-description"]')

    """Actions"""

    def click_cheese_bort(self):
        select = Select(self.find(self.choose_bort, EC.element_to_be_clickable))
        select.select_by_visible_text("Сырный - 55.00 р.")
        print("Выбран сырный борт")

    def click_add_cart_button(self):
        self.find(self.add_cart_button, EC.element_to_be_clickable).click()
        print("Пицца добавлена в корзину")

    def click_go_cart(self):
        self.find(self.go_cart, EC.element_to_be_clickable).click()
        print("Переход в корзину")

    """Methods"""

    def add_options_pizza(self):
        with allure.step("Просмотр информации о товаре и добавление опций"):
            self.click_cheese_bort()
            self.click_add_cart_button()

    def check_pizza_info(self):
        with allure.step("Проверка перехода к описанию пиццы"):
            self.get_value(self.descr, "ОПИСАНИЕ")
