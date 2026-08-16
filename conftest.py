import random
import string

import allure
import pytest

from data import SUCCESS_RESPONSE
from helpers import (
    delete_courier,
    register_new_courier_and_return_login_password
)


@pytest.fixture(scope='function')
def created_courier():
    with allure.step('Создать уникального курьера для теста'):
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, 'Не удалось создать курьера для теста'

    yield courier_data

    with allure.step('Удалить тестового курьера'):
        login, password, first_name = courier_data
        delete_response = delete_courier(login, password)
        assert delete_response is not None
        assert delete_response.status_code == 200
        assert delete_response.json() == SUCCESS_RESPONSE


@pytest.fixture(scope='function')
def courier_payload():
    letters = string.ascii_lowercase
    payload = {
        'login': ''.join(random.choice(letters) for i in range(10)),
        'password': ''.join(random.choice(letters) for i in range(10)),
        'firstName': ''.join(random.choice(letters) for i in range(10))
    }

    yield payload

    with allure.step('Удалить курьера, если он был создан в тесте'):
        delete_response = delete_courier(
            payload['login'],
            payload['password']
        )

        if delete_response is not None:
            assert delete_response.status_code == 200
            assert delete_response.json() == SUCCESS_RESPONSE
