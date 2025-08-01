from pages.main_page import MainPage
from pages.bonus_program import BonusProgram
import allure


@allure.description("Регистрация в бонусной системе")
def test_01(selenium):
    driver = selenium

    with allure.step("Переход в раздел бонусной программы"):
        main_p = MainPage(driver)
        main_p.go_bonus_programm()

    with allure.step("Регистрация в бонусной программе c проверкой"):
        bonus_program_p = BonusProgram(driver)
        bonus_program_p.get_bonus_card()