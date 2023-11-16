class Ship:
    def __init__(self, user, name, id, is_active, capacity):
        self.user = user
        self.name = name
        self.id = id
        self.is_active = is_active
        self.capacity = capacity

    def dict(self):
        return {"name": self.name,
                "id": self.id,
                "is_active": self.is_active,
                "capacity": self.capacity
                }

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id


