from flask import request, jsonify
from instance.authService import AuthService
from flask import Blueprint

from flask_jwt_extended import (
    #JWTManager,
    jwt_required,
    create_access_token
)

login_controller = Blueprint('login_controller', __name__, url_prefix='/auth')




class LoginController:
    def __init__(self, app):
        app.register_blueprint(login_controller)


    @staticmethod
    @login_controller.route('/login', methods=['POST'])
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
    @login_controller.route(rule='/test', methods=['GET'])
    def test():
        return jsonify({"msg": "Custom Controller"}), 200

    ## curl -X POST http://127.0.0.1:5000/register -d "{\"username\":\"test\", \"password\":\"test\"}" -H "Content-Type: application/json"
    @staticmethod
    @login_controller.route(rule='/register', methods=['POST'])
    def register():
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if AuthService.username_exists(username):
            return jsonify({"msg": "User already exists"}), 409
        user = AuthService().create_user(username, password)
        access_token = create_access_token(identity=user.name)
        return jsonify(access_token=access_token), 200

    @staticmethod
    @login_controller.route(rule='/test_jwt', methods=['GET'])
    @jwt_required()
    def is_jwt_working():
        return jsonify({"msg": "Test JWT Works"}), 200

