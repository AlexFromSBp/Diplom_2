import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite("Авторизация пользователя")
class TestLogin:

    @allure.description("Успешная авторизация пользователя с существующими данными")
    @allure.title("Авторизация существующего пользователя")
    def test_login_user(self):
        with allure.step("Подготовить корректные данные пользователя"):
            user_data = User.data_correct

        with allure.step("Отправить POST-запрос на авторизацию"):
            response = requests.post(
                f"{Urls.MAIN_URL}{Handlers.AUTH}",
                data=user_data
            )

        with allure.step("Проверить успешность авторизации"):
            assert response.status_code == 200
            assert response.json().get('success') is True

    @allure.description("Возникновение ошибки при авторизации несуществующего пользователя")
    @allure.title("Попытка авторизации с несуществующим email/password")
    def test_login_user_error(self):
        with allure.step("Подготовить некорректные данные пользователя"):
            user_data = User.data_wrong_date

        with allure.step("Отправить POST-запрос с неверными данными"):
            response = requests.post(
                f"{Urls.MAIN_URL}{Handlers.AUTH}",
                data=user_data
            )

        with allure.step("Проверить сообщение об ошибке авторизации"):
            assert response.status_code == 401
            assert response.json().get("success") is False
