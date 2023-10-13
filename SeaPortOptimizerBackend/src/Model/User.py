from db_mock import MockDBController

DBController = MockDBController()

class User:
    def __init__(self, id, name, salt, hashed_pw):
        self.id = id
        self.name = name
        self.salt = salt
        self.hashed_pw = hashed_pw

    def __dict__(self):
        return {"name": self.name,
                "id": self.id,
                "hashed_pw": self.hashed_pw,
                }

    @staticmethod
    def authorize(name, password):
        hashed_pw=DBController.get_user_hash(name)