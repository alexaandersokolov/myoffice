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