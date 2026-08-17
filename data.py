ORDER_DATA = {
    'firstName': 'Naruto',
    'lastName': 'Uchiha',
    'address': 'Konoha, 142 apt.',
    'metroStation': 4,
    'phone': '+7 800 355 35 35',
    'rentTime': 5,
    'deliveryDate': '2026-08-10',
    'comment': 'Saske, come back to Konoha'
}

SUCCESS_RESPONSE = {'ok': True}

COURIER_ALREADY_EXISTS_RESPONSE = {
    'code': 409,
    'message': 'Этот логин уже используется. Попробуйте другой.'
}

NOT_ENOUGH_CREATE_DATA_RESPONSE = {
    'code': 400,
    'message': 'Недостаточно данных для создания учетной записи'
}

NOT_ENOUGH_LOGIN_DATA_RESPONSE = {
    'code': 400,
    'message': 'Недостаточно данных для входа'
}

COURIER_NOT_FOUND_RESPONSE = {
    'code': 404,
    'message': 'Учетная запись не найдена'
}

NOT_ENOUGH_DELETE_DATA_RESPONSE = {
    'code': 400,
    'message': 'Недостаточно данных для удаления курьера'
}

COURIER_ID_NOT_FOUND_RESPONSE = {
    'code': 404,
    'message': 'Курьера с таким id нет.'
}

NOT_ENOUGH_SEARCH_DATA_RESPONSE = {
    'code': 400,
    'message': 'Недостаточно данных для поиска'
}

COURIER_ID_DOES_NOT_EXIST_RESPONSE = {
    'code': 404,
    'message': 'Курьера с таким id не существует'
}

ORDER_ID_DOES_NOT_EXIST_RESPONSE = {
    'code': 404,
    'message': 'Заказа с таким id не существует'
}

ORDER_NOT_FOUND_RESPONSE = {
    'code': 404,
    'message': 'Заказ не найден'
}

NONEXISTENT_ID = 999999999
