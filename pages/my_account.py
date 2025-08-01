import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class MyAccount(BasePage):
    """Локаторы"""

    account_button = (By.XPATH, '//li[@id="menu-item-30"]')
    registration_button = (By.XPATH, '//button[@class="custom-register-button"]')
    name_field = (By.XPATH, '//input[@id="username"]')
    password_field = (By.XPATH, '//input[@id="password"]')
    auth_button = (By.XPATH, '//button[@name="login"]')
    field_error = (By.XPATH, '//ul[@class="woocommerce-error"]/li')
    forget_password = (By.LINK_TEXT, "Забыли пароль?")
    reset_password_field = (By.XPATH, '//input[@name="user_login"]')
    reset_button = (By.XPATH, '//button[@value="Reset password"]')
    message = (By.XPATH, '//div[@class="woocommerce-message"]')

    """Actions"""

    def click_account_button(self):
        self.find(self.account_button, EC.element_to_be_clickable).click()
        print('Переход в раздел "Мой аккаунт"')

    def click_registration_button(self):
        self.find(self.registration_button, EC.element_to_be_clickable).click()
        print('Переход на страницу "Регистрация"')

    def send_name_field(self):
        self.find(self.name_field, EC.element_to_be_clickable).send_keys("firyuza")
        print("Введено имя пользователя")

    def send_password_field(self):
        self.find(self.password_field, EC.element_to_be_clickable).send_keys("123456789")
        print("Введен пароль")

    def click_auth_button(self):
        self.find(self.auth_button, EC.element_to_be_clickable).click()
        print("Клик по кнопке авторизации")

    def click_forget_password(self):
        self.find(self.forget_password, EC.element_to_be_clickable).click()
        print("Клик по кнопке восстановления пароля")

    def send_reset_password(self):
        self.find(self.reset_password_field, EC.element_to_be_clickable).send_keys("firyuza")
        print("Введен логин для сброса пароля")

    def click_reset_button(self):
        self.find(self.reset_button, EC.element_to_be_clickable).click()
        print("Клик по кнопке Сброс пароля")

    """Methods"""

    def my_account_reg(self):
        with allure.step('Переход на вкладку "Мой аккаунт" с последующей регистрацией'):
            self.click_account_button()
            self.click_registration_button()

    def go_my_account(self):
        with allure.step("Переход на вкладку Мой аккаунт"):
            self.click_account_button()

    def authorization(self):
        with allure.step("Авторизация"):
            self.send_name_field()
            self.send_password_field()
            self.click_auth_button()

    def authorization_empty_login(self):
        with allure.step("Авторизация c пустым полем логин"):
            self.driver.get("https://pizzeria.skillbox.cc/my-account/")
            self.send_password_field()
            self.click_auth_button()
            self.get_value(self.field_error, "Error: Имя пользователя обязательно.")

    def authorization_empty_password(self):
        with allure.step("Авторизация c пустым полем пароль"):
            self.driver.get("https://pizzeria.skillbox.cc/my-account/")
            self.send_name_field()
            self.click_auth_button()
            self.get_value(self.field_error, "Пароль обязателен.")

    def check_forget_password_link(self):
        with allure.step("Восстановление забытого пароля"):
            self.driver.get("https://pizzeria.skillbox.cc/my-account/")
            self.click_forget_password()
            time.sleep(2)
            self.send_reset_password()
            self.click_reset_button()
            self.get_value(self.message, "Password reset email has been sent.")
