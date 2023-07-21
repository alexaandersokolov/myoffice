import time
import allure
from store.base_methods import BasePage
from store.locator import MyofficePageLocators


class MyofficePage(BasePage):
    @allure.step('Работаем с поле поиск ')
    def button_accept(self):
        check_dict = {'Кнопка Принять (cookie)': self.is_element_present(*MyofficePageLocators.BUTTON_ACCEPT)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_ACCEPT).click()

    def button_split(self):
        self.move_find_to_be_clickable_2(*MyofficePageLocators.BUTTON_SPLIT_BISSNES)
        check_dict = {'Кнопка split для бизнеса': self.is_element_present(*MyofficePageLocators.BUTTON_SPLIT_BISSNES),
                      'Кнопка split для гос': self.is_element_present(*MyofficePageLocators.BUTTON_SPLIT_STATE)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_SPLIT_BISSNES).click()
        check_dict = {'Описание split для бизнеса': self.is_element_present(*MyofficePageLocators.DESCRIPTION_BISSNES)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_SPLIT_STATE).click()
        check_dict = {'Описание split для гос': self.is_element_present(*MyofficePageLocators.DESCRIPTION_STATE)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'

    def choose_platform(self):
        check_dict = {'Кнопка PC': self.is_element_present(*MyofficePageLocators.BUTTON_PC),
                      'Кнопка Mobile': self.is_element_present(*MyofficePageLocators.BUTTON_MOBILE),
                      'Кнопка Server': self.is_element_present(*MyofficePageLocators.BUTTON_SERVER)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_PC).click()
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_MOBILE).click()
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_SERVER).click()

    def button_buy(self):
        self.move_find_to_be_clickable(*MyofficePageLocators.BUTTON_BUY)
        check_dict = {'Кнопка купить': self.is_element_present(*MyofficePageLocators.BUTTON_BUY)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_BUY).click()

    def field_company_name(self):
        self.move_find_to_be_clickable(*MyofficePageLocators.FIELD_COMPANY_NAME)
        check_dict = {'Поле название компании': self.is_element_present(*MyofficePageLocators.FIELD_COMPANY_NAME)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.FIELD_COMPANY_NAME).send_keys('TEGRUS')

    def choose_region(self):
        self.move_find_to_be_clickable(*MyofficePageLocators.REGION)
        check_dict = {'Поле Регион': self.is_element_present(*MyofficePageLocators.REGION)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.REGION).click()
        self.find_to_be_clickable(*MyofficePageLocators.REGION_RUSSIA).click()

    def check_box(self):
        self.move_find_to_be_clickable(*MyofficePageLocators.CHECKBOX_PROFESSIONAL)
        check_dict = {'Чек-бокс Мой офис Профессиональный': self.is_element_present(*MyofficePageLocators.CHECKBOX_PROFESSIONAL)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.CHECKBOX_PROFESSIONAL).click()

    def search(self):
        self.move_find_to_be_clickable(*MyofficePageLocators.BUTTON_SEARCH)
        check_dict = {'Кнопка поиск': self.is_element_present(*MyofficePageLocators.BUTTON_SEARCH)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*MyofficePageLocators.BUTTON_SEARCH).click()