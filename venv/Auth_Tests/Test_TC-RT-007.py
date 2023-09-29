import os
import pytest
from manager import my_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestAuthentication():

    @pytest.fixture(scope="class")
    def browser():
        driver = my_driver
        yield driver
        driver.quit()

    @pytest.fixture(scope="function")
    def wait(self, browser):
        return WebDriverWait(browser, 10)

    @pytest.mark.run(order=1)
    def test_open_page(self, browser, wait):
        # Открываем страницу
        browser.get("https://b2c.passport.rt.ru")
        assert "RT.RU Passport" in browser.title

    @pytest.mark.run(order=2)
    def test_select_phone_tab(self, browser, wait):
        # Выбираем таб "Телефон" в меню выбора типа аутентификации.
        phone_tab = browser.find_element(By.ID, "t-btn-tab-phone")
        phone_tab.click()
        assert "Телефон" in browser.page_source

    @pytest.mark.run(order=3)
    def test_enter_phone_number(self, browser, wait):
        # Пользователь вводит корректный номер телефона в поле ввода.
        phone_input = browser.find_element(By.ID, "username")
        phone_input.send_keys("+7 999 123-45-67")

    @pytest.mark.run(order=4)
    def test_enter_password(self, browser, wait):
        # Пользователь вводит корректный пароль в соответствующее поле
        password_input = browser.find_element(By.ID, "password-input")
        password_input.send_keys("your_password_here")  # Заменить на корректный пароль
