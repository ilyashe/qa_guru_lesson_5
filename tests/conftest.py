import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def setting_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'  # вместо этой строки можно добавить другие опции
    browser.config.driver_options = driver_options
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()
