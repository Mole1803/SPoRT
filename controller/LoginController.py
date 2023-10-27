from flask import request, jsonify
from instance.authService import AuthService
from app import app
from controller.BaseController import BaseController

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)

import jwt as jwt_lib

jwt = JWTManager(app)




class LoginController(BaseController, base_route="/auth"):
    @staticmethod
    @BaseController.controllerRoute(rule='/login', methods=['POST'])
    def login():
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user = AuthService().verify_user(username, password)
        if not user:
            return jsonify({"msg": "Bad username or password"}), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    # curl -X POST http://127.0.0.1:5000/auth/login -d "{\"username\":\"test\", \"password\":\"test\"}" -H "Content-Type: application/json"
    @staticmethod
    @BaseController.controllerRoute(rule='/test', methods=['GET'])
    def test():
        return jsonify({"msg": "Custom Controller"}), 200

    ## curl -X POST http://127.0.0.1:5000/register -d "{\"username\":\"test\", \"password\":\"test\"}" -H "Content-Type: application/json"
    @staticmethod
    @BaseController.controllerRoute(rule='/register', methods=['POST'])
    def register():
        print(request.json, flush=True)
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user = AuthService().create_user(username, password)
        access_token = create_access_token(identity=user.name)
        return jsonify(access_token=access_token), 200

    @staticmethod
    @BaseController.controllerRoute(rule='/test_jwt', methods=['GET'])
    @jwt_required()
    def is_jwt_working():
        return jsonify({"msg": "Test JWT Works"}), 200

    @staticmethod
    def get_user_from_jwt(_request):
        token = _request.headers.get("Authorization")[7::]
        return jwt_lib.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])["sub"]
