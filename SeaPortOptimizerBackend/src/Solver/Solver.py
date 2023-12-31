from abc import ABC, abstractmethod
from instance import DBController


class Solver(ABC):
    def __init__(self, id=None):
        if(id):
            self.ships = DBController.get_all_active_ships_from_user_id_db(id)
            self.quests = DBController.get_all_active_quests_from_user_id_db(id)

    def set(self, ships, quests):
        self.ships = ships
        self.quests = quests

    def verify_valid(self):
        if len(self.ships) == 0:
            return False
        if len(self.quests) == 0:
            return False
        return True

    @abstractmethod
    def calculate_time_optimized(self):
        pass

    @abstractmethod
    def calculate_resource_optimized(self):
        pass
