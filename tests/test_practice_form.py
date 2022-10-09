import allure
from allure_commons.types import Severity
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from demoqa.models.controls import datepicker
from demoqa.models.pages.automation_practice_form import *
from utils import attach


# browser.config.hold_browser_open = True

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Elena0808")
@allure.description("demoqa")
@allure.feature("Student Registration Form")
@allure.story("Проверка регистрации студента")
@allure.link("https://demoqa.com/automation-practice-form")
def test_practice_form():
    with allure.step('Открываем регистрационную форму студента'):
        open_page('https://demoqa.com', '/automation-practice-form')
    with allure.step('Заполняем персональные данные студента'):
        set_first_and_last_name('Тест', 'Тестов')
        set_email('test@test.test')
        set_gender('Female')
        set_user_number('8915999999')
        datepicker.select_date_of_bday()
    with allure.step('Заполняем дисциплину'):
        set_subject('Accounting', 'Economics')
    with allure.step('Заполняем хобби'):
        set_hobbies('Sports', 'Music')
    with allure.step('Заполняем адресные данные'):
        set_address('Россия, Москва')
        select_state('Haryana')
        select_city('Karnal')
    with allure.step('Добавляем фотографию'):
        set_photo('../files_for_test/test.png')
    with allure.step('Отправляем форму'):
        submit()
    with allure.step('Проверяем заполненную форму'):
        data_verification('Тест Тестов')
        data_verification('test@test.test')
        data_verification('Female')
        data_verification('8915999999')
        data_verification('08 August,1996')
        data_verification('Accounting, Economics')
        data_verification('Sports, Music')
        data_verification('test.png')
        data_verification('Россия, Москва')
        data_verification('Haryana Karnal')
