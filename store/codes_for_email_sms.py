import email
import imaplib
import time
from opensearchpy import OpenSearch
from datetime import datetime as dt


class Codes:

    @staticmethod
    def auth_sms():
        """ Метод для автоматического получения кодов подтверждения с телефона.
        Примечание: Заранее установленное приложение на телефон, которое переадресовывает смс на указанную почту 'forautotests@mail.ru'
        Далее полученные письма обрабатываем с помощью метода описанного в 'Метод для автоматического получения кодов подтверждения с почты'
        1  Определяем интерпретатор для нашего скрипта;
        2  Явно указываем кодировку;
        4  Импортируем модуль imaplib для возможности подключения к почтовому ящику по IMAP;
        6  Создаем сессию для подключения к почтовому ящику по IMAP и заносим ее в переменную mail;
        7  Подключаемся к почтовому ящику по IMAP с использованием учетной записи forautotests@mail.ru;
        9  Выводим список папок в почтовом ящике;
        10  Выбираем для работы папку входящие (sms);
        11  Получаем массив со списком найденных почтовых сообщений;
        12  Сохраняем в переменную ids строку с номерами писем;
        13  Получаем массив номеров писем;
        14  Задаем переменную latest_email_id, значением которой будет номер последнего письма;
        15  Получаем письмо с идентификатором latest_email_id (последнее письмо);
        16  В переменную raw_email заносим необработанное письмо;
        17  Переводим текст письма в кодировку UTF-8 и сохраняем в переменную raw_email_string;
        18  Импортируем модуль email для получения заголовков и тела писем;
        19  Получаем заголовки и тело письма и заносим результат в переменную email_message. Обратите внимание, что мы используем переменную raw_email_string, в которую на этапе выше занесли необработанное письмо;
        20  Проверяем, является ли письмо многокомпонентным. Если да, то выводим по очереди на экран значения каждого компонента. Предварительно, перекодируем текст в UTF-8;
        21  Если письмо не многокомпонентное, выводим его содержимое;
        22  Убираем лишнее из письма, используя метод выборки чисел из текста.
        23  На выходе получаем код. """

        mail = imaplib.IMAP4_SSL('imap.mail.ru')
        mail.login('forautotests@mail.ru', 'ghv9wuS3brnBusTBN4gn')

        mail.list()
        mail.select("sms")

        result, data = mail.search(None, "ALL")

        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]

        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)

        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
                string = body
                sms_result = string.split(' ')
                print(sms_result[9])
                sms_result2 = sms_result[9]
        else:
            body = email_message.get_payload(decode=True).decode('utf-8')
        return sms_result2

    @staticmethod
    def auth_email(email_name):
        """ Метод для автоматического получения кодов подтверждения с почты.
        Примечание: Используется мэйл почта с дополнительной настройкой протоколов доступа.
        Данные от почты: логин - forautotests2@mail.ru пароль - TrueGamesoiude21
        Пароль указанный в программе отличается, так как для доступа через imaplib, требуется отдельный пароль - UmxyVDmB6T3sEcaErEdE для forautotests2@mail.ru
        Пароль указанный в программе отличается, так как для доступа через imaplib, требуется отдельный пароль - ghv9wuS3brnBusTBN4gn для forautotests@mail.ru
        Далее идет описание хода работы программы.
        1  Определяем интерпретатор для нашего скрипта;
        2  Явно указываем кодировку;
        4  Импортируем модуль imaplib для возможности подключения к почтовому ящику по IMAP;
        6  Создаем сессию для подключения к почтовому ящику по IMAP и заносим ее в переменную mail;
        7  Подключаемся к почтовому ящику по IMAP с использованием учетной записи forautotests@mail.ru;
        9  Выводим список папок в почтовом ящике;
        10  Выбираем для работы папку входящие (elpts);
        11  Получаем массив со списком найденных почтовых сообщений;
        12  Сохраняем в переменную ids строку с номерами писем;
        13  Получаем массив номеров писем;
        14  Задаем переменную latest_email_id, значением которой будет номер последнего письма;
        15  Получаем письмо с идентификатором latest_email_id (последнее письмо);
        16  В переменную raw_email заносим необработанное письмо;
        17  Переводим текст письма в кодировку UTF-8 и сохраняем в переменную raw_email_string;
        18  Импортируем модуль email для получения заголовков и тела писем;
        19  Получаем заголовки и тело письма и заносим результат в переменную email_message. Обратите внимание, что мы используем переменную raw_email_string, в которую на этапе выше занесли необработанное письмо;
        20  Проверяем, является ли письмо многокомпонентным. Если да, то выводим по очереди на экран значения каждого компонента. Предварительно, перекодируем текст в UTF-8;
        21  Если письмо не многокомпонентное, выводим его содержимое;
        22  Убираем лишнее из письма, используя метод выборки чисел из текста.
        23  На выходе получаем код.
        24	Выбираем для работы папку elpts. Явно указываем, что мы подключаемся к каталогу в режиме не только для чтения
        25	Получаем массив со списком найденных почтовых сообщений
        26	Сохраняем в переменную ids строку с номерами писем
        27	Получаем массив номеров писем
        28	Делаем перебор нашего массива id_list (список идентификаторов писем)
        29	Копируем письмо с идентификатором mail_id в каталог Completed. Резуьтат заносим в переменную copy_res
        30 	Проверяем результат копирования письма. Если письмо успешно скопировано, то устанавливаем на него флаг Deleted (для удаления)
        31	Удаляем все письма с установленным флагом Deleted"""

        login1 = 'forautotests@mail.ru'
        login2 = 'forautotests2@mail.ru'
        password1 = 'ghv9wuS3brnBusTBN4gn'
        password2 = 'UmxyVDmB6T3sEcaErEdE'
        mail = imaplib.IMAP4_SSL('imap.mail.ru')
        if email_name == 'forautotests@mail.ru':
            mail.login(login1, password1)
        else:
            mail.login(login2, password2)

        mail.list()
        mail.select("elpts")

        result, data = mail.search(None, "ALL")

        ids = data[0]

        id_list = ids.split()
        i = 0
        while len(id_list) <= 0 and i < 20:
            time.sleep(5)
            i = i + 1
            mail.list()
            mail.select("elpts")

            result, data = mail.search(None, "ALL")

            ids = data[0]

            id_list = ids.split()
        latest_email_id = id_list[-1]

        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)

        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
        else:
            body = email_message.get_payload(decode=True).decode('utf-8')
            string = body
            email_result = string.split(' ')
            email_result3 = email_result[11]

        mail.select("elpts", readonly=False)
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()

        for mail_id in id_list:
            copy_res = mail.copy(mail_id, 'Completed')
            if copy_res[0] == 'OK':
                delete_res = mail.store(mail_id, '+FLAGS', '\\Deleted')

        mail.expunge()
        return email_result3

    @staticmethod
    def clean_email(email_name):
        """ Метод для автоматической чистки папки на почте.
        1	Выбираем для работы папку elpts. Явно указываем, что мы подключаемся к каталогу в режиме не только для чтения
        2	Получаем массив со списком найденных почтовых сообщений
        3	Сохраняем в переменную ids строку с номерами писем
        4	Получаем массив номеров писем
        5	Делаем перебор нашего массива id_list (список идентификаторов писем)
        6	Копируем письмо с идентификатором mail_id в каталог Completed. Резуьтат заносим в переменную copy_res
        7	Проверяем результат копирования письма. Если письмо успешно скопировано, то устанавливаем на него флаг Deleted (для удаления)
        8	Удаляем все письма с установленным флагом Deleted"""

        login1 = 'forautotests@mail.ru'
        login2 = 'forautotests2@mail.ru'
        password1 = 'ghv9wuS3brnBusTBN4gn'
        password2 = 'UmxyVDmB6T3sEcaErEdE'
        mail = imaplib.IMAP4_SSL('imap.mail.ru')
        if email_name == 'forautotests@mail.ru':
            mail.login(login1, password1)
        else:
            mail.login(login2, password2)

        mail.list()
        mail.select("elpts", readonly=False)
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()

        for mail_id in id_list:
            copy_res = mail.copy(mail_id, 'Completed')
            if copy_res[0] == 'OK':
                delete_res = mail.store(mail_id, '+FLAGS', '\\Deleted')

        mail.expunge()

    @staticmethod
    def auth_sms_from_opensearch(sid):
        """
        Метод принимает SID сессии пользователя и возвращает СМС-код из OpenSearch для подтверждения (сервис sms-srv).
        """
        host = [{'host': 'osearchtst.ppdp.int', 'port': 9200}]
        auth = ('admin', 'admin')

        client = OpenSearch(
            hosts=host,
            http_compress=True,
            http_auth=auth,
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

        log_data = dt.today().strftime("%Y-%m-%d")
        index = f'event_log-{log_data}'

        query = {
            "query": {
                "query_string": {
                    "query": f"srv_key:sms-srv AND sid_key:{sid}"
                }
            },
            "size": 10,
            "from": 0,
            "sort": [
                {
                    "method_key": {
                        "unmapped_type": "keyword",
                        "order": "asc"
                    }
                }
            ]
        }

        response = client.search(
            body=query,
            index=index,
        )
        print(response)
        print(sid)
        try:
            return response['hits']['hits'][0]['_source']['body'][24:30]
        except IndexError as error:
            print(f'Не получили SID из OpenSearch, возникла ошибка: {error}')