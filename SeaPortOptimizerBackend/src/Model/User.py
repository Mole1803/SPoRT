class User:
    def __init__(self, id, name, password, salt):
        self.id = id
        self.name = name
        self.password = password
        self.salt = salt

    def __dict__(self):
        return {"name": self.name,
                "id": self.id,
                }
