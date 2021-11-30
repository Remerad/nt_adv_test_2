from main import *
import random


class TestFolderMakerPytest:
    ya_token = 'AQAAAAATlnZQAADLW5A840miiEbKjoTh8Um5GHo'

    def setup(self):
        self.test_YAfm = YA_API_folder_maker(self.ya_token)
        while self.test_YAfm.is_test_folder_exist():
            self.test_YAfm.folder_name = 'Test_folder' + str(random.randint(1, 999))

    def teardown(self):
        self.test_YAfm.delete_folder()

    def test_make_folder(self):
        response = self.test_YAfm.make_folder()
        if 200 <= response.status_code <= 299:
            assert True
        else:
            assert False
