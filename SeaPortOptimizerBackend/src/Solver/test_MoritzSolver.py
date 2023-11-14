from unittest import TestCase
from MoritzSolver import MoritzSolver
from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Model.Step import Step

class TestMoritzSolutionCalculateOptimalRessource(TestCase):
    def test_calculate_optimal_quest_solutions(self):
        ships = [
            Ship("TestUser", "ship1", "id_1", True, 20),
            Ship("TestUser", "ship2", "id_2", True, 50),
            Ship("TestUser", "ship3", "id_3", True, 10),
        ]

        quest = Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 100)
        assert len(MoritzSolver.calculate_optimal_quest_solutions(quest, ships)) == 2


    def test_calculate_resource_optimized(self):
        ships = [
            Ship("TestUser", "ship1", "id_1", True, 20),
            Ship("TestUser", "ship2", "id_2", True, 50),
            Ship("TestUser", "ship3", "id_3", True, 10),
        ]

        quests = [Quest("TestUser", "quest1", "quest_id_1", True, "Stein", 1, 100),
                  Quest("TestUser", "quest2", "quest_id_2", True, "Stein", 1, 100)]
        assert print(len(MoritzSolver._calculate_resource_optimized(quests, ships))) == 4


class TestMoritzSolver(TestCase):
    def test_calculate_max_rounds_from_array(self):
        arr = [[1, 2], [1, 3], [1, 2, 3, 4]]
        expected = 3
        output = MoritzSolver.calculate_max_rounds_from_array(arr)
        assert expected == output


class TestMoritzSolver_TimeOptimized(TestCase):
    def test___calculate_time_optimized(self):
        ships = [
            Ship("TestUser", "ship1", "id_1", True, 20),
            Ship("TestUser", "ship2", "id_2", True, 50),
            Ship("TestUser", "ship3", "id_3", True, 10),
        ]

        quests = [Quest("TestUser", "quest1", "quest_id_1", True, "Stein", 1, 100),
                  Quest("TestUser", "quest2", "quest_id_2", True, "Stein", 1, 100)]

        assert len(MoritzSolver._calculate_time_optimized(quests, ships)) == 4

