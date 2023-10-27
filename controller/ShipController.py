from controller.BaseController import BaseController
from flask import request, jsonify


class ShipController(BaseController, base_route="/ship"):
    @staticmethod
    @BaseController.controllerRoute(rule='/list', methods=['GET'])
    def list():
        return jsonify({"msg": "List Ships"}), 200
