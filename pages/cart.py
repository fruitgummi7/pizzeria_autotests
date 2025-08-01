import time
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException


class Cart(BasePage):
    """Локаторы"""

    quantity_field = (By.XPATH, '(//input[@class="input-text qty text"])[1]')
    pizza_1 = (By.LINK_TEXT, 'Пицца "Как у бабушки"')
    pizza_2 = (By.LINK_TEXT, 'Пицца "Ветчина и грибы"')
    options = (By.XPATH, '//dd[@class="variation-"]')
    del_pizza = (By.XPATH, '(//a[@aria-label="Remove this item"])[2]')
    dessert = (By.LINK_TEXT, 'Десерт "Морковный каприз"')
    order_button = (By.XPATH, '//a[normalize-space(text())="ПЕРЕЙТИ К ОПЛАТЕ"]')
    promocode_field = (By.XPATH, '//input[@id="coupon_code"]')
    cupon_button = (By.XPATH, '//button[@name="apply_coupon"]')
    cupon_apply_right = (By.XPATH, '//div[@class="woocommerce-message"]')
    cupon_apply_wrong = (By.XPATH, '//ul[@class="woocommerce-error"]')

    """Actions"""

    def edit_quantity(self):
        field = self.find(self.quantity_field, EC.element_to_be_clickable)
        field.click()
        field.send_keys(Keys.BACKSPACE)
        field.send_keys("2")
        field.send_keys(Keys.RETURN)
        print("Количество пицц изменено")

    def remove_pizza(self):
        self.find(self.del_pizza, EC.element_to_be_clickable).click()
        print("Пицца удалена из заказа")

    def click_order_button(self):
        """Клик по кнопке 'Перейти к оплате'"""
        for _ in range(3):
            try:
                self.find(self.order_button, EC.element_to_be_clickable).click()
                break
            except StaleElementReferenceException:
                time.sleep(1)

    def send_promocode_field_right(self):
        self.find(self.promocode_field, EC.element_to_be_clickable).send_keys("GIVEMEHALYAVA")
        print("Ввод верного промокода")

    def send_promocode_field_wrong(self):
        self.find(self.promocode_field, EC.element_to_be_clickable).send_keys("DC120")
        print("Ввод ошибочного промокода")

    def click_cupon_button(self):
        self.find(self.cupon_button, EC.element_to_be_clickable).click()
        print("Клик по кнопке применить купон")

    """Methods"""

    def assert_dessert(self):
        with allure.step("Проверка, десерт добавлен в корзину"):
            self.get_value(self.dessert, 'Десерт "Морковный каприз"')

    def order(self):
        with allure.step("Перейти к оплате"):
            self.click_order_button()

    def apply_right_promo(self):
        with allure.step("Ввод верного промокода"):
            self.send_promocode_field_right()
            self.click_cupon_button()

    def apply_wrong_promo(self):
        with allure.step("Ввод ошибочного промокода"):
            self.send_promocode_field_wrong()
            self.click_cupon_button()

    def assert_cupon_right(self):
        with allure.step("Проверка применения верного промокода"):
            self.get_value(self.cupon_apply_right, "Coupon code applied successfully.")

    def assert_cupon_wrong(self):
        with allure.step("Проверка применения ошибочного промокода"):
            self.get_value(self.cupon_apply_wrong, "Неверный купон.")

    def promocode_assert(self):
        with allure.step("Проверка применения верного промокода"):
            self.promocode_assertion(self.cupon_apply_right, "Coupon code applied successfully.")

    def assertion_pizza(self):
        with allure.step("Проверка что пицца добавлена в корзину"):
            self.get_value(self.pizza_1, 'Пицца "Как у бабушки"')

    def assertion_pizza_2(self):
        with allure.step("Проверка что пицца добавлена в корзину"):
            self.get_value(self.pizza_2, 'Пицца "Ветчина и грибы"')

    def assertion_cheese_bort(self):
        with allure.step("Проверка, сырный борт добавлен"):
            self.get_value(self.options, "Сырный борт")

    def edit_cart(self):
        with allure.step("Изменение количества товаров и удаление товара из корзины"):
            self.get_value(self.pizza_1, 'Пицца "Как у бабушки"')
            self.get_value(self.pizza_2, 'Пицца "Ветчина и грибы"')
            self.edit_quantity()
            time.sleep(3)
            self.remove_pizza()
