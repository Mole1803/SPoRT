from flask_jwt_extended import jwt_required
from controller.BaseController import BaseController
from flask import request, jsonify
from instance import DBController
from utils.utility_functions import UtilityFunctions


class QuestController(BaseController, base_route="/quest"):

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/get')
    def get_quest():
        id = request.args.get("id")
        return DBController.get_quest_db(id).__dict__()

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/list')
    def get_quests():
        user = UtilityFunctions.get_user_from_jwt(request)
        ships = DBController.get_all_quests_from_user_id_db(user)
        erg = []
        for ship in ships:
            erg.append(ship.__dict__())
        return erg

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/add')
    def add_quest():
        user = UtilityFunctions.get_user_from_jwt(request)
        name = request.args.get("name")
        is_active = bool(request.args.get("is_active"))
        resource = request.args.get("resource")
        items_per_capacity = request.args.get("items_per_capacity")
        demand = request.args.get("demand")
        id = request.args.get("id")
        return DBController.create_quest_db(user, name, id, is_active, resource, items_per_capacity, demand)

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/update')
    def update_quest():
        user = UtilityFunctions.get_user_from_jwt(request)
        name = request.args.get("name")
        is_active = bool(request.args.get("is_active"))
        resource = request.args.get("resource")
        items_per_capacity = request.args.get("items_per_capacity")
        demand = request.args.get("demand")
        id = request.args.get("id")
        return DBController.update_quest_db(user, name, id, is_active, resource, items_per_capacity, demand)

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/delete')
    def delete_quest():
        id = request.args.get("id")
        return DBController.delete_quest_db(id)
