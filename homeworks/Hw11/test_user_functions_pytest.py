import pytest
import os
import shutil
import json
from config import Config
from user_functions import check_email, create_file, user_add, update_user

TEST_ALL_USERS_DATA = [{"first_name": "test", "last_name": "test", "Email": "test@test.com", "id": 1},
                       {"first_name": "test1", "last_name": "test1", "Email": "test1@test.com", "id": 2}]
TEST_EMAIL = "test@test.com"
TEST_FALSE_EMAIL = "sobaka@sobaka.com"
TEST_DATABASE_DIRECTORY = 'test_database'
TEST_FILE = 'test.json'
TEST_FILE_PATH = TEST_DATABASE_DIRECTORY + "/" + TEST_FILE
TEST_INPUT = "just_test"
TEST_USER_ID = 1


if os.path.exists(TEST_DATABASE_DIRECTORY):
    shutil.rmtree(TEST_DATABASE_DIRECTORY)
Config.USERS_DIRECTORY = TEST_DATABASE_DIRECTORY
Config.USERS_FILE = TEST_FILE
Config.PATH_TO_USERS_FILE = TEST_FILE_PATH


def test_check_email():
    assert check_email(TEST_EMAIL, TEST_ALL_USERS_DATA) == True
    assert check_email(TEST_FALSE_EMAIL, TEST_ALL_USERS_DATA) == False


def test_create_file():
    file = create_file()
    assert os.path.exists(TEST_DATABASE_DIRECTORY) == True
    assert os.path.exists(Config.PATH_TO_USERS_FILE) == True
    data = json.loads(file.read())
    assert type(data) == list
    file.close()
    shutil.rmtree(TEST_DATABASE_DIRECTORY)


def test_user_add(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: TEST_INPUT)
    user_add()
    file = open(Config.PATH_TO_USERS_FILE, 'r')
    data = json.loads(file.read())
    file.close()
    assert (len(data) > 0) == True
    assert data[0]['first_name'] == TEST_INPUT
    assert data[0]['id'] == 1
    shutil.rmtree(TEST_DATABASE_DIRECTORY)


def test_update_user(monkeypatch):
    file = create_file()
    file.close()
    with open(Config.PATH_TO_USERS_FILE, 'w') as file:
        file.write(json.dumps(TEST_ALL_USERS_DATA))
    monkeypatch.setattr('builtins.input', lambda x: TEST_USER_ID)
    update_user()

    '''testing'''

    file = open(Config.PATH_TO_USERS_FILE, 'r')
    data = json.loads(file.read())
    assert data[0]['first_name'] == TEST_USER_ID
    assert data[0]['last_name'] == TEST_USER_ID
    assert data[0]['Email'] == TEST_USER_ID
    file.close()
    shutil.rmtree(TEST_DATABASE_DIRECTORY)