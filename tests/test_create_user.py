import pytest
import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite("Генерация карточки пользователя")
class TestCreateUser:

    @allure.description("Генерация карточки пользователя")
    @allure.title("Генерация карточки пользователя")
    def test_create_user_success(self):
        response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=User.create_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.description("Возникновение ошибки при создании дубликата карточки")
    @allure.title("Создание пользователя с использованными ранее данными")
    def test_create_double_user_error(self):
        response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=User.data_repeat)
        assert response.status_code == 403 and "User already exists" in response.text

    @allure.description("Возникновение ошибки при генерация карточки пользователя с пропуском поля")
    @allure.title("Генерация пользователя с пустым обязательным полем")
    @pytest.mark.parametrize("user_data", [User.data_no_mail, User.data_no_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text
