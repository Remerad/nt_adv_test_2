import test
from main import *
import mock
import random


class TestCalculatePytest:
    ya_token = 'AQAAAAATlnZQAADLW5A840miiEbKjoTh8Um5GHo'

    def setup(self):
        self.test_YAfm = YA_API_folder_maker(self.ya_token)
        while self.test_YAfm.is_test_folder_exist():
            print(f"Тестовая папка {self.test_YAfm.folder_name} существует, попробуем другое имя.")
            self.test_YAfm.folder_name = 'Test_folder' + str(random.randint(1, 999))
            print(f"Новое имя для тестовой папки: {folder_name}?")
        print(f"Папки с тами именем нет, попробуем её создать.")

    def teardown(self):
        self.test_YAfm.delete_folder()
        print("Конец программы")


    def test_make_folder(self):
        status_code_dict = {
            201: 'OK',
            400: 'Некорректные данные.',
            401: 'Не авторизован.',
            403: 'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или увеличьте объём Диска.',
            404: 'Не удалось найти запрошенный ресурс.',
            406: 'Ресурс не может быть представлен в запрошенном формате.',
            409: 'Ресурс "{path}" уже существует.',
            423: 'Ресурс заблокирован. Возможно, над ним выполняется другая операция.',
            429: 'Слишком много запросов.',
            503: 'Сервис временно недоступен.',
            507: 'Недостаточно свободного места.'
        }
        response = self.test_YAfm.make_folder()
        if 200 <= response.status_code <= 299:
            assert True
        else:
            print(f"Ошибка: {status_code_dict[response.status_code]}")
            assert False
