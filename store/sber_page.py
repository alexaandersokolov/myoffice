import time
import allure
from store.base_methods import BasePage
from store.locator import SberPageLocators


class SberPage(BasePage):
    @allure.step('Работаем с поле поиск ')
    def field_search(self):
        check_dict = {'Поле поиск': self.is_element_present(*SberPageLocators.FIELD_SEARCH)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*SberPageLocators.FIELD_SEARCH).send_keys('QA')
        self.find_to_be_clickable(*SberPageLocators.BUTTON_SEARCH).click()

    @allure.step('Работаем с поле регион и населённый пункт')
    def field_city(self):
        self.find_to_be_clickable(*SberPageLocators.FIELD_CITY).send_keys('Москва')
        self.find_to_be_clickable(*SberPageLocators.MOSCOW).click()
        check_dict = {'Поле поиск': self.is_element_present(*SberPageLocators.FIELD_SEARCH_PROFFESION),
                      'Поле город': self.is_element_present(*SberPageLocators.FIELD_CITY),
                      'Кнопка сбросить': self.is_element_present(*SberPageLocators.RESET)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'

    @allure.step('Работаем с чек-боксом "доступно для людей с инвалидностью"')
    def for_invalids(self):
        self.find_to_be_clickable(*SberPageLocators.CHECKBOX_FOR_INVALIDS).click()
        check_dict = {'Поле поиск': self.is_element_present(*SberPageLocators.FIELD_SEARCH_PROFFESION),
                      'Поле город': self.is_element_present(*SberPageLocators.FIELD_CITY),
                      'Кнопка сбросить': self.is_element_present(*SberPageLocators.RESET)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*SberPageLocators.CHECKBOX_FOR_INVALIDS).click()

    @allure.step('Переходим в раздел Карьерные медиа')
    def career_media(self):
        self.find_to_be_clickable(*SberPageLocators.BUTTON_CAREER_MEDIA).click()
        check_dict = {'Bootstrap вперед': self.is_element_present(*SberPageLocators.BOOTSTRAP_FORWARD),
                      'Bootstrap назад': self.is_element_present(*SberPageLocators.BOOTSTRAP_BACK),
                      'Кнопка подробнее': self.is_element_present(*SberPageLocators.BUTTON_LEARN_MORE)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'

    @allure.step('Нажимаем кнопку "Подробнее"')
    def learn_more(self):
        self.find_to_be_clickable(*SberPageLocators.BUTTON_LEARN_MORE).click()

    @allure.step('Проверяем Bootstrap')
    def bootstrap(self):
        check_dict = {'Bootstrap вперед': self.is_element_present(*SberPageLocators.BOOTSTRAP_FORWARD),
                      'Bootstrap назад': self.is_element_present(*SberPageLocators.BOOTSTRAP_BACK),
                      'Кнопка подробнее': self.is_element_present(*SberPageLocators.BUTTON_LEARN_MORE)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*SberPageLocators.BOOTSTRAP_FORWARD).click()
        time.sleep(2)
        self.find_to_be_clickable(*SberPageLocators.BOOTSTRAP_BACK).click()

    @allure.step('Работа с "Фильтр"')
    def filter(self):
        # self.find_to_be_clickable(*SberPageLocators.BUTTON_CLOSE).click()
        self.move_find_to_be_clickable_2(*SberPageLocators.BUTTON_FILTER)
        self.find_to_be_clickable(*SberPageLocators.BUTTON_FILTER).click()
        check_dict = {'Кнопка сбросит все': self.is_element_present(*SberPageLocators.BUTTON_RESET_ALL)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*SberPageLocators.CHECKBOX_PODCAST).click()
        self.find_to_be_clickable(*SberPageLocators.CHECKBOX_CAREER).click()
        check_dict = {'Результат фильтра': self.is_element_present(*SberPageLocators.ABOUT_CAREER)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
        self.find_to_be_clickable(*SberPageLocators.BUTTON_RESET_ALL).click()

    @allure.step('Переходим в раздел "Студентам & выпускникам"')
    def graduate_students(self):
        self.move_find_to_be_clickable_2(*SberPageLocators.BUTTON_GRADUATE_STUDENTS)
        self.find_to_be_clickable(*SberPageLocators.BUTTON_GRADUATE_STUDENTS).click()
        check_dict = {'Кнопка подробнее': self.is_element_present(*SberPageLocators.BUTTON_LEARN_MORE_STUDENTS)}
        for key, value in check_dict.items():
            assert value, f'В интерфейсе отсутствует элемент: "{key}"'
