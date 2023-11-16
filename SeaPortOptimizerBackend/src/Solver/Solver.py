# from db_mock import MockDBController
from abc import ABC, abstractmethod

# DBController = MockDBController()


class Solver(ABC):
    def __init__(self, id):
        self.ships = DBController.get_all_ships_from_user_id_db(id)
        self.quests = DBController.get_all_quests_from_user_id_db(id)

    @abstractmethod
    def calculate_time_optimized(self):
        pass

    @abstractmethod
    def calculate_resource_optimized(self):
        pass
