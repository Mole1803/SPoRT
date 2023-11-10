class Step:
    def __init__(self, ship_id, quest_id, spare_capacity):
        self.ship_id = ship_id
        self.quest_id = quest_id
        self.spare_capacity = spare_capacity

    def __dict__(self):
        return {"ship_id": self.ship_id,
                "quest_id": self.quest_id,
                "spare_capacity": self.spare_capacity
                }
