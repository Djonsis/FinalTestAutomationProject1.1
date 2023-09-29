import os
import pytest
from manager import my_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestAuthentication(unittest.TestCase):

    @pytest.fixture(scope="class")
    def browser():
        driver = my_driver
        yield driver
        driver.quit()

    @pytest.fixture(scope="function")
    def wait(self, browser):
        return WebDriverWait(browser, 10)

    def test_step_1_open_authentication_page(self, browser, wait):
        # Шаг 1: Открыть страницу авторизации
        wait.until(EC.url_to_be("https://b2c.passport.rt.ru"))
        # Проверка: Перенаправление на страницу авторизации
        self.assertEqual(browser.current_url, "https://b2c.passport.rt.ru")

    def test_step_2_select_phone_tab(self, browser, wait):
        # Шаг 2: Выбрать таб "Телефон" в меню выбора типа аутентификации
        phone_tab = self.driver.find_element(By.ID, "t-btn-tab-phone")
        phone_tab.click()

    def test_step_3_check_phone_form_displayed(self, browser, wait):
        # Шаг 3: Проверить, что форма ввода "Телефон" отображается
        phone_form = self.driver.find_element(By.ID, "t-btn-tab-phone")
        self.assertTrue(phone_form.is_displayed())

    def test_step_4_check_other_forms_disabled(self, browser, wait):
        # Шаг 4: Проверить, что остальные формы ввода не активны
        email_form = self.driver.find_element(By.ID, "t-btn-tab-ls")
        self.assertFalse(email_form.is_enabled())
