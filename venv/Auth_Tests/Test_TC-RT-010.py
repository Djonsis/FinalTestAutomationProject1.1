import os
import pytest
from manager import my_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="class")
def browser():
    driver = my_driver
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def wait(self, browser):
     return WebDriverWait(browser, 10)

class TestAuthentication():

    # Тест-кейс для проверки связки Почта+Пароль (успешная)
    def test_successful_login_email(self, browser, wait):
        # Открываем страницу
        browser.get("https://b2c.passport.rt.ru")

        # Тестовая почта
        email = "почта@example.com"

        # Шаг 1: Ввод корректной почты
        email_input = browser.find_element(By.ID, "username")
        email_input.send_keys(email)

        # Проверяем, что введенная почта соответствует корректному формату электронной почты
        assert "@" in email_input.get_attribute("value"), "Некорректный формат почты"

    def test_successful_login_password(self, browser, wait):
        # Открываем страницу
        browser.get("https://b2c.passport.rt.ru")

        # Корректный пароль
        password = "Пароль"

        # Шаг 2: Ввод корректного пароля
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        # Проверяем, что введенный пароль соответствует заданным критериям безопасности
        assert len(password_input.get_attribute("value")) >= 8, "Пароль слишком короткий"

    def test_successful_login_button(self, browser, wait):
        # Открываем страницу
        browser.get("https://b2c.passport.rt.ru")

        # Тестовые данные (почта и пароль)
        email = "Почта@example.com"
        password = "Пароль"

        # Шаг 3: Нажатие кнопки "Войти"
        email_input = browser.find_element(By.ID, "kc-login")
        email_input.send_keys(email)

        password_input = browser.find_element(By.ID, "kc-login")
        password_input.send_keys(password)

        login_button = browser.find_element(By.ID, "kc-login")
        login_button.click()

        # Аутентификация клиента в системе - здесь можно добавить дополнительные проверки
        # Перенаправление клиента на страницу, указанную в redirect_uri
        assert "redirect_uri" in browser.current_url, "Перенаправление не выполнено"
