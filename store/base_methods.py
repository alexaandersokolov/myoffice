import time
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def find(self, how, what, timeout=20):  # Открываем что-то, используя явное ожидание
        try:
            element = WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what)))
            return element
        except (TimeoutException, StaleElementReferenceException, ElementNotInteractableException):
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise Exception("Время ожидания вышло. Элемент на странице не найден или с ним нельзя взаимодействовать")


    def find2(self, how_what, err_msg=None):  # Открываем что-то, используя список из ассертов
        how, what = how_what
        try:
            return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((how, what)))
        except Exception as e:
            print(self.browser.current_url)
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            if err_msg:
                raise AssertionError(err_msg) from e
            else:
                raise


    def find_to_be_clickable(self, how, what, timeout=10):  # Открываем что-то, используя явное ожидание и проверяем, что элемент кликабелен
        try:
            element = WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable((how, what)))
            return element
        except Exception:
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise Exception('На элемент нельзя кликнуть')


    def is_element_present(self, how, what):  # Проверяем, что элемент находится на странице, использовать с ASSERT
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            return False
        return True


    def is_element_present1(self, how_what, err_msg=None):  # Проверяем, что элемент находится на странице
        how, what = how_what
        try:
            self.find(how, what)
        except NoSuchElementException as e:
            if err_msg is not None:
                raise AssertionError(err_msg) from e
            else:
                raise


    def find_all_elements(self, how, what): # Находим все элементы на странице, возвращает список (или пустой список)
            elements = self.browser.find_elements(how, what)
            if len(elements) == 0:
                allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
                raise Exception('Ни один элемент на странице не найден - вернулся пустой список!')
            return elements

    def move_find_to_be_clickable(self, how, what, timeout=10):  # Открываем что-то, используя явное ожидание и проверяем, что элемент кликабелен
        try:
            element = WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable((how, what)))
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            self.browser.execute_script("window.scrollBy({top: -150});")
            return element
        except Exception as error:
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise Exception(f'На элемент нельзя кликнуть, ошибка: {error}')

    def move_find_to_be_clickable_2(self, how, what, timeout=10):  # Открываем что-то, используя явное ожидание и проверяем, что элемент кликабелен НЕ прокручивая потом вверх
        try:
            element = WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable((how, what)))
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except Exception as error:
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise Exception(f'На элемент нельзя кликнуть, ошибка: {error}')

    # Открываем ссылку в браузере
    def open(self):
        self.browser.get(self.url)

    def clear_input_fill(self, input_fill): #стереть поле нажав на крестик
        self.find(*input_fill).click()

    def delete_input_fill(self, input): #стереть поле нажав 60 раз на клавишу BACKSPACE
        self.find(*input).send_keys('\ue003'*60)

    def should_be_no_results(self):
        assert self.is_element_present(*NoResults.NO_RESULTS), "No results is not present!"

    def click_to_checkbox(self, checkbox):
        self.find_to_be_clickable(*checkbox).click()

    # Метод для наведения курсора мышки на указанный элемент
    def hover_mouse(self, browser, element):
        action = ActionChains(browser)
        action.pause(1).move_to_element(element).perform()

    def hover_mouse_and_click(self, browser, element):
        action = ActionChains(browser)
        action.pause(1).move_to_element(element).click().perform()

    def hover_mouse_to_delete(self, browser, element):
        action = ActionChains(browser)
        action.pause(1).move_to_element(element).click().send_keys('\ue003'*80).send_keys('Город Москва, площадь Андроньевская, д. 4, стр. 1').perform()

    # Метод для логаута через интерфейс
    def logout_from_interface(self):
        self.find_to_be_clickable(*Lk.LOGOUT_MENU).click()
        self.find_to_be_clickable(*Lk.LOGOUT_BUTTON).click()
        time.sleep(3)

    def close_page(self):
        self.browser.close()

    def move_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")



