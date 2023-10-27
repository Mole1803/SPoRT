from _DatabaseCall import db, Ships as ShipDB, Quests as QuestDB
from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship


def create_ship_db(username, name, id, isActive, capacity):
    ship = ShipDB(
        id=id,
        name=name,
        isActive=isActive,
        capacity=capacity,
        username=username
    )
    try:
        db.session.add(ship)
        db.session.commit()
        return True
    except:
        return False


def get_all_ships_from_user_id_db(username):
    ships = db.session.query(ShipDB).filter_by(username=username).all()
    returnList = []
    for ship in ships:
        returnList.append(Ship(ship.username, ship.name, ship.id, ship.isActive, ship.capacity))
    return returnList


def delete_ship_db(id):
    ship = db.get_or_404(ShipDB, id)
    if ship:
        db.session.delete(ship)
        db.session.commit()


def get_ship_db(id, username):
    ship = db.session.query(ShipDB).filter_by(username=username, id=id).all()
    if ship:
        return Ship(ship.username, ship.name, ship.id, ship.isActive, ship.capacity)
    return None


def update_ship_db(username, name, id, isActive, capacity):
    ship = db.get_or_404(ShipDB, id)
    if ship:
        ship.id = id
        ship.name = name
        ship.username = username
        ship.capacity = capacity
        ship.isActive = isActive
        db.session.commit()


def create_quest_db(username, name, id, isActive, resource, itemsPerCapacity, demand):
    quest = QuestDB(
        id=id,
        name=name,
        isActive=isActive,
        resource=resource,
        demand=demand,
        username=username,
        itemsPerCapacity=itemsPerCapacity
    )
    db.session.add(quest)
    db.session.commit()


def get_all_quests_from_user_id_db(username):
    quests = db.session.query(ShipDB).filter_by(username=username).all()
    returnList = []
    for quest in quests:
        returnList.append(Quest(quest.username, quest.name, quest.id, quest.isActive, quest.resource, quest.itemsPerCapactiy, quest.demand))
    return returnList


def delete_quest_db(id):
    quest = db.get_or_404(QuestDB, id)
    if quest:
        db.session.delete(quest)
        db.session.commit()


def get_quest_db(id):
    quest = db.get_or_404(QuestDB, id)
    if quest:
        return Quest(quest.username, quest.name, quest.id, quest.isActive, quest.resource, quest.itemsPerCapacity, quest.demand)
    return None


def update_quest_db(username, name, id, isActive, resource, itemsPerCapacity, demand):
    quest = db.get_or_404(QuestDB, id)
    if quest:
        quest.id = id
        quest.name = name
        quest.username = username
        quest.isActive = isActive
        quest.resource = resource
        quest.itemsPerCapacity = itemsPerCapacity
        quest.demand = demand
        db.session.commit()

