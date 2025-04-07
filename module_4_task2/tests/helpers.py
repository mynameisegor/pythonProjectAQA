# import requests
# from constants import AUTH_DATA
#
# BASE_URL = "https://api.pomidor-stage.ru"
# LOGIN_URL = f"{BASE_URL}/api/v1/login/access-token"
# ITEMS_URL = f"{BASE_URL}/api/v1/items/"
#
# HEADERS = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Accept": "application/json"
# }
#
#
#
# def get_auth_token():
#     response = requests.post(LOGIN_URL, data=AUTH_DATA, headers=HEADERS)
#     assert response.status_code == 200
#     return response.json().get("access_token")
#
# def create_item(title, description, token):
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Accept": "application/json"
#     }
#     data = {
#         "title": title,
#         "description": description
#     }
#     response = requests.post(ITEMS_URL, json=data, headers=headers)
#     assert response.status_code in (200, 201)
#     item = response.json()
#     print(f"{item['title']} (ID: {item['id']})")
#
# if __name__ == "__main__":
#     token = get_auth_token()
#     for i in range(20):
#         create_item(f"Test Item {i}", f"Description {i}", token)

import sys
print(sys.path)
