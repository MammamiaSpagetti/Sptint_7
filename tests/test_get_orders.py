import allure
import requests

from urls import GET_ORDERS_URL


@allure.feature('Заказы')
@allure.story('Получение списка заказов')
class TestGetOrders:

    @allure.title('Можно получить список заказов')
    def test_get_orders_success(self):
        with allure.step('Отправить запрос на получение списка заказов'):
            response = requests.get(GET_ORDERS_URL)

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 200
            assert 'orders' in response.json()
            assert isinstance(response.json()['orders'], list)
