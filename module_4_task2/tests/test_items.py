import pytest
from module_4_task2.config.constants import BASE_URL
class TestItems:
    """Класс тестов для работы с элементами (items) через API.
    Содержит тесты создания, чтения, обновления и удаления элементов,
    а также проверки валидации данных и пагинации.
    """
    endpoint = f"{BASE_URL}/api/v1/items/"
    long_str = 'aB3#kL9@xZ2!pQ5*eR8$yU1%vI4^oP7&wT0(nM6)jH9_gF4+dS5=lK3;zX7:cV2?mN8<bY0>qC1,rD6.sJ2/tA4|hG7\kE9[fO3]iW5~nB0'


    def test_create_item(self, auth_session, create_item):
        """Тест успешного создания элемента.
        Args:
            auth_session: Фикстура с авторизованной сессией.
            create_item: Фикстура, создающая тестовый элемент (возвращает response и данные).
        Checks:
            - Ответ содержит ID созданного элемента.
            - Поля title и description в ответе соответствуют переданным.
        """
        item_data = create_item[1]
        res_data = create_item[0].json()
        item_id = res_data.get("id")
        assert item_id is not None
        assert res_data.get("title") == item_data["title"]
        assert res_data.get("description") == item_data["description"]


    @pytest.mark.parametrize(('title', 'description'), ((12, True), ('', long_str), (long_str, 12), ([1,2],
                                                                                                        (1, 2, 3))))
    def test_create_invalid_item(self, auth_session, title, description):
        """Тест создания элемента с невалидными данными.
                Args:
                    auth_session: Фикстура с авторизованной сессией.
                    title: Невалидный title (число, пустая строка, список и т.д.).
                    description: Невалидное description (булево, число, кортеж и т.д.).
                Checks:
                    - Статус ответа 422 (Unprocessable Entity).
                    - Сообщение об ошибке соответствует типу невалидных данных.
                    - Элемент не появляется в GET-запросе.
                """
        data = {'title': title, 'description': description}
        response = auth_session.post(self.endpoint, json=data)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 422, 'Вернулась другая ошибка, вместо 422'
        if data['title'] != '':
            assert response.json()['detail'][0]['msg'] == 'Input should be a valid string', 'Текст ошибки не соответствует'
        else:
            assert response.json()['detail'][0]['msg'] == 'String should have at least 1 character', 'Текст ошибки не соответствует'

        # Проверим, что созданных элементов нет в ответе get метода
        response = auth_session.get(self.endpoint)
        check_data = response.json()['data'][0].get(str(title))
        assert not check_data, 'В ответе get метода появилась запись, которая не должна создаться'


    def test_create_get_delete_item_without_token(self, auth_session_without_token, generate_item_data, create_item):
        """Тест доступа без токена.
                Args:
                    auth_session_without_token: Фикстура с сессией без авторизации.
                    generate_item_data: Фикстура для генерации тестовых данных.
                    create_item: Фикстура для создания элемента.
                Checks:
                    - Все операции (POST, GET, DELETE) возвращают 401.
                    - Сообщение об ошибке: 'Not authenticated'.
                """
        data = generate_item_data()
        response = auth_session_without_token.post(self.endpoint, json=data)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 401, 'Вернулась другая ошибка, вместо 401'

        # проверяем, что метод гет также не работает без токена
        response = auth_session_without_token.get(self.endpoint)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 401, 'Вернулась другая ошибка, вместо 401'
        assert response.json()['detail'] == 'Not authenticated', 'Текст ошибки не соответствует'

    #   Проверяем, что удаление не работает без токена
        item_id = create_item[0].json().get('id')
        assert item_id, 'Ошибка! item не создан'
        response = auth_session_without_token.delete(self.endpoint+item_id)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 401, 'Вернулась другая ошибка, вместо 401'
        assert response.json()['detail'] == 'Not authenticated', 'Текст ошибки не соответствует'



    def test_update_item(self, generate_item_data, create_item, auth_session):
        """Тест обновления элемента.
        Args:
            generate_item_data: Фикстура для генерации тестовых данных.
            auth_session: Фикстура с авторизованной сессией.
        Checks:
            - Статус ответа 200/201 после обновления.
            - Поля в ответе соответствуют обновленным данным.
        """
        item_id = create_item[0].json().get("id")
        data = generate_item_data()
        response = auth_session.put(self.endpoint+item_id, json=data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert item_id == response.json().get('id'), 'id в ответе не соответствует'
        assert data['title'] == response.json().get('title'), 'title в ответе не соответствует'
        assert data['description'] == response.json().get('description'), 'description в ответе не соответствует'


    def test_update_item_get(self, generate_item_data, create_item, auth_session):
        """Тест проверки обновления через GET-запрос.
         Args:
             generate_item_data: Фикстура для генерации тестовых данных.
             auth_session: Фикстура с авторизованной сессией.
         Checks:
             - Данные в детальном просмотре (GET) соответствуют обновленным.
         """
        item_id = create_item[0].json().get("id")
        data = generate_item_data()
        response = auth_session.put(self.endpoint+item_id, json=data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert item_id == response.json().get('id'), 'id в ответе не соответствует'

        # проверяем, что в деталке данные обновились
        response = auth_session.get(self.endpoint+item_id)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert item_id == response.json().get('id'), 'id в ответе деталки не соответствует'
        assert data['title'] == response.json().get('title'), 'title в ответе деталки не соответствует'
        assert data['description'] == response.json().get('description'), 'description в ответе деталки не соответствует'


    @pytest.mark.parametrize(('title', 'description'), ((12, True), (False, long_str), (long_str, 12), ([1,2],
                                                                                                        (1, 2, 3))))
    def test_update_item_incorrect_data(self, auth_session, create_item, title, description):
        """Тест обновления элемента с невалидными данными.
        Args:
            auth_session: Фикстура с авторизованной сессией.
            create_item: Фикстура для создания элемента.
            title: Невалидный title.
            description: Невалидное description.
        Checks:
            - Статус ответа 422.
            - Элемент не обновляется в GET-запросе.
        """
        response = create_item[0]
        data = {'title': title, 'description': description}
        item_id = response.json().get("id")
        response = auth_session.put(self.endpoint + item_id, json=data)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 422, 'Вернулась другая ошибка, вместо 422'
        assert response.json()['detail'][0]['msg'] == 'Input should be a valid string', 'Текст ошибки не соответствует'

        # Проверим, что обновленных элементов нет в ответе get метода
        response = auth_session.get(self.endpoint)
        check_data = response.json()['data'][0].get(str(title))
        assert not check_data, 'В ответе get метода появилась обновленная запись, которая не должна обновится'


    def test_update_invalid_item(self, generate_item_data, auth_session):
        """Тест обновления несуществующего элемента.
        Args:
            generate_item_data: Фикстура для генерации тестовых данных.
            auth_session: Фикстура с авторизованной сессией.
        Checks:
            - Статус ответа 404.
            - Сообщение об ошибке: 'Item not found'.
        """
        invalid_id = 'e0ba54b8-b58c-4afa-9f9b-000000000000'
        data = generate_item_data()
        response = auth_session.put(self.endpoint+invalid_id, json=data)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 404, 'Вернулась другая ошибка, вместо 404'
        assert response.json()['detail'] == 'Item not found', 'Текст ошибки не соответствует'


    def test_get_items_pagination(self, cleanup_items, generate_item_data, auth_session):
        """Тест пагинации элементов.
                Args:
                    cleanup_items: Фикстура для очистки элементов после теста.
                    generate_item_data: Фикстура для генерации тестовых данных.
                    auth_session: Фикстура с авторизованной сессией.
                Checks:
                    - Элементы корректно разбиваются на страницы (skip/limit).
                    - Страницы не пересекаются.
                    - Порядок элементов соответствует ожидаемому.
                """
        data_list = []
        for _ in range(20):
            data = generate_item_data()
            response = auth_session.post(self.endpoint, json=data)
            data_list.append(response.json().get('id'))
            assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        page1 = auth_session.get(self.endpoint, params={"skip": 0, "limit": 10})
        assert page1.status_code == 200, f"Response: {page1.status_code}, {page1.text}"
        page2 = auth_session.get(self.endpoint, params={"skip": 10, "limit": 10})
        assert page2.status_code == 200, f"Response: {page2.status_code}, {page2.text}"

        # Проверяем кол-во элементов на странице
        assert len(page1.json().get('data')) == 10, "Число элементов на странице не соответствует"
        assert len(page2.json().get('data')) == 10, "Число элементов на странице не соответствует"

        # Проверяем что страницы не пересекаются и имеют правильный порядок
        page1_ids = [item['id'] for item in page1.json()['data']]
        page2_ids = [item["id"] for item in page2.json()['data']]
        assert  sorted(page1_ids) == sorted(data_list[0:10]), "Порядок элементов на 1 странице не соответствует"
        assert sorted(page2_ids) == sorted(data_list[10:20]), "Порядок элементов на 2 странице не соответствует"
        assert set(page1_ids).isdisjoint(set(page2_ids)), "Страницы содержат одинаковые элементы"


    def test_get_items_structure(self, auth_session):
        """Тест структуры ответа для списка элементов.
                Args:
                    auth_session: Фикстура с авторизованной сессией.
                Checks:
                    - Ответ содержит обязательные поля: data, count.
                    - Элементы в data содержат все обязательные поля.
                    - Типы полей соответствуют ожидаемым.
                """
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert "count" in data, "Response missing 'count' key"
        assert "id" in data["data"][0], "Response missing 'id' key"
        assert "owner_id" in data["data"][0], "Response missing 'owner_id' key"
        assert "title" in data["data"][0], "Response missing 'title' key"
        assert "description" in data["data"][0], "Response missing 'description' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"
        assert len(data['data']) == data.get("count")


    def test_delete_invalid_item(self, auth_session):
        """Тест удаления несуществующего элемента.
            Проверяет, что система корректно обрабатывает попытку удаления элемента с несуществующим ID.
            Args:
                auth_session: Фикстура авторизованной HTTP-сессии
            Checks:
                - Запрос возвращает статус 404 (Not Found)
                - Сообщение об ошибке соответствует ожидаемому
                - Запрос не возвращает успешные статусы (200, 201)
            """
        invalid_id = 'e0ba54b8-b58c-4afa-9f9b-000000000000'
        response = auth_session.delete(self.endpoint+invalid_id)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 404, 'Вернулась другая ошибка, вместо 404'
        assert response.json()['detail'] == 'Item not found', 'Текст ошибки не соответствует'


    def test_delete_item_two_times(self, auth_session, create_item):
        """Тест повторного удаления одного и того же элемента.
            Проверяет корректность поведения системы при попытке удалить уже удаленный элемент.
            Args:
                auth_session: Фикстура авторизованной HTTP-сессии
                create_item: Фикстура, создающая тестовый элемент
            Checks:
                - Первое удаление проходит успешно (200/201)
                - Повторное удаление возвращает 404
                - Сообщение об ошибке соответствует ожидаемому
            """
        item_id = create_item[0].json().get("id")
        response = auth_session.delete(self.endpoint + item_id)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        response = auth_session.delete(self.endpoint + item_id)
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 404, 'Вернулась другая ошибка, вместо 404'
        assert response.json()['detail'] == 'Item not found', 'Текст ошибки не соответствует'


    def test_del_all_items(self, auth_session):
        data_list = []
        response = auth_session.get(self.endpoint)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        for i in response.json()['data']:
            data_list.append(i.get('id'))
        for i in data_list:
            response = auth_session.delete(self.endpoint + i)
            assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        get_check_response = auth_session.get(f"{BASE_URL}/api/v1/items/")
        assert len(get_check_response.json().get("data")) == 0, 'Не все данные удалены!'