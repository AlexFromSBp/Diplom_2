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
        with allure.step("Подготовить данные пользователя"):
            user_data = User.create_data_user()

        with allure.step("Отправить POST-запрос для создания пользователя"):
            response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=user_data)

        with allure.step("Проверить успешность создания пользователя"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.description("Возникновение ошибки при создании дубликата карточки")
    @allure.title("Создание пользователя с использованными ранее данными")
    def test_create_double_user_error(self):
        with allure.step("Подготовить данные уже существующего пользователя"):
            user_data = User.data_repeat

        with allure.step("Отправить POST-запрос с дублирующимися данными"):
            response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=user_data)

        with allure.step("Проверить ошибку дублирования пользователя"):
            assert response.status_code == 403
            assert "User already exists" in response.text

    @allure.description("Возникновение ошибки при генерация карточки пользователя с пропуском поля")
    @allure.title("Генерация пользователя с пустым обязательным полем")
    @pytest.mark.parametrize("user_data", [User.data_no_mail, User.data_no_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        with allure.step(f"Подготовить данные пользователя с пропущенным полем: {user_data}"):
            test_data = user_data

        with allure.step("Отправить POST-запрос с неполными данными"):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=test_data)

        with allure.step("Проверить сообщение об ошибке валидации"):
            assert response.status_code == 403
            assert 'Email, password and name are required fields' in response.text
