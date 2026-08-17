import random
import string

import allure
import pytest

from helpers import (
    delete_courier,
    register_new_courier_and_return_login_password
)


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
        delete_courier(
            payload['login'],
            payload['password']
        )


@pytest.fixture(scope='function')
def created_courier(courier_payload):
    with allure.step('Создать уникального курьера для теста'):
        register_new_courier_and_return_login_password(courier_payload)

    return courier_payload
