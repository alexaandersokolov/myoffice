import time
import allure
from store.myoffice_page import MyofficePage


@allure.title("Сценарий 1.1.1 Пользователь работает с лендингом mail")
@allure.feature('Приложение myoffice/mail')
def test_scenario_1_1_1_sber(browser, website):
    """
    1) Пользователь открывает приложение https://myoffice.ru/products/mail/
    2) Нажимает кнопку "Принять пользовательское соглашение" - cookie
    3) Нажимает кнопку-split для бизнеса
    4) Нажимает кнопку-split для гос. организаций
    5) Нажимает на кнопку Приложения для ПК и веб-браузеров
    6) Нажимает на кнопку Мобильные приложения
    7) Нажимает на кнопку Серверные системы
    8) Нажимает на кнопку Купить
    9) Вводит в поле компания "TEGRUS"
    10) Выбирает регион
    11) Ставит чек-бокс
    12) Нажимает кнопку поиск
    """

    myoffice = MyofficePage(browser, website)  # myoffice - экземпляр класса MyofficePage
    myoffice.open()
    myoffice.button_accept()
    myoffice.button_split()
    myoffice.choose_platform()
    myoffice.button_buy()
    myoffice.field_company_name()
    myoffice.choose_region()
    myoffice.check_box()
    myoffice.search()
    time.sleep(5)