import allure
import pytest
import requests

from data import ORDER_DATA
from urls import CREATE_ORDER_URL


@allure.feature('Заказы')
@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ можно создать с разными вариантами цвета')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            None
        ],
        ids=['black', 'grey', 'black_and_grey', 'without_color']
    )
    def test_create_order_with_different_colors(self, color):
        with allure.step('Подготовить данные заказа'):
            payload = ORDER_DATA.copy()
            if color is not None:
                payload['color'] = color

        with allure.step('Отправить запрос на создание заказа'):
            response = requests.post(CREATE_ORDER_URL, json=payload)

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 201
            assert 'track' in response.json()
            assert response.json()['track'] is not None
            assert response.json()['track'] != ''
