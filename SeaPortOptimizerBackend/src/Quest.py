
class Quest:
    def __init__(self, name, id, is_active, resource, items_per_capacity,demand):
        self.name = name
        self.id = id
        self.is_active = is_active
        self.resource = resource
        self.items_per_capacity = items_per_capacity
        self.demand = demand
