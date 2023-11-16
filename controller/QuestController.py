from flask_jwt_extended import jwt_required
from flask import request, jsonify, Blueprint
from instance import DBController
from utils.utility_functions import UtilityFunctions

quest_controller = Blueprint('quest_controller', __name__, url_prefix='/quest')



class QuestController:
    def __init__(self,app):
        app.register_blueprint(quest_controller)


    @staticmethod
    @jwt_required()
    @quest_controller.route('/get')
    def get_quest():
        id = request.args.get("id")
        return DBController.get_quest_db(id).dict()

    @staticmethod
    @jwt_required()
    @quest_controller.route('/list')
    def get_quests():
        user = UtilityFunctions.get_user_from_jwt(request)
        quests = DBController.get_all_quests_from_user_id_db(user)
        erg = []
        for quest in quests:
            erg.append(quest.dict())
        return erg

    @staticmethod
    @jwt_required()
    @quest_controller.route('/add', methods=["POST"])
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
    @quest_controller.route('/update', methods=["POST"])
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
    @quest_controller.route('/delete', methods=["POST"])
    def delete_quest():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        id = body["id"]
        if DBController.delete_quest_db(user, id):
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 409
