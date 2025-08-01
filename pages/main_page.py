import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class MainPage(BasePage):
    """Локаторы"""
    url = "https://pizzeria.skillbox.cc/"
    pizza_descr = (By.XPATH, '(//div[@class="item-img"])[8]')
    pizza1_hover = (By.XPATH, '(//div[@class="item-img"])[6]')
    pizza2_hover = (By.XPATH, '(//div[@class="item-img"])[7]')
    pizza1_add_cart = (By.XPATH, '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[6]')
    pizza2_add_cart = (By.XPATH, '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[7]')
    left_slider = (By.XPATH, '//a[@class="slick-prev"]')
    right_slider = (By.XPATH, '//a[@class="slick-next"]')
    go_cart = (By.XPATH, '(//a[contains(text(), "Корзина")])[1]')
    menu = (By.XPATH, '//li[@id="menu-item-389"]')
    dessert = (By.XPATH, '//li[@id="menu-item-391"]')
    order = (By.XPATH, '//li[@id="menu-item-31"]')
    bonus_programm = (By.XPATH, '//li[@id="menu-item-363"]')

    """Actions"""

    def click_pizza_descr(self):
        self.find(self.pizza_descr, EC.element_to_be_clickable).click()
        print("Получение информации о пицце")

    def add_cart_pizza1(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.pizza1_hover)).perform()
        time.sleep(1)
        self.find(self.pizza1_add_cart).click()
        time.sleep(1)
        print("Добавление в корзину первой пиццы")

    def add_cart_pizza2(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.pizza2_hover)).perform()
        time.sleep(1)
        self.find(self.pizza2_add_cart).click()
        print("Добавление в корзину второй пиццы")

    def click_left_slider(self):
        self.find(self.left_slider).click()
        print("Перемещение слайдера влево")

    def click_right_slider(self):
        self.find(self.right_slider).click()
        print("Перемещение слайдера вправо")

    def click_go_cart(self):
        # self.find(self.go_cart).click()
        # print("Переход в корзину")
        for _ in range(3):
            try:
                self.find(self.go_cart, EC.element_to_be_clickable).click()
                break
            except StaleElementReferenceException:
                time.sleep(1)

    def click_menu(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.menu)).perform()
        time.sleep(1)
        self.find(self.dessert).click()
        print("Переход в раздел десерты")

    def click_order(self):
        self.find(self.order).click()
        print('Клик по кнопке "Оформление заказа"')

    def click_bonus_programm(self):
        self.find(self.bonus_programm).click()
        print('Клик по кнопке "Бонусная программа"')

    """Methods"""

    def select_pizza(self):
        with allure.step("Выбор пиццы"):
            self.driver.get(self.url)
            self.add_cart_pizza1()
            time.sleep(1)

    def order_product(self):
        with allure.step("Переход на страницу оформления заказа"):
            self.click_order()

    def go_bonus_programm(self):
        with allure.step("Переход на страницу бонусной программы"):
            self.driver.get(self.url)
            self.click_bonus_programm()
            time.sleep(1)

    def go_site(self):
        with allure.step("Переход на сайт"):
            self.driver.get(self.url)

    def add_pizza(self):
        with allure.step("Добавление пиццы в корзину"):
            self.add_cart_pizza1()

    def go_to_cart(self):
        with allure.step("Переход в корзину"):
            self.click_go_cart()
            time.sleep(1)

    def slider_test(self):
        with allure.step("Прокрутка слайдера влево и вправо"):
            self.driver.get(self.url)
            self.add_cart_pizza1()
            self.click_right_slider()
            time.sleep(1)
            self.click_left_slider()

    def pizza_info(self):
        with allure.step("Получение информации о пицце"):
            self.click_pizza_descr()

    def go_to_dessert(self):
        with allure.step("Переход в раздел десерты"):
            self.click_menu()
