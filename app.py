from flask import request, jsonify
from flask_cors import CORS
from _DatabaseCall import app
from controller import LoginController, ShipController, QuestController, SolveController
from flask_jwt_extended import (
    JWTManager, jwt_required
)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.config["JWT_TOKEN_LOCATION"] = ["headers"]

app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "cf65d36897822be9be6afe519020fbfc111676854c4778d62ceca2af46e1ef47"

jwt = JWTManager(app)

login_controller = LoginController.LoginController()
ship_controller = ShipController.ShipController()
quest_controller = QuestController.QuestController()
solve_controller = SolveController.SolveController()

@app.route('/isAlive')
def is_alive():
    return jsonify({"msg": "Alive"}), 200


if __name__ == '__main__':
    app.run()
