class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __dict__(self):
        return {"name": self.name,
                "id": self.id,
                }