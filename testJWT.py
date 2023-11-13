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

import hashlib, uuid
salt = uuid.uuid4().hex
if __name__ == '__main__':
    salt = "5034818909694aeaffbcc4a39abd3e54f0890a11a4b02ff0e097d5644bbf7037"
    password = "test"
    print(hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest())


#if __name__ == '__main__':
#    bearerToken = login().json()["access_token"]
#    print(test_jwt(bearerToken).json())

