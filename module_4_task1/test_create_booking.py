from constant import base_url

class TestBooking:

    def test_create_check_delete_booking(self, auth_session, create_booking, booking_data):
        create_response = create_booking
        booking_id = create_response.get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"
        print(create_response)
        assert create_response["booking"]["firstname"] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert create_response["booking"]["lastname"] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert create_response["booking"]["totalprice"] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert create_response["booking"][
                   "additionalneeds"] == "Cigars", "Дополнительные потребности не совпадают с заданными"

        get_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_response.status_code == 200, f"Ошибка при получении букинга с ID {booking_id}"

        delete_response = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        check_delete_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Букинг с ID {booking_id} не был удален"


    def test_create_without_required_fields(self, auth_session, booking_data):
        """Проверка создания бронирования без обязательных полей.
            Тест последовательно пытается создать бронирование, удаляя каждое из обязательных полей.
            Ожидается, что API вернет ошибку (status_code 500) при отсутствии любого обязательного поля.
            Args:
                auth_session (requests.Session): Авторизованная сессия для отправки запросов.
                booking_data (dict): Данные для создания бронирования (фикстура).
            Steps:
                1. Для каждого обязательного поля:
                   - Создается копия booking_data без текущего поля.
                   - Отправляется POST-запрос на создание бронирования.
                2. Проверяется, что статус ответа 500.
            """
        fields = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
        for i in fields:
            res_data = booking_data.copy()
            del res_data[i]
            res = auth_session.post(f"{base_url}/booking", json=res_data)
            assert res.status_code == 500, 'Ошибка! Запись с обязательным полем создалась'

    def test_update_delete_booking(self, auth_session, create_booking, update_booking_data):
        """
        Проверка метода для обновления брони - позитивный кейс
        :param auth_session: созданние сессии с токеном авторизации в куках
        :param create_booking: создание брони
        :param update_booking_data: запрос для обновления брони
        """
        booking_id = create_booking.get("bookingid")
        update_response = auth_session.put(f'{base_url}/booking/{booking_id}', json = update_booking_data)
        assert update_response.status_code == 200, 'Ошибка при обновлении'
        assert update_response.json().get('firstname') == update_booking_data['firstname'], 'Имя не совпадает с заданным'
        assert update_response.json().get("lastname") == update_booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert update_response.json().get("totalprice") == update_booking_data['totalprice'], "Цена не совпадает с заданной"
        assert update_response.json().get(
                   "additionalneeds") == update_booking_data['additionalneeds'], "Дополнительные потребности не совпадают с заданными"
        """Удаление брони и проверка что удалилось"""
        delete_response = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        check_delete_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Букинг с ID {booking_id} не был удален"


    def test_update_without_token(self, auth_session_without_token, create_booking, update_booking_data):
        """Проверка обновления бронирования без авторизационного токена.
            Тест проверяет, что API возвращает ошибку 403 при попытке обновления бронирования
            без передачи валидного токена авторизации.
            Args:
                auth_session_without_token (requests.Session): Сессия без авторизационного токена.
                create_booking (dict): Фикстура с созданным бронированием (содержит bookingid).
                update_booking_data (dict): Данные для обновления бронирования.
            Steps:
                1. Получает bookingid созданного бронирования.
                2. Отправляет PUT-запрос на обновление без токена авторизации.
                3. Проверяет, что статус ответа 403.
            """
        booking_id = create_booking.get("bookingid")
        update_response = auth_session_without_token.put(f'{base_url}/booking/{booking_id}', json=update_booking_data)
        print(auth_session_without_token.headers)
        assert update_response.status_code == 403, 'Формат ошибки отличается от ожидаемого'


    def test_partial_update_booking_res(self, auth_session, create_booking, booking_data, part_req_data):
        """
           Тестирование частичного обновления данных бронирования (PATCH-запрос) с проверкой ответа.
           Проверяет:
           1. Успешность обновления (status code 200)
           2. Корректность обновленных полей в ответе (firstname, lastname, totalprice)
           3. Сохранение неизмененных полей в ответе (depositpaid, bookingdates, additionalneeds)
           4. Последующее удаление бронирования с проверкой:
              - Успешность удаления (status code 201)
              - Фактическое отсутствие бронирования после удаления (status code 404)
           Args:
               auth_session: Авторизованная сессия для запросов
               create_booking: Фикстура создания тестового бронирования
               booking_data: Исходные данные бронирования
               part_req_data: Данные для частичного обновления
           """
        booking_id = create_booking.get("bookingid")
        req_update = auth_session.patch(f'{base_url}/booking/{booking_id}', json=part_req_data)

        assert req_update.status_code == 200, 'Ошибка при обновлении'
        assert req_update.json().get('firstname') == part_req_data['firstname'], 'Имя не совпадает с заданным'
        assert req_update.json().get("lastname") == part_req_data['lastname'], "Фамилия не совпадает с заданной"
        assert req_update.json().get("totalprice") == part_req_data['totalprice'], "Цена не совпадает с заданной"
        assert req_update.json().get("depositpaid") == booking_data['depositpaid'], "Не совпадает depositpaid"
        assert req_update.json().get("bookingdates") == booking_data['bookingdates'], "Не совпадает bookingdates"
        assert (req_update.json().get("additionalneeds") ==
                booking_data['additionalneeds']), "Дополнительные потребности не совпадают с заданными"

        delete_response = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        check_delete_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Букинг с ID {booking_id} не был удален"


    def test_get_after_partial_update(self, auth_session, create_booking, part_req_data, booking_data):
        """
            Тестирование получения данных бронирования после частичного обновления.
            Проверяет:
            1. Успешность обновления (status code 200)
            2. Корректность объединенных данных при GET-запросе:
               - Обновленные поля должны содержать новые значения
               - Неизмененные поля должны сохранить исходные значения
            3. Структура ответа должна соответствовать полному набору данных бронирования
            Args:
                auth_session: Авторизованная сессия для запросов
                create_booking: Фикстура создания тестового бронирования
                part_req_data: Данные для частичного обновления
                booking_data: Исходные данные бронирования (для проверки неизмененных полей)
            """

        booking_id = create_booking.get("bookingid")
        req_update = auth_session.patch(f'{base_url}/booking/{booking_id}', json=part_req_data)
        assert req_update.status_code == 200, 'Ошибка при обновлении'

        get_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        check_data = booking_data
        check_data['firstname'] = part_req_data['firstname']
        check_data['lastname'] = part_req_data['lastname']
        check_data['totalprice'] = part_req_data['totalprice']
        print(get_response.text)
        assert get_response.status_code == 200, f"Ошибка при получении букинга с ID {booking_id}"
        assert get_response.json() == check_data


    def test_get_all_items(self, auth_session, booking_data):
        """Проверка создания, получения и удаления нескольких бронирований.
            Тест выполняет следующие шаги:
            1. Создает 10 бронирований через API и сохраняет их `bookingid`.
            2. Проверяет, что список бронирований не пуст.
            3. Запрашивает все бронирования через GET-запрос.
            4. Проверяет, что все созданные `bookingid` присутствуют в ответе.
            5. Удаляет каждое бронирование и проверяет, что они больше не доступны.

            Args:
                auth_session (requests.Session): Авторизованная сессия для HTTP-запросов.
                booking_data (dict): Данные для создания бронирования (фикстура).
            """
        booking_ids = [auth_session.post(f"{base_url}/booking", json=booking_data).json().get('bookingid') for _ in range(10)]
        assert len(booking_ids) != 0, 'Ошибка генерации броней'
        data = auth_session.get(f'{base_url}/booking')
        assert data.status_code == 200, 'Ошибка получения списка броней'
        counter = 0
        check_data = []
        for i in data.json():
            if i['bookingid'] in booking_ids:
                check_data.append(i['bookingid'])
                counter += 1
        assert counter == len(booking_ids), 'Ошибка! Кол-во созданных элементов не соответствует кол-ву в ответе'
        assert check_data.sort() == booking_ids.sort(), "Ошибка! bookingid's в ответе не соответствуют созданным"

        for i in booking_ids:
            delete_response = auth_session.delete(f"{base_url}/booking/{i}")
            assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {i}"
            check_delete_response = auth_session.get(f"{base_url}/booking/{i}")
            assert check_delete_response.status_code == 404, f"Букинг с ID {i} не был удален"




