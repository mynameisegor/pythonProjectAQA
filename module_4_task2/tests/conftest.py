from typing import Generator, Callable, Tuple, Dict, Any

import pytest
from requests import Session
from module_4_task2.config.constants import AUTH_HEADERS, BASE_URL, AUTH_DATA, API_HEADERS
from faker import Faker

fake = Faker()
endpoint = f"{BASE_URL}/api/v1/items/"


@pytest.fixture(scope='session')
def auth_session() -> Session:
    """Фикстура для создания авторизованной сессии.

    Returns:
        Session: Авторизованная HTTP-сессия с токеном доступа

    Raises:
        AssertionError: Если аутентификация не удалась или токен не получен
    """
    session = Session()

    # Аутентификация
    auth_response = session.post(
        f"{BASE_URL}/api/v1/login/access-token",
        data=AUTH_DATA,
        headers=AUTH_HEADERS
    )
    assert auth_response.status_code == 200, (
        f"Ошибка аутентификации: {auth_response.status_code}, {auth_response.text}"
    )

    # Получение токена
    token = auth_response.json().get("access_token")
    assert token, "Токен доступа не получен в ответе"

    # Настройка заголовков сессии
    session.headers.update({
        **API_HEADERS,
        "Authorization": f"Bearer {token}"
    })

    return session


@pytest.fixture(scope='function')
def auth_session_without_token() -> Session:
    """Фикстура для создания неавторизованной сессии (без токена).

    Returns:
        Session: HTTP-сессия без авторизационных заголовков
    """
    session = Session()
    session.headers.update(API_HEADERS)
    return session


@pytest.fixture
def generate_item_data()-> Callable[[], dict[str, str | Any]]:
    """
    Фикстура для генерации тестовых данных элемента.

    Returns:
        function: Функция, возвращающая словарь с тестовыми данными
    """

    def generate():
        return {
            "title": fake.word().capitalize(),
            "description": fake.sentence(nb_words=10)
        }

    return generate


@pytest.fixture()
def create_item(auth_session: Session, generate_item_data: Callable[[], Dict[str, str]]) -> Tuple[Any, Dict[str, str]]:
    """Фикстура для создания тестового элемента.

    Args:
        auth_session: Фикстура авторизованной сессии
        generate_item_data: Фикстура генерации тестовых данных

    Returns:
        tuple: (response, data) - ответ сервера и использованные данные

    Raises:
        AssertionError: Если создание элемента не удалось
    """
    data = generate_item_data()
    response = auth_session.post(endpoint, json=data)

    assert response.status_code in (200, 201), (
        f"Ошибка создания элемента: {response.status_code}, {response.text}"
    )

    return response, data


@pytest.fixture()
def cleanup_items(auth_session: Session) -> Generator[None, None, None]:
    """Фикстура для очистки всех элементов до и после теста.
    Args:
        auth_session: Фикстура авторизованной сессии
    """

    # Удаление всех существующих элементов перед тестом
    get_response = auth_session.get(endpoint)
    assert get_response.status_code == 200, (
        f"Ошибка получения списка элементов: {get_response.text}"
    )

    for item in get_response.json().get('data', []):
        item_id = item['id']
        del_response = auth_session.delete(f"{endpoint}{item_id}")
        assert del_response.status_code in (200, 204), (
            f"Ошибка удаления элемента {item_id}: {del_response.text}"
        )

    final_check = auth_session.get(endpoint)
    assert len(final_check.json().get("data", [])) == 0, (
        "Не все элементы были удалены перед тестом"
    )

    yield

    # Удаление всех элементов после теста
    get_response = auth_session.get(endpoint)
    if get_response.status_code == 200:  # Проверяем только если запрос успешен
        for item in get_response.json().get('data', []):
            item_id = item['id']
            auth_session.delete(f"{endpoint}{item_id}")
