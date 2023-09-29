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

    def test_step_1_open_auth_page(self, browser, wait):
        # Шаг 1: Открыть страницу авторизации
        browser.get("https://b2c.passport.rt.ru")

        # Ожидаем, что произойдет перенаправление на страницу авторизации
        assert "Авторизация" in browser.title

    def test_step_2_select_phone_tab(self, browser, wait):
        # Шаг 2: Выбрать таб "Телефон" в меню выбора типа аутентификации
        browser.get("https://b2c.passport.rt.ru")
        phone_tab = self.browser.find_element(By.ID, "t-btn-tab-phone")
        phone_tab.click()

        # Ожидаем, что форма отображается корректно
        assert phone_tab.is_selected()

    def test_step_3_enter_phone_number(self, browser, wait):
        # Шаг 3: Клиент вводит номер телефона
        browser.get("https://b2c.passport.rt.ru")
        phone_input = browser.find_element(By.ID, "username")
        phone_input.send_keys("+7 999 123-45-67")

        # Ожидаем, что форма принимает формат ввода в виде "+7 999 123-45-67"
        assert phone_input.get_attribute("value") == "+7 999 123-45-67"
