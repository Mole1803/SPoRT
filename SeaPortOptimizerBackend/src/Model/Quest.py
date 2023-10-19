class Quest:
    def __init__(self, user, name, id, is_active, resource, items_per_capacity, demand):
        self.user = user
        self.name = name
        self.id = id
        self.is_active = is_active
        self.resource = resource
        self.items_per_capacity = items_per_capacity
        self.demand = demand
        self.remaining_demand = demand

    def __dict__(self):
        return {"name": self.name,
                "id": self.id,
                "is_active": self.is_active,
                "resource": self.resource,
                "items_per_capacity": self.items_per_capacity
                }
