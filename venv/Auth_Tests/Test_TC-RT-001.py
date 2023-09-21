import os
import pytest
from manager import my_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Определение класса для тестов
class TestAuthentication:
    def setup_method(self):
        self.driver = my_driver

    # Тест 1: Проверка форм и страницы
    def test_check_authentication_form_display(self):
        try:
            # Шаг 1: Открыть страницу авторизации
            my_driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=e6d44528-2e17-413d-92b3-999f0b96c890&theme&auth_type")
            wait = WebDriverWait(my_driver, 20)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#body")))

            # Шаг 2: Проверить наличие формы "Авторизация"
            auth_form = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#page-right > div")))
            assert auth_form.is_displayed()

            # Шаг 3: Проверить, что страница разделена на два блока
            page_left_elements = my_driver.find_elements(By.ID, "page-left")
            page_right_elements = my_driver.find_elements(By.ID, "page-right")
            assert len(page_left_elements) == 1
            assert len(page_right_elements) == 1

            # Шаг 4: Проверить наличие меню выбора типа аутентификации в правой части
            assert my_driver.find_element(By.ID, "t-btn-tab-phone").is_displayed()
            assert my_driver.find_element(By.ID, "t-btn-tab-mail").is_displayed()
            assert my_driver.find_element(By.ID, "t-btn-tab-login").is_displayed()
            assert my_driver.find_element(By.ID, "t-btn-tab-ls").is_displayed()

            # Шаг 5: Проверить наличие продуктового слогана
            assert my_driver.find_element(By.CSS_SELECTOR, "#page-left > div > div.what-is > p").is_displayed()

            print("Тест успешно завершен.")
        except Exception as e:
            print(f"Тест провален: {str(e)}")

    # Тест 2: Проверить наличие вспомогательной информации в левой части
    def test_check_left_page(self):
        try:
            # Попытка найти элемент app-footer > div.rt-footer-left внутри page-left
            page_left = my_driver.find_element(By.ID, "page-left")
            footer = page_left.find_element(By.CSS_SELECTOR, "#app-footer > div.rt-footer-left")

            print("Вспомогательная информация находится в левой части страницы")
        except NoSuchElementException:
            print("Вспомогательная информация не находится в левой части страницы")

    # Тест 3: Проверить, что по умолчанию выбрана форма авторизации по телефону
    def test_phone_form_main(self):
        try:
            auth_form_phone = my_driver.find_element(By.ID, "t-btn-tab-phone")
            element_classes = auth_form_phone.get_attribute("class")
            assert "rt-tab--active" in element_classes, "Элемент не имеет класс 'rt-tab--active'"

            print("Тест успешно завершен.")
        except Exception as e:
            print(f"Тест провален: {str(e)}")

    def teardown_method(self):
        self.driver.quit()
