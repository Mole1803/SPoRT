from flask import Flask, jsonify, request
from flask_cors import CORS

from SeaPortOptimizerBackend.src.Ship import Ship
from db_mock import MockDBController

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})


# CORS(app)

DBController = MockDBController()

@app.route('/getShip')
def get_ship():
    id = request.args.get("id")
    return DBController.get_ship(id).__dict__()


@app.route('/getShips')
def get_ships():
    ships = DBController.get_all_ships()
    erg = []
    for ship in ships:
        erg.append(ship.__dict__())
    return erg


@app.route('/addShip')
def add_ship():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return DBController.create_ship(user, name, id, is_active, capacity)


@app.route('/updateShip')
def update_ship():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return DBController.update_ship(user, name, id, is_active, capacity)


@app.route('/deleteShip')
def delete_ship():
    id = request.args.get("id")
    return DBController.delete_ship(id)


@app.route('/addQuest')
def add_quest():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    resource= request.args.get("resource")
    items_per_capacity=request.args.get("items_per_capacity")
    demand=request.args.get("demand")
    id = request.args.get("id")

    return DBController.create_quest(user, name, id, is_active, resource, items_per_capacity, demand)


@app.route('/updateQuest')
def update_quest():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    resource = request.args.get("resource")
    items_per_capacity = request.args.get("items_per_capacity")
    demand = request.args.get("demand")
    id = request.args.get("id")

    return DBController.update_quest(user, name, id, is_active, resource, items_per_capacity, demand)


@app.route('/deleteQuest')
def delete_quest():
    id = request.args.get("id")
    return DBController.delete_quest(id)


@app.route('/isAlive')
def hello_world():
    return jsonify({'isAlive': True})


if __name__ == '__main__':
    app.run()
