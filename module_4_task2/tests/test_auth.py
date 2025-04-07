from module_4_task2.config.constants import BASE_URL, AUTH_DATA

class TestAuth:
    """
    Набор тестов для проверки авторизации и валидации токена пользователя.
    """
    def test_token(self, auth_session):
        """
        Проверяет, что действительный токен проходит аутентификацию.
        :param auth_session:
        Checks:
        - Отправляет POST-запрос на эндпоинт /login/test-token с валидным токеном.
        - Проверяет, что статус-код ответа — 200 или 201.
        - Проверяет, что в теле ответа:
            - пользователь активен (is_active = True)
            - email совпадает с переданными данными авторизации
            - id пользователя совпадает с ожидаемым.
        """
        response = auth_session.post(f'{BASE_URL}/api/v1/login/test-token')
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.json()['is_active'] == True, 'Состояние пользователя != true'
        assert response.json()['email'] == AUTH_DATA['username'], 'email не соответствует'
        assert response.json()['id'] == AUTH_DATA['client_id'], 'id не соответствует'


    def test_invalid_token(self, auth_session_without_token):
        """
        Проверяет, что при отсутствии токена запрос не проходит аутентификацию.
        Checks:
        - Отправляет POST-запрос на эндпоинт /login/test-token без токена.
        - Проверяет, что возвращённый статус-код не 200/201.
        - Ожидаемый статус — 401 Unauthorized.
        - Проверяет, что сообщение об ошибке — 'Not authenticated'.
        """
        response = auth_session_without_token.post(f'{BASE_URL}/api/v1/login/test-token')
        assert response.status_code not in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert response.status_code == 401, f"Response: {response.status_code}, {response.text}"
        assert response.json()['detail'] == 'Not authenticated', 'Неверное описание ошибки'