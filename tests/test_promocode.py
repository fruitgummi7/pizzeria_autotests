import time
from pages.main_page import MainPage
from pages.cart import Cart
from pages.my_account import MyAccount
from pages.checkout import Checkout
import allure
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.description("Проверка применения верного промокода")
def test_01(selenium):
    driver = selenium

    with allure.step("Выбор пиццы и переход в корзину"):
        main_p = MainPage(driver)
        main_p.select_pizza()
        main_p.go_to_cart()

    with allure.step("Применение промокода"):
        cart_p = Cart(driver)
        cart_p.apply_right_promo()

    with allure.step("Проверка"):
        cart_p.assert_cupon_right()


@allure.description("Проверка применения ошибочного промокода")
def test_02(selenium):
    driver = selenium

    with allure.step("Выбор пиццы и переход в корзину"):
        main_p = MainPage(driver)
        main_p.select_pizza()
        main_p.go_to_cart()

    with allure.step("Применение промокода"):
        cart_p = Cart(driver)
        cart_p.apply_wrong_promo()

    with allure.step("Проверка"):
        cart_p.assert_cupon_wrong()



def intercept_request(request):
    if "wc-ajax=apply_coupon" in request.url:
        request.abort()  # Отклоняем запрос, имитируя сбой сервера

@allure.description("Проверка применения промокода при сбоях сервера")
def test_03():
    options = {
        'disable_encoding': True,
        'request_interceptor': intercept_request
    }

    driver = webdriver.Chrome(seleniumwire_options=options)
    wait = WebDriverWait(driver, 10)

    try:
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")

        with allure.step("Добавление пиццы в корзину"):
            add_button = wait.until(EC.presence_of_element_located((
                By.XPATH,
                '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[6]'
            )))
            time.sleep(1)
            add_button.click()
            time.sleep(1)

        with allure.step("Переход в корзину"):
            cart_link = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                '(//a[contains(text(), "Корзина")])[1]'
            )))
            cart_link.click()

        with allure.step("Ввод промокода"):
            promo_field = wait.until(EC.presence_of_element_located((
                By.ID, "coupon_code"
            )))
            promo_field.send_keys("GIVEMEHALYAVA")

        with allure.step("Применение промокода (с имитацией сбоя сервера)"):
            driver.request_interceptor = intercept_request
            apply_button = wait.until(EC.element_to_be_clickable((
                By.NAME, "apply_coupon"
            )))
            apply_button.click()
            time.sleep(3)

    finally:
        driver.quit()



@allure.description("Проверка повторного применения промокода")
def test_04(selenium):
    driver = selenium

    with allure.step("Добавление пиццы в корзину и переход на страницу оформления заказа"):
        main_p = MainPage(driver)
        main_p.select_pizza()
        main_p.order_product()

    with allure.step("Переход в раздел мой аккаунт"):
        account_p = MyAccount(driver)
        account_p.go_my_account()

    with allure.step("Авторизация пользователя"):
        account_p.authorization()

    with allure.step("Переход в корзину"):
        main_p.go_to_cart()

    with allure.step("Применение промокода"):
        cart_p = Cart(driver)
        time.sleep(1)
        cart_p.apply_right_promo()

    with allure.step("Оформить заказ"):
        cart_p.order()

    with allure.step("Оформление заказа"):
        checkout_p = Checkout(driver)
        checkout_p.checkout()
        time.sleep(5)

    with allure.step("Повторный выбор пиццы"):
        main_p = MainPage(driver)
        main_p.select_pizza()
        main_p.go_to_cart()

    with allure.step("Повторное применение промокода"):
        cart_p.apply_right_promo()
        cart_p.promocode_assert()