import allure
import pytest
import requests

from data import (
    COURIER_ALREADY_EXISTS_RESPONSE,
    NOT_ENOUGH_CREATE_DATA_RESPONSE,
    SUCCESS_RESPONSE
)
from urls import CREATE_COURIER_URL


@allure.feature('Курьер')
@allure.story('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно успешно создать')
    def test_create_courier_success(self, courier_payload):
        with allure.step('Подготовить данные нового курьера'):
            payload = courier_payload.copy()

        with allure.step('Отправить запрос на создание курьера'):
            response = requests.post(CREATE_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 201
            assert response.json() == SUCCESS_RESPONSE

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, created_courier):
        with allure.step('Повторно отправить те же данные'):
            response = requests.post(
                CREATE_COURIER_URL,
                data=created_courier
            )

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 409
            assert response.json() == COURIER_ALREADY_EXISTS_RESPONSE

    @allure.title('Нельзя создать курьера с пустым обязательным полем')
    @pytest.mark.parametrize(
        'empty_field',
        ['login', 'password', 'firstName'],
        ids=['empty_login', 'empty_password', 'empty_first_name']
    )
    def test_create_courier_with_empty_required_field(
        self,
        courier_payload,
        empty_field
    ):
        with allure.step(f'Подготовить данные с пустым полем {empty_field}'):
            payload = courier_payload.copy()
            payload[empty_field] = ''

        with allure.step('Отправить запрос на создание курьера'):
            response = requests.post(CREATE_COURIER_URL, data=payload)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 400
            assert response.json() == NOT_ENOUGH_CREATE_DATA_RESPONSE
