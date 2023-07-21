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

    # Логинимся под Иванов Петр Анатольевич АО "ЭЛЕКТРОННЫЙ ПАСПОРТ"
    # Логин GTZXCLJAL Пароль 123456789Abc++
    def login_to_petrov(self):
        self.browser.find_element(By.CSS_SELECTOR, '[href="#/auth/csp"]').click()
        self.browser.find_element(By.XPATH, '//div[@id="CertificateItem"]/div/div[text()="Иванов Петр Анатольевич"]').click()
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()
        self.browser.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys("123456789Abc+++")
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Логинимся под Кудряшов Сергей Юрьевич ООО "ТЕСТ"
        # Логин ZDCBGKXVU Пароль Knopka123456!!!
    def login_to_kudryashov(self):
        self.browser.find_element(By.CSS_SELECTOR, '[href="#/auth/csp"]').click()
        self.browser.find_element(By.XPATH, '//div[@id="CertificateItem"]/div/div[text()="ООО ТЕСТ"]').click()
        self.browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]').click()
        self.browser.find_element(By.XPATH, '//*[@id="username"]').click()
        self.browser.find_element(By.CSS_SELECTOR, 'ul li[aria-label="ZDCBGKXVU"]').click()
        self.browser.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys("Knopka123456!!!!")
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Логинимся под АО "Альфа-Банк"
    # Логин RHBCZPEMG Пароль 12345678Abc++
    def login_to_alpha(self):
        self.browser.find_element(By.CSS_SELECTOR, '[href="#/auth/csp"]').click()
        self.browser.find_element(By.XPATH, '//div[@id="CertificateItem"]/div/div[contains(., "АЛЬФА-БАНК")]').click()
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()
        self.browser.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys("12345678Abc++")
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def login_with_gosuslugi(self, login, password):
        self.find_to_be_clickable(By.CSS_SELECTOR, '[href="#/auth/person"]').click()
        self.find_to_be_clickable(By.CSS_SELECTOR, '.p-checkbox-box').click()
        self.find_to_be_clickable(By.CSS_SELECTOR, 'button[type="button"]').click()
        new_window = self.browser.window_handles[1]     # ID новой открывшейся вкладки
        self.browser.switch_to.window(new_window)       # Переключаем Selenium на новую открывшуюся вкладку
        self.find_to_be_clickable(By.ID, 'login').send_keys(login)
        self.find_to_be_clickable(By.ID, 'password').send_keys(password)
        self.find_to_be_clickable(By.XPATH, "//button[@class='plain-button plain-button_wide']").click()
        self.browser.switch_to.window(self.browser.window_handles[0]) # Переключаем Selenium на первоначальную вкладку

    def login_with_gosuslugi_real(self, login, password):
        self.find_to_be_clickable(By.CSS_SELECTOR, '[href="#/auth/person"]').click()
        self.find_to_be_clickable(By.CSS_SELECTOR, '.p-checkbox-box').click()
        self.find_to_be_clickable(By.CSS_SELECTOR, 'button[type="button"]').click()
        new_window = self.browser.window_handles[1]     # ID новой открывшейся вкладки
        self.browser.switch_to.window(new_window)       # Переключаем Selenium на новую открывшуюся вкладку
        self.find_to_be_clickable(By.ID, 'login').send_keys(login)
        self.find_to_be_clickable(By.ID, 'password').send_keys(password)
        self.find_to_be_clickable(By.XPATH, '//button[text()=" Войти "]').click()
        self.browser.switch_to.window(self.browser.window_handles[0]) # Переключаем Selenium на первоначальную вкладку

    def get_anonymous_sid(self):
        time.sleep(2)
        localstorage = self.browser.execute_script("return window.localStorage;")
        return localstorage.get('anonymousSid')

    def should_be_my_page(self):  # Модули, которые должны отображаться в личном кабинете
        self.should_be_oib()
        self.should_be_nsi()
        self.should_be_viw()

    def should_be_my_page_after_gosuslugi(self):
        self.find_to_be_clickable(By.CSS_SELECTOR, 'a[href="#/"]')
        self.find_to_be_clickable(By.CSS_SELECTOR, 'a[href="#/profile"]')
        self.find_to_be_clickable(By.CSS_SELECTOR, 'a[href="/cos/"]')
        self.find_to_be_clickable(By.CSS_SELECTOR, 'a[href="/sbkts/"]')

    def should_be_cos_page(self):
        self.find_to_be_clickable(By.CSS_SELECTOR, 'a[href="#/request"]')
        time.sleep(3)

    def should_be_dkp(self):
        assert self.is_element_present(*OibPageLocators.DKP), "dkp is not present!!!"

    def should_be_oib(self):
        assert self.is_element_present(*LoginPageLocators.OIB), "oib is not present!!!"

    def should_be_nsi(self):
        assert self.is_element_present(*LoginPageLocators.NSI), "nsi is not present!!!"

    def should_be_viw(self):
        assert self.is_element_present(*LoginPageLocators.VIW), "viw is not present!!!"

    def go_to_oib(self):  # Переход в модуль Управления доступом
        oib = self.find(*LoginPageLocators.OIB)
        oib.click()
        # Ожидаем пока таблица с пользователями загрузится полностью
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(OibPageLocators.USERS_TABLE))

    def go_to_nsi(self):  # Переход в модуль Справочники
        companies = self.browser.find_element(*LoginPageLocators.NSI)
        companies.click()

    def go_to_viw(self):  # Переход в модуль осмотра
        view = self.browser.find_element(*LoginPageLocators.VIW)
        view.click()

    def go_to_ff(self):  # Переход в модуль Учет баллов
        ff = self.browser.find_element(*LoginPageLocators.FF)
        ff.click()
        assert self.find(*FfPageLocators.CANVAS), 'Diagramm is not present'   # Проверяем диаграмму и дожидаемся ее загрузки

    def go_to_cos(self):  # Переход в модуль Договор купли-продажи
        cos = self.browser.find_element(*LoginPageLocators.COS)
        cos.click()

    def go_to_sbkts(self):  # Переход в модуль ЭСБКТС
        sbkts = self.browser.find_element(*LoginPageLocators.SBKTS)
        sbkts.click()

    def go_to_ep(self):  # Переход в модуль Электронный паспорт
        ep = self.browser.find_element(*LoginPageLocators.EP)
        ep.click()

    def go_to_requests(self):
        self.find_to_be_clickable(*OibPageLocators.REQUESTS).click()

    def go_to_my_organization(self):  # Переход во вкладку Организация в личном кабинете пользователя
        self.find_to_be_clickable(*LoginPageLocators.MY_ORGANIZATION).click()

    def should_be_my_organization(self):
        assert self.is_element_present(*LoginPageLocators.MY_ORGANIZATION), 'Organization is not present!!!'

    def go_to_user_in_lk(self):  # Переход во вкладку "Пользователи" модуля "Личный кабинет"
        WebDriverWait(self.browser, 10).until(
            ec.text_to_be_present_in_element((LoginPageLocators.MY_USER), "Пользователь"))
        self.find(*LoginPageLocators.MY_USER).click()

    def should_be_my_user_in_lk(self):
        assert self.is_element_present(*LoginPageLocators.MY_USER), 'My user if not present!'

    def click_to_add_button(self):
        self.find_to_be_clickable(*Keys.ADD_BUTTON, timeout=60).click()

    def message_note_updated(self):  # Информационное сообщение о том, что запись обновлена
        message = self.find(*Lk.NOTE_UPDATE)
        assert message, 'Отсутствует сообщение "Запись обновлена"'

    def message_note_updated_marker(self):  # Информационное сообщение о том, что заявка на маркер отклонена
        message = self.browser.find_element(*Lk.APPLICATION_REJECTED)
        message_to_assert = self.is_element_present(*Lk.APPLICATION_REJECTED)
        assert message_to_assert, 'Отсутствует сообщение "Заявка отклонена"'
        WebDriverWait(self.browser, 15).until(ec.staleness_of(message)) # Дожидаемся пока сообщение пропадет

    def staleness_of_delete_marker_form(self):
        marker_form = self.browser.find_element(*Lk.DELETE_MARKER_FORM)
        WebDriverWait(self.browser, 30).until(ec.staleness_of(marker_form))

    def message_user_blocked(self):
        message = self.find(*InsideTheOib.MESSAGE_BLOCKED)
        assert message, 'Сообщение не появилось'

    def click_button(self, button):
        time.sleep(1)
        key = self.find_to_be_clickable(*button)
        key.click()

    def fill_reject_reason(self):
        self.find_to_be_clickable(*InsideTheOib.REASON_REJECT_INPUT).send_keys('Отказ')

    def alert_accept(self):
        confirm = self.browser.switch_to.alert
        confirm.accept()

    def find_in_the_search_field(self, locator, inp):
        self.find_to_be_clickable(*locator).send_keys(inp)

    def click_to_submit_key(self):  # Нажать на кнопку сохранить
        self.find(*InsideTheOib.SUBMIT_KEY).click()

    def error_message(self):
        error_message = self.find(*Lk.ERROR_MESSAGE)
        assert error_message, 'Должно появиться информационное сообщение об ошибке'

    def error_have_already_been_used(self):
        error_message = self.find(*Lk.ERROR_PASSWORD_ALREADY_USED)
        assert error_message, 'Должна появиться ошибка'

    def should_be_results(self, locator):
        assert self.is_element_present(*locator), 'No results'

    def clear_input_fill(self, input_fill): #стереть поле нажав на крестик
        self.find(*input_fill).click()

    def delete_input_fill(self, input): #стереть поле нажав 60 раз на клавишу BACKSPACE
        self.find(*input).send_keys('\ue003'*60)

    def should_be_no_results(self):
        assert self.is_element_present(*NoResults.NO_RESULTS), "No results is not present!"

    def click_to_checkbox(self, checkbox):
        self.find_to_be_clickable(*checkbox).click()

    def add_markers_request(self):  # Запрос на добавление маркера
        self.find(*InsideTheOib.ROLE_RAW)
        self.find_to_be_clickable(*Lk.ADD_MARKERS_REQUEST).click()

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



