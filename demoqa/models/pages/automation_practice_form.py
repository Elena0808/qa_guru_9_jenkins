import os

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss
from demoqa.models.controls import dropdown
from demoqa.models.controls.checkbox import select_checkbox
from demoqa.models.controls.radiobutton import select_radiobutton
from utils import path


def open_page(url, resourses):
    browser.open(url + resourses)
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_first_and_last_name(first_name, last_name):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)


def set_email(email):
    browser.element('#userEmail').type(email)


def set_gender(option):
    select_radiobutton('[for^=gender-radio]', option).first.click()


def set_user_number(user_number):
    browser.element('#userNumber').type(user_number)


def set_subject(subject_1, subject_2):
    browser.element('[id="subjectsInput"]').type(subject_1).press_enter() \
        .type(subject_2).press_enter()


def set_hobbies(option, option1):
    select_checkbox('[for^=hobbies-checkbox]', option).first.click()
    select_checkbox('[for^=hobbies-checkbox]', option1).first.click().perform(command.js.scroll_into_view)


def set_photo(photo):
    browser.element('[id="uploadPicture"]').send_keys(path.to_resource(photo))


def set_address(current_address):
    browser.element('[id="currentAddress"]').type(current_address)


def select_state(state):
    dropdown.select_data(browser.element('#state'), state)


def select_city(city):
    dropdown.select_data(browser.element('#city'), city)


def submit():
    browser.element('#submit').press_enter()


def data_verification(parameter_name):
    browser.element('.table-responsive').should(have.text(parameter_name))
