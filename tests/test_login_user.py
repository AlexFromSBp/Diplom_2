import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite("Авторизация пользователя")
class TestLogin:

    @allure.description("Успешная авторизация пользователя с существующими данными")
    @allure.title("Авторизация существующего пользователя")
    def test_login_user(self):
        response = requests.post(f"{Urls.MAIN_URL}{Handlers.AUTH}", data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description("Возникновение ошибки при авторизации несуществующего пользователя")
    @allure.title("Попытка авторизации с несуществующим email/password")
    def test_login_user_error(self):
        response = requests.post(f"{Urls.MAIN_URL}{Handlers.AUTH}", data=User.data_wrong_date)
        assert response.status_code == 401 and response.json().get("success") == False
