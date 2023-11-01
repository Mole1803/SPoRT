# TODO delete this file

class User:
    def __init__(self, name, salt, password):
        self.name = name
        self.salt = salt
        self.password = password

    def __dict__(self):
        return {"name": self.name,
                }
