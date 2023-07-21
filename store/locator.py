from selenium.webdriver.common.by import By


class SberPageLocators:
    # Поле поиск
    FIELD_SEARCH = (By.XPATH, "//input[@placeholder='Профессия, навык или сфера']")
    BUTTON_SEARCH = (By.XPATH, "//button[@class='styled__Button-sc-1vm2lnu-0 ktremY']")
    # Поле регион/город
    FIELD_CITY = (By.XPATH, "//input[@placeholder='Город/регион']")
    MOSCOW = (By.XPATH, "//div[contains(@class,'Text-sc-36c35j-0 okCCd')][contains(text(),'г Москва')]")
    FIELD_SEARCH_PROFFESION = (By.XPATH, "//input[@placeholder='Какую специальность ищешь?']")
    RESET = (By.XPATH, "//button[@class='styled__Button-sc-1vm2lnu-0 styled__ClearButton-sc-1fgc3ot-0 gqakuA iaZRMU']")
    # Чек-бокс доступно для людей с инвалидностью
    CHECKBOX_FOR_INVALIDS = (By.XPATH, "//label[@class='styled__IconWrapper-sc-l642s6-2 cVAOxy']//*[name()='svg']")
    # Раздел Карьерные медиа
    BUTTON_CAREER_MEDIA = (By.XPATH, "//a[contains(text(),'Карьерные медиа')]")
    BUTTON_LEARN_MORE = (By.XPATH, "//div[@class='swiper-slide swiper-slide-active']//a[contains(text(),'Подробнее')]")
    BOOTSTRAP_FORWARD = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]')
    BOOTSTRAP_BACK = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div/div/div[2]/div[1]')
    BUTTON_FILTER = (By.XPATH, "//button[@class='styled__Button-sc-1vm2lnu-0 btitRc']")
    BUTTON_RESET_ALL = (By.XPATH, "//div[@class='Box-sc-159i47a-0 lpegKi']//div[1]")
    CHECKBOX_CAREER = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div/div/div[3]/div[2]/div[2]/div/div/div/div['
                                 '3]/div[2]/div[10]/div')
    CHECKBOX_PODCAST = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div/div/div[3]/div[2]/div[2]/div/div/div/div['
                                  '2]/div[2]/div[3]/div')
    ABOUT_CAREER = (By.XPATH, "//img[@alt='О карьере']")
    BUTTON_CLOSE = (By.XPATH, "/html/body/div[3]/div/div[3]/span/img")
    # Раздел Студентам & выпускникам
    BUTTON_GRADUATE_STUDENTS = (By.XPATH, "//a[contains(text(),'Выпускникам и студентам')]")
    BUTTON_LEARN_MORE_STUDENTS = (By.XPATH, "//div[contains(@class,'swiper-slide swiper-slide-active')]//div["
                                            "contains(@class,'styled__Button-sc-1vm2lnu-0 ktremY')]")


class MyofficePageLocators:
    BUTTON_ACCEPT = (By.XPATH, '//*[@id="cookie"]/div/div/div/a')
    BUTTON_SPLIT_BISSNES = (By.XPATH, "//button[@class='accordion']")
    BUTTON_SPLIT_STATE = (By.XPATH, "//button[contains(text(),'Для государственных организаций')]")
    DESCRIPTION_BISSNES = (By.XPATH, "//p[contains(text(),'Используйте почтовую систему не только для обмена ')]")
    DESCRIPTION_STATE = (By.XPATH, "//p[contains(text(),'Создайте единую систему для коммуникаций между все')]")
    BUTTON_PC = (By.XPATH, "//section[@class='for__whom for__whom2']//li[1]")
    BUTTON_MOBILE = (By.XPATH, "//section[@class='for__whom for__whom2']//li[2]")
    BUTTON_SERVER = (By.XPATH, "//section[@class='for__whom for__whom2']//li[3]")
