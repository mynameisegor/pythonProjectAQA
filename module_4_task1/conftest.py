from faker import Faker
from constant import headers, base_url
import requests
import pytest

faker = Faker()


@pytest.fixture(scope='session')
def auth_session():
    session = requests.Session()
    session.headers.update(headers)

    response = requests.post(f"{base_url}/auth", headers=headers,
                             json={"username": "admin", "password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture(scope='function')
def auth_session_without_token():
    session = requests.Session()
    session.headers.update(headers)

    response = requests.post(f"{base_url}/auth", headers=headers,
                             json={"username": "admin", "password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации, статус код не 200"
    return session


@pytest.fixture()
def create_booking(auth_session, booking_data):
    res = auth_session.post(f"{base_url}/booking", json=booking_data)
    assert res.status_code == 200, "Ошибка при создании букинга"
    return res.json()


@pytest.fixture()
def booking_data():
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Cigars"
        }

@pytest.fixture()
def update_booking_data():
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2029-04-05",
                "checkout": "2021-04-08"
            },
            "additionalneeds": "Breakfast"
        }

@pytest.fixture()
def part_req_data():
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
        }

