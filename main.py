import requests
import random
import os
ya_token = 'AQAAAAATlnZQAADLW5A840miiEbKjoTh8Um5GHo'
folder_name = 'Test_folder' + str(random.randint(1, 999))
YA_API_BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {
    "Accept": "application/json",
    "Authorization": "OAuth " + ya_token
}
params = {
    'path': '/' + folder_name
}


def folder_maker():
    status_code_dict = {
        201:	'OK',
        400:	'Некорректные данные.',
        401:	'Не авторизован.',
        403:    'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или увеличьте объём Диска.',
        404:    'Не удалось найти запрошенный ресурс.',
        406:	'Ресурс не может быть представлен в запрошенном формате.',
        409:	'Ресурс "{path}" уже существует.',
        423:	'Ресурс заблокирован. Возможно, над ним выполняется другая операция.',
        429:	'Слишком много запросов.',
        503:	'Сервис временно недоступен.',
        507:	'Недостаточно свободного места.'
    }
    response = requests.put(YA_API_BASE_URL, params=params, headers=headers)
    if 200 <= response.status_code <= 299:
        return True
    else:
        print(status_code_dict[response.status_code])
        return False


def folder_deleter():
    status_code_dict = {
    200:	'OK',
    202:	'Операция выполняется асинхронно.',
    204:	'OK',
    400:	'Проверка md5 возможна только для файлов',
    401:	'Не авторизован.',
    403:	'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или увеличьте объём Диска.',
    404:	'Не удалось найти запрошенный ресурс.',
    406:	'Ресурс не может быть представлен в запрошенном формате.',
    409:	'Ресурс уже существует.',
    423:	'Ресурс заблокирован. Возможно, над ним выполняется другая операция.',
    429:	'Слишком много запросов.',
    503:	'Сервис временно недоступен.'
    }
    response = requests.delete(YA_API_BASE_URL, params=params, headers=headers)

    if 200 <= response.status_code <= 299:
        return True
    else:
        print(status_code_dict[response.status_code])
        return False

def is_test_folder_exist():
    status_code_dict = {
        200: 'Успешно.',
        400: 'Некорректные данные.',
        401: 'Не авторизован.',
        403: 'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или увеличьте объём Диска.',
        404: 'Не удалось найти запрошенный ресурс.',
        406: 'Ресурс не может быть представлен в запрошенном формате.',
        429: 'Слишком много запросов.',
        503: 'Сервис временно недоступен.',
    }
    response = requests.get(YA_API_BASE_URL, params=params, headers=headers)

    if response.status_code == 200:
        return True
    else:
        print(status_code_dict[response.status_code])
        return False


if __name__ == '__main__':
    print("Проверка функционала Яндекс.Диск REST API, отвечающего за создание папки.")
    print(f"Существует ли тестовая папка {folder_name}?")
    while is_test_folder_exist():
        print(f"Тестовая папка {folder_name} существует, попробуем другое имя.")
        folder_name = 'Test_folder' + str(random.randint(1, 999))
        print(f"Новое имя для тестовой папки: {folder_name}?")
    print(f"Папки с тами именем нет, попробуем её создать.")
    if not folder_maker():
        print("Создать папку не удалось.")
    else:
        if is_test_folder_exist():
            print(f"Папка {folder_name} создана.")
            print("***Функционал Яндекс.Диск REST API, отвечающий за создание папки, работает.***")
        if (folder_deleter()):
            print(f"Папка {folder_name} удалена с Яндекс.Диска .")
    os.system("pause")