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
        quests = DBController.get_all_quests_from_user_id_db(user)
        erg = []
        for quest in quests:
            erg.append(quest.__dict__())
        return erg

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/add', methods=["POST"])
    def add_quest():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        name = body["name"]
        is_active = bool(body["isActive"])
        resource = body["resource"]
        items_per_capacity = body["itemsPerCapacity"]
        demand = body["demand"]
        id = body["id"]
        if DBController.create_quest_db(user, name, id, is_active, resource, items_per_capacity, demand):
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 409

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/update', methods=["POST"])
    def update_quest():
        user = UtilityFunctions.get_user_from_jwt(request)
        print(request.json)
        body = request.get_json()
        name = body["name"]
        is_active = bool(body["isActive"])
        resource = body["resource"]
        items_per_capacity = body["itemsPerCapacity"]
        demand = body["demand"]
        id = body["id"]
        if DBController.update_quest_db(user, name, id, is_active, resource, items_per_capacity, demand):
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 409

    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('/delete', methods=["POST"])
    def delete_quest():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        id = body["id"]
        if DBController.delete_quest_db(user, id):
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 409
