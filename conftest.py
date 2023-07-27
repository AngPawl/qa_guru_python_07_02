import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture
def determine_new_browser():
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    browser.config.driver_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})


@pytest.fixture
def set_window_size(determine_new_browser):
    browser.config.window_width = 1400
    browser.config.window_height = 2800


@pytest.fixture
def open_browser(set_window_size):
    browser.open()

    yield

    browser.quit()