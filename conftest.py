import os
import pytest
import requests
import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options


@pytest.fixture(scope="module")
def context():
    """Фикстура-контейнер для передачи данных из теста в тест.
    В качестве контейнера используется словарь."""

    return {}


@pytest.fixture(autouse=True, scope="function")
def time_start_finish():
    """Фикстура для вывода времени начала, окончания теста и его длительности.
    Применяется автоматичекски к каждому тесту"""

    start_time = dt.datetime.now()
    print(f'\nТест начался: {start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')
    yield
    finish_time = dt.datetime.now()
    print(f'\nТест закончился: {finish_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')
    delta_time = finish_time - start_time
    print(f'\nТест длился: {str(delta_time)[:-3]}')


#  Добавляем параметр запуска тестов в командной строке
def pytest_addoption(parser):
    # Для запуска тестов на удаленном сервере значение default="chrome"
    # Для запуска тестов на локальной машине значение default="chrome_local"
    parser.addoption('--browser_name', action='store', default="chrome_local", help="Choose browser: chrome or firefox")
    parser.addoption("--website", action="store", default="myoffice")
    # default="rabota"


@pytest.fixture
def get_chrome_options():
    """Фикстура для формирования опций браузера"""

    options = Chrome_Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=800,600')
    options.add_argument('--disable-gpu')
    options.add_extension(os.path.join(os.path.dirname(__file__), 'extension_1_2_8_0.crx'))
    return options


@pytest.fixture
def website(pytestconfig):
    """Фикстура для передачи URL в тесты для запуска"""
    website = pytestconfig.getoption("website")
    return f'https://{website}.ru/products/mail/'
    # return f'http://{website}.sber.ru/'


@pytest.fixture
def browser(request, get_chrome_options):
    """Фикстура для создания объекта драйвер с опциями для каждого теста (удаленного или локального запуска Chrome)
    В конце каждого теста получаем значение SID из localstorage браузера и делаем logout, закрываем сессию"""

    browser_name = request.config.getoption("browser_name")  # Получаем параметр командной строки browser_name
    remote_driver = "http://10.0.20.22:4444/wd/hub"
    options = get_chrome_options
    if browser_name == "chrome":
        print("\nstart Сhrome remote browser for test..")
        browser = webdriver.Remote(command_executor=remote_driver, options=options)
    elif browser_name == "chrome_local":
        print("\nstart Chrome_local browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise Exception("В функции pytest_addoption --browser_name указан неверный браузер")
    yield browser
    try:
        localstorage = browser.execute_script("return window.localStorage;")
    finally:
        browser.quit()
