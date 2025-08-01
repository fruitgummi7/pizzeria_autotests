import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class BonusProgram(BasePage):
    """Локаторы"""

    name_field = (By.XPATH, '//input[@id="bonus_username"]')
    phone_field = (By.XPATH, '//input[@id="bonus_phone"]')
    apply_card_button = (By.XPATH, '//button[@name="bonus"]')
    apply_card = (By.XPATH, '//h3[contains(text(), "Ваша карта оформлена!")]')

    """Actions"""

    def send_name_field(self, name):
        self.find(self.name_field, EC.element_to_be_clickable).send_keys(name)
        print("Ввод имени")

    def send_phone_field(self, phone):
        self.find(self.phone_field, EC.element_to_be_clickable).send_keys(phone)
        print("Ввод номера телефона")

    def click_apply_card_button(self):
        self.find(self.apply_card_button, EC.element_to_be_clickable).click()
        print('Клик по кнопке "Оформить карту"')

    """Methods"""

    def get_bonus_card(self):
        with allure.step("Регистрация в бонусной программе"):
            self.send_name_field("Фирюза")
            self.send_phone_field("+71223437455")
            self.click_apply_card_button()
            time.sleep(1)
            self.driver.switch_to.alert.accept()
            self.get_value(self.apply_card, "Ваша карта оформлена!")
