import random
import string

import allure
import pytest
import requests

from data import (
    COURIER_NOT_FOUND_RESPONSE,
    NOT_ENOUGH_LOGIN_DATA_RESPONSE
)
from urls import LOGIN_COURIER_URL


@allure.feature('Курьер')
@allure.story('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Созданный курьер может авторизоваться')
    def test_login_courier_success(self, created_courier):
        with allure.step('Подготовить логин и пароль созданного курьера'):
            login, password, first_name = created_courier
            payload = {'login': login, 'password': password}

        with allure.step('Отправить запрос на авторизацию'):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 200
            assert 'id' in response.json()
            assert response.json()['id'] is not None

    @allure.title('Нельзя авторизоваться с пустым обязательным полем')
    @pytest.mark.parametrize(
        'empty_field',
        ['login', 'password'],
        ids=['empty_login', 'empty_password']
    )
    def test_login_courier_with_empty_required_field(
        self,
        created_courier,
        empty_field
    ):
        with allure.step(f'Подготовить данные с пустым полем {empty_field}'):
            login, password, first_name = created_courier
            payload = {'login': login, 'password': password}
            payload[empty_field] = ''

        with allure.step('Отправить запрос на авторизацию'):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 400
            assert response.json() == NOT_ENOUGH_LOGIN_DATA_RESPONSE

    @allure.title('Нельзя авторизоваться с неправильным логином')
    def test_login_courier_with_wrong_login(self, created_courier):
        with allure.step('Подготовить неправильный логин'):
            login, password, first_name = created_courier
            payload = {'login': f'{login}wrong', 'password': password}

        with allure.step('Отправить запрос на авторизацию'):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == COURIER_NOT_FOUND_RESPONSE

    @allure.title('Нельзя авторизоваться с неправильным паролем')
    def test_login_courier_with_wrong_password(self, created_courier):
        with allure.step('Подготовить неправильный пароль'):
            login, password, first_name = created_courier
            payload = {'login': login, 'password': f'{password}wrong'}

        with allure.step('Отправить запрос на авторизацию'):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == COURIER_NOT_FOUND_RESPONSE

    @allure.title('Нельзя авторизоваться как несуществующий курьер')
    def test_login_nonexistent_courier(self):
        with allure.step('Подготовить уникальные несуществующие данные'):
            letters = string.ascii_lowercase
            payload = {
                'login': ''.join(random.choice(letters) for i in range(20)),
                'password': ''.join(random.choice(letters) for i in range(20))
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == COURIER_NOT_FOUND_RESPONSE
