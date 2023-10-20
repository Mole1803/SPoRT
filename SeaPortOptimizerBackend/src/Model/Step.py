
class Step:
    def __init__(self, ship_id, quest_id, quest_capacity):
        self.ship_id = ship_id
        self.quest_id = quest_id
        self.quest_capacity = quest_capacity
        self.spare_capacity = 0

    def set_spare_capacity(self, spare_capacity):
        self.spare_capacity = spare_capacity
