import random
import string

import allure
import pytest
import requests

from data import ORDER_DATA
from helpers import (
    delete_courier,
    register_new_courier_and_return_login_password
)
from urls import (
    CREATE_ORDER_URL,
    GET_ORDER_BY_TRACK_URL,
    LOGIN_COURIER_URL
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


@pytest.fixture(scope='function')
def courier_id(created_courier):
    response = requests.post(
        LOGIN_COURIER_URL,
        data={
            'login': created_courier['login'],
            'password': created_courier['password']
        }
    )

    return response.json()['id']


@pytest.fixture(scope='function')
def created_order():
    response = requests.post(CREATE_ORDER_URL, json=ORDER_DATA)

    return response.json()['track']


@pytest.fixture(scope='function')
def order_id(created_order):
    response = requests.get(
        GET_ORDER_BY_TRACK_URL,
        params={'t': created_order}
    )

    return response.json()['order']['id']
