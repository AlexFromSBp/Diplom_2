import allure
import requests

from data.handlers import Urls, Handlers
from data.ingredients import Ingredient


@allure.suite("Получить заказы конкретного пользователя")
class TestGetOrderUser:

    @allure.description("Успешное получение доступных заказов авторизованного пользователя")
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        with allure.step("Подготовить токен авторизации"):
            token = {"Authorization": create_user[3]}

        with allure.step("Создать тестовый заказ"):
            requests_create_order = requests.post(
                f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}",
                headers=token,
                data=Ingredient.correct_ingredients_data
            )

        with allure.step("Получить список заказов пользователя"):
            response_get_order = requests.get(
                f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}",
                headers=token
            )

        with allure.step("Проверить статус код и соответствие номеров заказов"):
            assert response_get_order.status_code == 200
            assert response_get_order.json()["orders"][0]["number"] == \
                   requests_create_order.json()["order"]["number"]

    @allure.description("Возникновение ошибки при получение заказов пользователя без авторизации")
    @allure.title("Попытка получения заказов без авторизации")
    def test_get_order_user_not_auth(self):
        with allure.step("Отправить GET-запрос без авторизации"):
            r = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}")

        with allure.step("Проверить статус код и сообщение об ошибке"):
            assert r.status_code == 401
            assert r.json()["message"] == "You should be authorised"