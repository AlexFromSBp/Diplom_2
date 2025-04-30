from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": "correct_mail@ya.ru",
        "password": "password"}

    data_wrong_date = {
        "email": "wrong_mail@ya.ru",
        "password": "password"}

    data_no_mail = {
        "email": "",
        "password": "password",
        "name": "User"}

    data_no_password = {
        "email": "no_password@ya.ru",
        "password": "",
        "name": "Username"}

    data_without_name = {
        "email": "without_name@yandex.ru",
        "password": "password",
        "name": ""}

    data_repeat = {
        "email": "without_name@yandex.ru",
        "password": "password",
        "name": "Username"}

    data_change = {
        "email": "without_name@yandex.ru",
        "password": "password",
        "name": "Test"}
