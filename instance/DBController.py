from _DatabaseCall import db, Users as UserDB, Ships as ShipDB, Quests as QuestDB
from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
#from SeaPortOptimizerBackend.src.Model.User import User




#def get_all_users_db():
#    users = db.session.execute(db.select(UserDB).order_by(UserDB.name)).scalars()
#    returnList = []
#    for user in users:
#        returnList.append(User(user.id, user.name))
#    return users


#def delete_user_db(id):
#    user = db.get_or_404(UserDB, id)
#    if user:
#        db.session.delete(user)
#        db.session.commit()


#def get_user_db(id):
#    user = db.get_or_404(UserDB, id)
#    if user:
#        return User(user.id, user.name)
#    return None


#def update_user_db(name, id):
#    user = db.get_or_404(UserDB, id)
#    if user:
#        user.id = id
#        user.name = name
#        db.session.commit()


def create_ship_db(userID, name, id, isActive, capacity):
    ship = ShipDB(
        id=id,
        name=name,
        isActive=isActive,
        capacity=capacity,
        userID=userID
    )
    db.session.add(ship)
    db.session.commit()


def get_all_ships_db():
    ships = db.session.execute(db.select(ShipDB).order_by(ShipDB.name)).scalars()
    returnList = []
    for ship in ships:
        returnList.append(Ship(ship.userID, ship.name, ship.id, ship.isActive, ship.capacity))
    return returnList


def delete_ship_db(id):
    ship = db.get_or_404(ShipDB, id)
    if ship:
        db.session.delete(ship)
        db.session.commit()


def get_ship_db(id):
    ship = db.get_or_404(ShipDB, id)
    if ship:
        return Ship(ship.userID, ship.name, ship.id, ship.isActive, ship.capacity)
    return None


def update_ship_db(userID, name, id, isActive, capacity):
    ship = db.get_or_404(ShipDB, id)
    if ship:
        ship.id = id
        ship.name = name
        ship.userID = userID
        ship.capacity = capacity
        ship.isActive = isActive
        db.session.commit()


def create_quest_db(userID, name, id, isActive, resource, itemsPerCapacity, demand):
    quest = QuestDB(
        id=id,
        name=name,
        isActive=isActive,
        resource=resource,
        demand=demand,
        userID=userID,
        itemsPerCapacity=itemsPerCapacity
    )
    db.session.add(quest)
    db.session.commit()


def get_all_quests_db():
    quests = db.session.execute(db.select(QuestDB).order_by(QuestDB.name)).scalars()
    returnList = []
    for quest in quests:
        returnList.append(Quest(quest.user, quest.name, quest.id, quest.isActive, quest.resource, quest.itemsPerCapactiy, quest.demand))
    return returnList


def delete_quest_db(id):
    quest = db.get_or_404(QuestDB, id)
    if quest:
        db.session.delete(quest)
        db.session.commit()


def get_quest_db(id):
    quest = db.get_or_404(QuestDB, id)
    if quest:
        return Quest(quest.userID, quest.name, quest.id, quest.isActive, quest.resource, quest.itemsPerCapacity, quest.demand)
    return None


def update_quest_db(userID, name, id, isActive, resource, itemsPerCapacity, demand):
    quest = db.get_or_404(QuestDB, id)
    if quest:
        quest.id = id
        quest.name = name
        quest.userID = userID
        quest.isActive = isActive
        quest.resource = resource
        quest.itemsPerCapacity = itemsPerCapacity
        quest.demand = demand
        db.session.commit()

