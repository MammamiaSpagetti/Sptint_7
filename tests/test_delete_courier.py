import allure
import requests

from data import (
    COURIER_ID_NOT_FOUND_RESPONSE,
    NONEXISTENT_ID,
    NOT_ENOUGH_DELETE_DATA_RESPONSE,
    SUCCESS_RESPONSE
)
from urls import DELETE_COURIER_URL, DELETE_COURIER_WITHOUT_ID_URL


@allure.feature('Курьер')
@allure.story('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Курьера можно успешно удалить')
    def test_delete_courier_success(self, courier_id):
        with allure.step('Отправить запрос на удаление курьера'):
            response = requests.delete(
                DELETE_COURIER_URL.format(courier_id=courier_id)
            )

        with allure.step('Проверить код и тело ответа'):
            assert response.status_code == 200
            assert response.json() == SUCCESS_RESPONSE

    @allure.title('Нельзя удалить курьера без id')
    def test_delete_courier_without_id(self):
        with allure.step('Отправить запрос на удаление без id курьера'):
            response = requests.delete(DELETE_COURIER_WITHOUT_ID_URL)

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 400
            assert response.json() == NOT_ENOUGH_DELETE_DATA_RESPONSE

    @allure.title('Нельзя удалить курьера с несуществующим id')
    def test_delete_courier_with_nonexistent_id(self):
        with allure.step('Отправить запрос с несуществующим id курьера'):
            response = requests.delete(
                DELETE_COURIER_URL.format(courier_id=NONEXISTENT_ID)
            )

        with allure.step('Проверить код и тело ошибки'):
            assert response.status_code == 404
            assert response.json() == COURIER_ID_NOT_FOUND_RESPONSE
