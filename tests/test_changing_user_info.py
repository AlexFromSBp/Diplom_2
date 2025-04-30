import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite("Обновление информации о пользователе")
class TestChangingUserData:

    @allure.description("Успешное изменение поля email у авторизованного пользователя ")
    @allure.title("Замена данных в поле email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, create_user):
        payload = {"email": User.create_data_user()["email"]}
        token = {"Authorization": create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_INFO}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()["user"]["email"] == payload["email"]

    @allure.description("Успешное изменение поля password у авторизованного пользователя")
    @allure.title("Замена данных в поле password авторизованного пользователя")
    def test_changing_user_password_with_auth(self, create_user):
        payload = {"password": User.create_data_user()["password"]}
        token = {"Authorization": create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_INFO}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Успешное изменение поля name у авторизованного пользователя")
    @allure.title("Замена данных в поле name авторизованного пользователя")
    def test_changing_user_name_with_auth(self, create_user):
        payload = {"name": User.create_data_user()["name"]}
        token = {"Authorization": create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_INFO}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()["user"]["name"] == payload["name"]

    @allure.description("Возникновение ошибки при изменении полей у неавторизованного пользователя")
    @allure.title("Замена данных неавторизованного пользователя")
    def test_changing_user_data_not_auth(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_INFO}", data=User.create_data_user())
        assert r.status_code == 401 and r.json()["message"] == "You should be authorised"
