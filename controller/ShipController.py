from flask_jwt_extended import jwt_required

from flask import request, jsonify, Blueprint
from instance import DBController
from utils.utility_functions import UtilityFunctions

ship_controller = Blueprint('ship_controller', __name__, url_prefix='/ship')

class ShipController:
    def __init__(self,app):
        app.register_blueprint(ship_controller)
    @staticmethod
    @jwt_required()
    @ship_controller.route(rule='/get')
    def get_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        id = request.args.get("id")
        return DBController.get_ship_db(id, user).__dict__()

    @staticmethod
    @jwt_required()
    @ship_controller.route(rule='/list')
    def get_all_ships():
        user = UtilityFunctions.get_user_from_jwt(request)
        ships = DBController.get_all_ships_from_user_id_db(user)
        erg = []
        for ship in ships:
            erg.append(ship.__dict__())
        return erg

    @staticmethod
    @jwt_required()
    @ship_controller.route(rule='/add', methods=["POST"])
    def add_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        name = body["name"]
        is_active = body["is_active"]
        capacity = body["capacity"]
        id = body["id"]
        if DBController.create_ship_db(user, name, id, is_active, capacity):
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 409

    @staticmethod
    @jwt_required()
    @ship_controller.route(rule='/update', methods=["POST"])
    def update_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        print(request.json)
        name = body["name"]
        is_active = body["is_active"]
        capacity = body["capacity"]
        id = body["id"]
        if DBController.update_ship_db(user, name, id, is_active, capacity):
            return jsonify(success=True), 200
        return jsonify(success=False), 204

    @staticmethod
    @jwt_required()
    @ship_controller.route('/delete', methods=["POST"])
    def delete_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        id = body["id"]
        if DBController.delete_ship_db(user, id):
            return jsonify(success=True), 200
        return jsonify(success=False), 204

