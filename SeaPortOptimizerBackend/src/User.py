class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.a = 0

    def __dict__(self):
        return {"name": self.name,
                "id": self.id,
                }