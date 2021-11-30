import requests
import random
import os


class YA_API_folder_maker:
    ya_token = ''
    folder_name = 'Test_folder' + str(random.randint(1, 999))
    YA_API_BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Accept": "application/json",
        "Authorization": "OAuth " + ya_token
    }
    params = {
        'path': '/' + folder_name
    }

    def __init__(self, TOKEN):
        self.ya_token = TOKEN
        self.headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + self.ya_token
        }

    def make_folder(self):
        return requests.put(self.YA_API_BASE_URL,
                            params=self.params,
                            headers=self.headers)

    def delete_folder(self):
        response = requests.delete(self.YA_API_BASE_URL,
                                   params=self.params,
                                   headers=self.headers)
        if 200 <= response.status_code <= 299:
            return True
        else:
            return False

    def is_test_folder_exist(self):
        response = requests.get(self.YA_API_BASE_URL,
                                    params=self.params,
                                    headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False


if __name__ == '__main__':
    YAfm = YA_API_folder_maker(input("Введите токен Яндекс Диска: "))
    print("Проверка функционала Яндекс.Диск REST API, отвечающего за создание папки.")
    print(f"Существует ли тестовая папка {YAfm.folder_name}?")
    while YAfm.is_test_folder_exist():
        print(f"Тестовая папка {YAfm.folder_name} существует, попробуем другое имя.")
        YAfm.folder_name = 'Test_folder' + str(random.randint(1, 999))
        print(f"Новое имя для тестовой папки: {YAfm.folder_name}?")
    print(f"Папки с тами именем нет, попробуем её создать.")
    if not YAfm.make_folder():
        print("Создать папку не удалось.")
    else:
        if YAfm.is_test_folder_exist():
            print(f"Папка {YAfm.folder_name} создана.")
            print("***Функционал Яндекс.Диск REST API, отвечающий за создание папки, работает.***")
        if (YAfm.delete_folder()):
            print(f"Папка {YAfm.folder_name} удалена с Яндекс.Диска .")
    os.system("pause")