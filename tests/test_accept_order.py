import allure
import requests

from data import (
    COURIER_ID_DOES_NOT_EXIST_RESPONSE,
    NONEXISTENT_ID,
    NOT_ENOUGH_SEARCH_DATA_RESPONSE,
    ORDER_ID_DOES_NOT_EXIST_RESPONSE,
    SUCCESS_RESPONSE
)
from urls import ACCEPT_ORDER_URL


@allure.feature('Заказы')
@allure.story('Принятие заказа')
class TestAcceptOrder:

    @allure.title('Курьер может успешно принять заказ')
    def test_accept_order_success(self, courier_id, order_id):
        with allure.step('Отправить запрос на принятие заказа'):
            response = requests.put(
                f'{ACCEPT_ORDER_URL}/{order_id}',
                params={'courierId': courier_id}
            )

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 200
            assert response.json() == SUCCESS_RESPONSE

    @allure.title('Нельзя принять заказ без id курьера')
    def test_accept_order_without_courier_id(self, order_id):
        with allure.step('Отправить запрос без query-параметра courierId'):
            response = requests.put(f'{ACCEPT_ORDER_URL}/{order_id}')

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 400
            assert response.json() == NOT_ENOUGH_SEARCH_DATA_RESPONSE

    @allure.title('Нельзя принять заказ с неверным id курьера')
    def test_accept_order_with_nonexistent_courier_id(self, order_id):
        with allure.step('Передать неверный id курьера в query-параметре'):
            response = requests.put(
                f'{ACCEPT_ORDER_URL}/{order_id}',
                params={'courierId': NONEXISTENT_ID}
            )

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == COURIER_ID_DOES_NOT_EXIST_RESPONSE

    @allure.title('Нельзя принять заказ без id заказа')
    def test_accept_order_without_order_id(self, courier_id):
        with allure.step('Отправить запрос без id заказа в URL'):
            response = requests.put(
                ACCEPT_ORDER_URL,
                params={'courierId': courier_id}
            )

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 400
            assert response.json() == NOT_ENOUGH_SEARCH_DATA_RESPONSE

    @allure.title('Нельзя принять заказ с неверным id заказа')
    def test_accept_order_with_nonexistent_order_id(self, courier_id):
        with allure.step('Передать неверный id заказа в URL'):
            response = requests.put(
                f'{ACCEPT_ORDER_URL}/{NONEXISTENT_ID}',
                params={'courierId': courier_id}
            )

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == ORDER_ID_DOES_NOT_EXIST_RESPONSE
