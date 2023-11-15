
class Step:
    def __init__(self, ship_id, quest_id, quest_capacity):
        self.ship_id = ship_id
        self.quest_id = quest_id
        self.quest_capacity = quest_capacity
        self.spare_capacity = 0

    def set_spare_capacity(self, spare_capacity):
        self.spare_capacity = spare_capacity

    def __dict__(self):
        return {"shipId": self.ship_id,
                "questId": self.quest_id,
                "usedCapacity": self.quest_capacity
                }

    def __eq__(self, other):
        return self.ship_id == other.ship_id and self.quest_id == other.quest_id

    def __str__(self):
        return self.ship_id
