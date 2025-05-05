class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"


class Handlers:
    CREATE_ORDER = "/api/orders"
    CREATE_USER = "/api/auth/register"
    AUTH = "/api/auth/login"
    CHANGE_USER_INFO = "/api/auth/user"
    DELETE_USER = "/api/auth/user"
    GET_ORDERS = "/api/orders"

    headers = {"Content-Type": "application/json"}
