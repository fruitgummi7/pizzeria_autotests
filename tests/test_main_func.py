import allure
from pages.main_page import MainPage
from pages.about_pizza import AboutPizza
from pages.cart import Cart
from pages.desserts import Desserts
from pages.my_account import MyAccount
from pages.registration import Registration
from pages.checkout import Checkout


@allure.description("Добавление пиццы в корзину со слайдера")
def test_01(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Добавление пиццы в корзину"):
        main_p.add_cart_pizza1()
        main_p.go_to_cart()

    with allure.step("Проверка, что пицца добавлена в корзину"):
        cart_p = Cart(driver)
        cart_p.assertion_pizza()

@allure.description("Проверка работы слайдера")
def test_02(selenium):
    driver = selenium

    with allure.step("Проверка работы слайдера"):
        main_p = MainPage(driver)
        main_p.slider_test()


@allure.description("Просмотр информации о пицце")
def test_03(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Просмотр информации о пицце"):
        main_p.pizza_info()

    with allure.step("Проверка, что страница с информацией о пицце открыта"):
        about_pizza_p = AboutPizza(driver)
        about_pizza_p.check_pizza_info()


@allure.description("Добавление опций к пицце")
def test_04(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Просмотр информации о пицце"):
        main_p.pizza_info()

    with allure.step("Добавление опций к пицце"):
        about_pizza_p = AboutPizza(driver)
        about_pizza_p.add_options_pizza()

    with allure.step("Переход в корзину"):
        main_p.go_to_cart()

    with allure.step("Проверка отображения выбранной пиццы в корзине"):
        cart_p = Cart(driver)
        cart_p.assertion_pizza_2()

    with allure.step("Проверка, что сырный борт добавлен"):
        cart_p.assertion_cheese_bort()


@allure.description("Редактирование корзины")
def test_05(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Просмотр информации о пицце"):
        main_p.add_cart_pizza1()
        main_p.pizza_info()

    with allure.step("Добавление опций к пицце"):
        about_pizza_p = AboutPizza(driver)
        about_pizza_p.add_options_pizza()

    with allure.step("Переход в корзину"):
        main_p.go_to_cart()

    with allure.step("Редактирование товаров в корзине"):
        cart_p = Cart(driver)
        cart_p.edit_cart()


@allure.description("Переход в раздел десерты")
def test_06(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Добавление пиццы в корзину"):
        main_p.add_cart_pizza1()

    with allure.step("Переход в корзину"):
        main_p.go_to_cart()

    with allure.step("Переход на страницу с десертами"):
        main_p.go_to_dessert()

    with allure.step("Проверка перехода"):
        dessert_p = Desserts(driver)
        dessert_p.check_dessert()


@allure.description("Настройка фильтров в разделе десерты и добавление десерта в корзину")
def test_07(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Переход в раздел десерты"):
        main_p.go_to_dessert()

    with allure.step("Добавление десерта в корзину"):
        dessert_p = Desserts(driver)
        dessert_p.buy_dessert()

    with allure.step("Переход в корзину"):
        main_p.go_to_cart()

    with allure.step("Проверка, что десерт добавлен в корзину"):
        cart_p = Cart(driver)
        cart_p.assert_dessert()


@allure.description("Регистрация пользователя")
def test_08(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Переход в раздел мой аккаунт"):
        my_account_p = MyAccount(driver)
        my_account_p.my_account_reg()

    with allure.step("Регистрация пользователя"):
        registration_p = Registration(driver)
        registration_p.registration()


@allure.description("Авторизация зарегистрированного пользователя")
def test_09(selenium):
    driver = selenium

    with allure.step("Открытие главной страницы сайта"):
        main_p = MainPage(driver)
        main_p.go_site()

    with allure.step("Авторизация пользователя"):
        account_p = MyAccount(driver)
        account_p.go_my_account()
        account_p.authorization()


@allure.description("Авторизация с пустым полем Логин")
def test_10(selenium):
    driver = selenium

    my_account_p = MyAccount(driver)
    my_account_p.authorization_empty_login()


@allure.description("Авторизация с пустым полем Пароль")
def test_11(selenium):
    driver = selenium

    my_account_p = MyAccount(driver)
    my_account_p.authorization_empty_password()


@allure.description("Проверка восстановления пароля")
def test_12(selenium):
    driver = selenium

    my_account_p = MyAccount(driver)
    my_account_p.check_forget_password_link()


@allure.description("Регистрация с существующим email")
def test_13(selenium):
    driver = selenium

    registration_p = Registration(driver)
    registration_p.registration_exist_email()


@allure.description("Регистрация с пустым полем логин")
def test_14(selenium):
    driver = selenium

    registration_p = Registration(driver)
    registration_p.registration_without_login()


@allure.description("Регистрация с пустым полем пароль")
def test_15(selenium):
    driver = selenium

    registration_p = Registration(driver)
    registration_p.registration_without_password()


@allure.description("Выбор товара и оформление заказа")
def test_16(selenium):
    driver = selenium

    with allure.step("Выбор товара и переход к оформлению заказа"):
        main_p = MainPage(driver)
        main_p.select_pizza()
        main_p.order_product()

    with allure.step("Авторизация"):
        account_p = MyAccount(driver)
        account_p.go_my_account()
        account_p.authorization()

    with allure.step("Переход в корзину"):
        main_p.go_to_cart()

    with allure.step("Переход в корзину и к оформлению заказа"):
        cart = Cart(driver)
        cart.order()

    with allure.step("Оформление заказа"):
        checkout_p = Checkout(driver)
        checkout_p.checkout()