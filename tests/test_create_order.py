import allure
import requests


from data.handlers import Urls, Handlers
from data.ingredients import Ingredient


@allure.suite("Генерация заказа")
class TestCreateOrder:

    @allure.description("Успешная генерация заказа от авторизованного пользователя, ингредиенты есть")
    @allure.title("")
    def test_create_order_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}", headers=token, data=Ingredient.correct_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Заказ сгенерирован от неавторизованного пользователя, ингредиенты есть")
    @allure.title("")
    def test_create_order_not_auth(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}", data=Ingredient.correct_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True


    @allure.description("Возникновение ошибки при отсутствии ингредиентов")
    @allure.title("")
    def test_create_order_with_ingredient(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}")
        assert r.status_code == 400 and r.json()["message"] == "Ingredient ids must be provided"

    @allure.description("Возникновение ошибки при передаче невалидного хеша ингредиента")
    @allure.title("")
    def test_create_order_invalid_hash_ingridient(self):
        response = requests.post(Urls.MAIN_URL + Handlers.CREATE_ORDER, headers=Handlers.headers,
                                 json=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500 and "Internal Server Error" in response.text
