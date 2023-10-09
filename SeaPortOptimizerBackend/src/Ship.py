class Ship:
    def __init__(self, user, name, id, is_active, capacity):
        self.user = user
        self.name = name
        self.id = id
        self.is_active = is_active
        self.capacity = capacity

    def __dict__(self):
        return {"name": self.name,
                "id": self.id,
                "is_active": self.is_active,
                "capacity": self.capacity
                }
