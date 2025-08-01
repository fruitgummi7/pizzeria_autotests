import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class Checkout(BasePage):
    """Локаторы"""

    name = (By.XPATH, '//input[@id="billing_first_name"]')
    surname = (By.XPATH, '//input[@id="billing_last_name"]')
    street = (By.XPATH, '//input[@id="billing_address_1"]')
    city = (By.XPATH, '//input[@id="billing_city"]')
    state = (By.XPATH, '//input[@id="billing_state"]')
    postcode = (By.XPATH, '//input[@id="billing_postcode"]')
    phone = (By.XPATH, '//input[@id="billing_phone"]')
    payment = (By.XPATH, '//input[@id="payment_method_cod"]')
    agreement = (By.XPATH, '//input[@id="terms"]')
    order_date = (By.XPATH, '//input[@id="order_date"]')
    order_button = (By.XPATH, '//button[@id="place_order"]')

    """Actions"""

    def send_name(self):
        field = self.find(self.name, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Фирюза")
        print("Ввод имени")

    def send_surname(self):
        field = self.find(self.surname, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Османова")
        print("Ввод фамилии")

    def send_street(self):
        field = self.find(self.street, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Вишневского д.1")
        print("Ввод улицы")

    def send_city(self):
        field = self.find(self.city, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Казань")
        print("Ввод города")

    def send_state(self):
        field = self.find(self.state, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("республика Татарстан")
        print("Ввод области")

    def send_postcode(self):
        field = self.find(self.postcode, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("111111")
        print("Ввод индекса")

    def send_phone(self):
        field = self.find(self.phone, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("+77777777777")
        print("Ввод номера телефона")

    def click_payment(self):
        self.find(self.payment, EC.element_to_be_clickable).click()
        print("Выбор способа оплаты")

    def click_agreement(self):
        self.find(self.agreement, EC.element_to_be_clickable).click()
        print("Пользовательское соглашение")

    def click_order_button(self):
        self.find(self.order_button, EC.element_to_be_clickable).click()
        print('Клик по кнопке "Оформить заказ"')

    def send_order_date(self):
        field = self.find(self.order_date, EC.element_to_be_clickable)
        field.send_keys("11")
        field.send_keys("11")
        field.send_keys("2025")
        print("Ввод даты")

    """Methods"""

    def checkout(self):
        with allure.step("Оформление заказа, ввод данных"):
            self.send_name()
            self.send_surname()
            self.send_street()
            self.send_city()
            self.send_state()
            self.send_postcode()
            self.send_phone()
            self.click_payment()
            self.click_agreement()
            self.send_order_date()
            self.click_order_button()
