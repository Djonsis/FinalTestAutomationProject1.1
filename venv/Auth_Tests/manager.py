import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_chromedriver_path():
    # Установить путь к драйверу Chrome
    webdriver_path = ChromeDriverManager().install()

    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome()

    # Разворачиваем браузер на весь экран
    driver.maximize_window()

    # Создаем экземпляр драйвера Chrome и возвращаем его
    return driver

# Использование функции для получения экземпляра драйвера
my_driver = get_chromedriver_path()
