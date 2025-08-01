from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        """Инициализация драйвера и ожидания"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator, condition=EC.presence_of_element_located):
        """Ожидание и возврат элемента по локатору"""
        return self.wait.until(condition(locator))

    def get_value(self, locator, word):
        """Получение значения локатора"""
        locator = self.wait.until(EC.visibility_of_element_located(locator))
        value_word = locator.text
        print(f"Полученное значение: '{value_word}'")
        assert value_word == word
        print(word, "Проверка пройдена успешно")

    def get_current_url(self, url):
        """Ожидание определённого URL и его проверка"""
        self.wait.until(lambda driver: driver.current_url == url)
        current_url = self.driver.current_url
        print(f"Текущий URL: '{current_url}'")
        assert current_url == url
        print(current_url, "Проверка пройдена")

    def promocode_assertion(self, locator, error_text):
        """Проверка, что промокод не был применён повторно"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text
        if actual_text == error_text:
            raise Exception("Промокод применён повторно — ошибка")

