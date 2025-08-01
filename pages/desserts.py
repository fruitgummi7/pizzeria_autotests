import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class Desserts(BasePage):
    """Локаторы"""

    right_slider = (By.XPATH, '(//span[@class="ui-slider-handle ui-state-default ui-corner-all"])[2]')
    apply_button = (By.XPATH, '//button[contains(text(), "Применить")]')
    add_cart_button = (By.XPATH, '(//a[contains(text(), "В корзину")])[2]')
    dessert = (By.XPATH, '//h1[@class="entry-title ak-container"]')

    """Actions"""

    def move_right_slider(self):
        slider = self.find(self.right_slider, EC.element_to_be_clickable)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, -200, 0).perform()
        time.sleep(2)
        print("Установка верхней границы цены")

    def click_apply_button(self):
        self.find(self.apply_button, EC.element_to_be_clickable).click()
        print('Клик по кнопке "Применить"')

    def click_add_cart(self):
        self.find(self.add_cart_button, EC.element_to_be_clickable).click()
        print('Клик по кнопке "В корзину"')

    """Methods"""

    def buy_dessert(self):
        with allure.step("Настройка фильтров поиска и добавление десерта в корзину"):
            self.move_right_slider()
            self.click_apply_button()
            self.click_add_cart()

    def check_dessert(self):
        with allure.step("Проверка перехода в раздел Десерты"):
            self.get_value(self.dessert, "ДЕСЕРТЫ")
