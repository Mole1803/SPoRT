from flask import Flask, jsonify, request
from flask_cors import CORS

from SeaPortOptimizerBackend.src.Ship import Ship

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})



#CORS(app)

@app.route('/getShip')
def getShip():
    id=request.args.get("id")
    return getShipFromDb(id).__dict__()


@app.route('/getShips')
def getShips():
    ships=getAllShipsFromDb()
    erg=[]
    for ship in ships:
        erg.append(ship.__dict__())
    return erg
@app.route('/addShip')
def addShip():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return addShipToDb(user, name, id, is_active, capacity)

@app.route('/updateShip')
def updateShip():
    user = request.args.get(" user")
    name = request.args.get("name")
    is_active = request.args.get("is_active")
    capacity = request.args.get("capacity")
    id = request.args.get("id")
    return updateShipToDb(user, name, id, is_active, capacity)

@app.route('/deleteShip')
def deleteShip():
    id = request.args.get("id")
    return deleteShipFromDb(id)

def addShipToDb(user, name, id, is_active, capacity):
    return False

def updateShipToDb(user, name, id, is_active, capacity):
    return False

def deleteShipFromDb(id):
    return False

def getAllShipsFromDb():
    erg = [Ship("testuser", "ship_name2", "id1", True, 50), Ship("testuser", "ship_name2", "id2", True, 50)]
    return erg

def getShipFromDb(id):
    erg = Ship("testuser","mock_name", id, True, 50)
    return erg


@app.route('/isAlive')
def hello_world():
    return jsonify({'isAlive': True})


if __name__ == '__main__':
    app.run()
