
class User:
    def __init__(self,  name, salt, hashed_pw):
        self.name = name
        self.salt = salt
        self.hashed_pw = hashed_pw

    def __dict__(self):
        return {"name": self.name,
                "hashed_pw": self.hashed_pw,
                }

