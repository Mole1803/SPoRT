import requests

username = "test"
password = "test"



def register_user():
    return requests.post("http://127.0.0.1:5000/auth/register", json={"username": username, "password": password})


def login():
    return requests.post("http://127.0.0.1:5000/auth/login", json={"username": username, "password": password})


def test_jwt(bearerToken):
    print(bearerToken)
    return requests.get("http://127.0.0.1:5000/auth/test_jwt", headers={"Authorization": "Bearer "+bearerToken})


if __name__ == '__main__':
    bearerToken = login().json()["access_token"]
    print(test_jwt(bearerToken).json())

