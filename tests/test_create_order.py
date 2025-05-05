import allure
import requests


from data.handlers import Urls, Handlers
from data.ingredients import Ingredient


@allure.suite("Генерация заказа")
class TestCreateOrder:

    @allure.description("Успешная генерация заказа от авторизованного пользователя, ингредиенты есть")
    @allure.title("Создание заказа с авторизацией и валидными ингредиентами")
    def test_create_order_with_auth(self, create_user):
        with allure.step("Подготовить токен авторизации"):
            token = {'Authorization': create_user[3]}

        with allure.step("Отправить POST-запрос для создания заказа"):
            r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}",
                              headers=token,
                              data=Ingredient.correct_ingredients_data)

        with allure.step("Проверить статус код и успешность создания заказа"):
            assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Заказ сгенерирован от неавторизованного пользователя, ингредиенты есть")
    @allure.title("Создание заказа без авторизации с валидными ингредиентами")
    def test_create_order_not_auth(self):
        with allure.step("Отправить POST-запрос без авторизации"):
            r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}",
                              data=Ingredient.correct_ingredients_data)

        with allure.step("Проверить статус код и успешность создания заказа"):
            assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Возникновение ошибки при отсутствии ингредиентов")
    @allure.title("Попытка создания заказа без ингредиентов")
    def test_create_order_with_ingredient(self):
        with allure.step("Отправить POST-запрос без указания ингредиентов"):
            r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}")

        with allure.step("Проверить статус код и сообщение об ошибке"):
            assert r.status_code == 400 and r.json()["message"] == "Ingredient ids must be provided"

    @allure.description("Возникновение ошибки при передаче невалидного хеша ингредиента")
    @allure.title("Попытка создания заказа с невалидными ингредиентами")
    def test_create_order_invalid_hash_ingridient(self):
        with allure.step("Подготовить заголовки и невалидные данные ингредиентов"):
            headers = Handlers.headers
            payload = Ingredient.incorrect_ingredients_data

        with allure.step("Отправить POST-запрос с невалидными ингредиентами"):
            response = requests.post(Urls.MAIN_URL + Handlers.CREATE_ORDER,
                                     headers=headers,
                                     json=payload)

        with allure.step("Проверить статус код и наличие ошибки сервера"):
            assert response.status_code == 500 and "Internal Server Error" in response.text