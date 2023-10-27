from flask_jwt_extended import jwt_required
from controller.BaseController import BaseController
from flask import request, jsonify
from instance import DBController
from utils.utility_functions import UtilityFunctions


class ShipController(BaseController, base_route="/ship"):
    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute(rule='/get')
    def get_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        id = request.args.get("id")
        return DBController.get_ship_db(id, user).__dict__()

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute(rule='/list')
    def get_all_ships():
        user = UtilityFunctions.get_user_from_jwt(request)
        ships = DBController.get_all_ships_from_user_id_db(user)
        erg = []
        for ship in ships:
            erg.append(ship.__dict__())
        return erg

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute(rule='/add')
    def add_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        name = request.args.get("name")
        is_active = bool(request.args.get("is_active"))
        capacity = request.args.get("capacity")
        id = request.args.get("id")
        if DBController.create_ship_db(user, name, id, is_active, capacity):
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 409

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute(rule='/update')
    def update_ship():
        user = UtilityFunctions.get_user_from_jwt(request)
        name = request.args.get("name")
        is_active = bool(request.args.get("is_active"))
        capacity = request.args.get("capacity")
        id = request.args.get("id")
        return DBController.update_ship_db(user, name, id, is_active, capacity)

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/ship/delete')
    def delete_ship():
        id = request.args.get("id")
        return DBController.delete_ship_db(id)

