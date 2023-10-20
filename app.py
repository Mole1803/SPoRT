from flask import request, jsonify
from flask_cors import CORS
from _DatabaseCall import app
from instance import DBController

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
)
import jwt as jwt_lib
import uuid
import hashlib

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.config["JWT_TOKEN_LOCATION"] = ["headers"]

app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "cf65d36897822be9be6afe519020fbfc111676854c4778d62ceca2af46e1ef47"

jwt = JWTManager(app)


def __get_user(request):
    token = request.headers.get("Authorization")[7::]
    return jwt_lib.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    try:
        user = DBController.get_user_db(username)
    except:
        user = None
    if user:
        salted_pw = password + user.salt
        hashed_pw = hashlib.sha256(bytes(salted_pw, 'utf-8')).hexdigest()
        verified = hashed_pw == user.password
        if not verified:
            return jsonify({"msg": "Bad username or password"}), 401
    else:
        myuuid = uuid.uuid4()
        id = str(myuuid)
        salt = id
        salted_pw = password + salt
        hashed_pw = hashlib.sha256(bytes(salted_pw, 'utf-8')).hexdigest()
        DBController.create_user_db(username, id, hashed_pw, salt)

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/test_jwt', methods=['GET'])
@jwt_required()
def test_jwt():
    # Beispiel um user zu bekommen
    token = request.headers.get("Authorization")[7::]
    user = jwt_lib.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
    print(user, flush=True)
    return jsonify({"msg": "Test JWT Works"}), 200


@jwt_required()
@app.route('/ship/get')
def get_ship():
    id = request.args.get("id")
    return DBController.get_ship_db(id, __get_user(request)).__dict__()


@jwt_required()
@app.route('/ship/list')
def get_all_ships():
    user = request.args.get("user")
    ships = DBController.get_all_ships_from_user_id_db(user)
    erg = []
    for ship in ships:
        erg.append(ship.__dict__())
    return erg


@jwt_required()
@app.route('/ship/add')
def add_ship():
    user = request.args.get("user")
    name = request.args.get("name")
    is_active = bool(request.args.get("is_active"))
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return DBController.create_ship_db(user, name, id, is_active, capacity)


@jwt_required()
@app.route('/ship/update')
def update_ship():
    user = request.args.get("user")
    name = request.args.get("name")
    is_active = bool(request.args.get("is_active"))
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return DBController.update_ship_db(user, name, id, is_active, capacity)


@jwt_required()
@app.route('/ship/delete')
def delete_ship():
    id = request.args.get("id")
    return DBController.delete_ship_db(id)


@jwt_required()
@app.route('/quest/get')
def get_quest():
    id = request.args.get("id")
    return DBController.get_quest_db(id).__dict__()


@jwt_required()
@app.route('/quest/list')
def get_quests():
    user = request.args.get("user")
    ships = DBController.get_all_quests_from_user_id_db(user)
    erg = []
    for ship in ships:
        erg.append(ship.__dict__())
    return erg


@jwt_required()
@app.route('/quest/add')
def add_quest():
    user = request.args.get("user")
    name = request.args.get("name")
    is_active = bool(request.args.get("is_active"))
    resource = request.args.get("resource")
    items_per_capacity = request.args.get("items_per_capacity")
    demand = request.args.get("demand")
    id = request.args.get("id")
    return DBController.create_quest_db(user, name, id, is_active, resource, items_per_capacity, demand)


@jwt_required()
@app.route('/quest/update')
def update_quest():
    user = request.args.get("user")
    name = request.args.get("name")
    is_active = bool(request.args.get("is_active"))
    resource = request.args.get("resource")
    items_per_capacity = request.args.get("items_per_capacity")
    demand = request.args.get("demand")
    id = request.args.get("id")
    return DBController.update_quest_db(user, name, id, is_active, resource, items_per_capacity, demand)


@jwt_required()
@app.route('/quest/delete')
def delete_quest():
    id = request.args.get("id")
    return DBController.delete_quest_db(id)


@jwt_required()
@app.route('/user/get')
def get_user():
    id = request.args.get("id")
    return DBController.get_user_db(id).__dict__()


@jwt_required()
@app.route('/user/list')
def get_all_users():
    users = DBController.get_all_users_db()
    erg = []
    for user in users:
        erg.append(user.__dict__())
    return erg


@jwt_required()
@app.route('/user/add', methods=['POST'])
def add_user():
    name = request.args.get("name")
    myuuid = uuid.uuid4()
    id = str(myuuid)
    password = request.args.get("password")
    salt = id
    salted_pw = password + salt
    hashed_pw = hashlib.sha256(salted_pw)

    return DBController.create_user_db(name, id, hashed_pw, salt)


@jwt_required()
@app.route('/user/update')
def update_user():
    name = request.args.get("name")
    id = request.args.get("id")
    password = request.args.get("password")
    salt = id
    return DBController.update_user_db(name, id, password, salt)


@jwt_required()
@app.route('/user/delete')
def delete_user():
    id = request.args.get("id")
    return DBController.delete_user_db(id)


@app.route('/isAlive')
def is_alive():
    return jsonify({"msg": "Alive"}), 200


if __name__ == '__main__':
    app.run()
