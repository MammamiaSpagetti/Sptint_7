import allure
import requests

from data import (
    NONEXISTENT_ID,
    NOT_ENOUGH_SEARCH_DATA_RESPONSE,
    ORDER_NOT_FOUND_RESPONSE
)
from urls import GET_ORDER_BY_TRACK_URL


@allure.feature('Заказы')
@allure.story('Получение заказа по трек-номеру')
class TestGetOrderByTrack:

    @allure.title('Можно получить заказ по его трек-номеру')
    def test_get_order_by_track_success(self, created_order):
        with allure.step('Передать трек-номер заказа в query-параметре'):
            response = requests.get(
                GET_ORDER_BY_TRACK_URL,
                params={'t': created_order}
            )

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 200
            assert 'order' in response.json()
            assert isinstance(response.json()['order'], dict)

    @allure.title('Нельзя получить заказ без трек-номера')
    def test_get_order_without_track(self):
        with allure.step('Отправить запрос без query-параметра t'):
            response = requests.get(GET_ORDER_BY_TRACK_URL)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 400
            assert response.json() == NOT_ENOUGH_SEARCH_DATA_RESPONSE

    @allure.title('Нельзя получить заказ по несуществующему трек-номеру')
    def test_get_order_with_nonexistent_track(self):
        with allure.step('Передать несуществующий трек-номер'):
            response = requests.get(
                GET_ORDER_BY_TRACK_URL,
                params={'t': NONEXISTENT_ID}
            )

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == ORDER_NOT_FOUND_RESPONSE
