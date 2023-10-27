from flask import request,jsonify
from flask_cors import CORS
from _DatabaseCall import app
from instance import DBController
from controller import LoginController

from flask_jwt_extended import (
    JWTManager
)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.config["JWT_TOKEN_LOCATION"] = ["headers"]

app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "cf65d36897822be9be6afe519020fbfc111676854c4778d62ceca2af46e1ef47"

jwt = JWTManager(app)

login_controller = LoginController.LoginController()



@app.route('/getShip')
def get_ship():
    id = request.args.get("id")
    return DBController.get_ship_db(id).__dict__()







@app.route('/getShips')
def get_all_ships():
    ships = DBController.get_all_ships_db()
    erg = []
    for ship in ships:
        erg.append(ship.__dict__())
    return erg


@app.route('/addShip')
def add_ship():
    user = request.args.get("user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return DBController.create_ship_db(user, name, id, is_active, capacity)


@app.route('/updateShip')
def update_ship():
    user = request.args.get("user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return DBController.update_ship_db(user, name, id, is_active, capacity)


@app.route('/deleteShip')
def delete_ship():
    id = request.args.get("id")
    return DBController.delete_ship_db(id)


@app.route('/getQuest')
def get_quest():
    id = request.args.get("id")
    return DBController.get_quest_db(id).__dict__()


@app.route('/getQuests')
def get_quests():
    ships = DBController.get_all_quests_db()
    erg = []
    for ship in ships:
        erg.append(ship.__dict__())
    return erg


@app.route('/addQuest')
def add_quest():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    resource = request.args.get("resource")
    items_per_capacity = request.args.get("items_per_capacity")
    demand = request.args.get("demand")
    id = request.args.get("id")
    return DBController.create_quest_db(user, name, id, is_active, resource, items_per_capacity, demand)


@app.route('/updateQuest')
def update_quest():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    resource = request.args.get("resource")
    items_per_capacity = request.args.get("items_per_capacity")
    demand = request.args.get("demand")
    id = request.args.get("id")
    return DBController.update_quest_db(user, name, id, is_active, resource, items_per_capacity, demand)


@app.route('/deleteQuest')
def delete_quest():
    id = request.args.get("id")
    return DBController.delete_quest_db(id)


@app.route('/getUser')
def get_user():
    id = request.args.get("id")
    return DBController.get_user_db(id).__dict__()


@app.route('/getUsers')
def get_all_users():
    users = DBController.get_all_users_db()
    erg = []
    for user in users:
        erg.append(user.__dict__())
    return erg


@app.route('/addUser')
def add_user():
    name = request.args.get("name")
    id = request.args.get("id")
    return DBController.create_user_db(name, id)


@app.route('/updateUser')
def update_user():
    name = request.args.get("name")
    id = request.args.get("id")
    return DBController.update_user_db(name, id)


@app.route('/deleteUser')
def delete_user():
    id = request.args.get("id")
    return DBController.delete_user_db(id)

@app.route('/isAlive')
def is_alive():
    return jsonify({"msg": "Alive"}), 200


if __name__ == '__main__':
    app.run()
