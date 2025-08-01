import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class Registration(BasePage):
    """Локаторы"""

    name_field = (By.XPATH, '//input[@id="reg_username"]')
    email_field = (By.XPATH, '//input[@id="reg_email"]')
    password_field = (By.XPATH, '//input[@id="reg_password"]')
    registration_button = (By.XPATH, '//button[@name="register"]')
    message = (By.XPATH, '//ul[@class="woocommerce-error"]/li')

    """Actions"""

    def send_name_field(self):
        self.find(self.name_field, EC.element_to_be_clickable).send_keys("firyuza")
        print("Ввод имени пользователя")

    def send_email_field(self):
        self.find(self.email_field, EC.element_to_be_clickable).send_keys("firyuza@mail.ru")
        print("Ввод email")

    def send_password_field(self):
        self.find(self.password_field, EC.element_to_be_clickable).send_keys("123456789")
        print("Ввод пароля")

    def click_registration_button(self):
        self.find(self.registration_button, EC.element_to_be_clickable).click()
        print('Кликнуть кнопку "Зарегистрироваться"')

    """Methods"""

    def registration(self):
        with allure.step("Регистрация"):
            self.send_name_field()
            self.send_email_field()
            self.send_password_field()
            self.click_registration_button()

    def registration_exist_email(self):
        with allure.step("Регистрация с существующим email"):
            self.driver.get("https://pizzeria.skillbox.cc/register/")
            self.send_name_field()
            self.send_email_field()
            self.send_password_field()
            self.click_registration_button()
            self.get_value(self.message,
                "Error: Учетная запись с такой почтой уже зарегистировавана. Пожалуйста авторизуйтесь.")

    def registration_without_login(self):
        with allure.step("Регистрация с пустым полем логин"):
            self.driver.get("https://pizzeria.skillbox.cc/register/")
            self.find(self.email_field, EC.element_to_be_clickable).send_keys("firyuza@l.ru")
            self.send_password_field()
            self.click_registration_button()
            self.get_value(self.message,
                "Error: Пожалуйста введите корректное имя пользователя.")

    def registration_without_password(self):
        with allure.step("Регистрация с пустым полем пароль"):
            self.driver.get("https://pizzeria.skillbox.cc/register/")
            self.find(self.name_field, EC.element_to_be_clickable).send_keys("firyuzaaa")
            self.find(self.email_field, EC.element_to_be_clickable).send_keys("firy@m.ru")
            self.click_registration_button()
            self.get_value(self.message,
                "Error: Введите пароль для регистрации.")
