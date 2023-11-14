from unittest import TestCase
from MoritzSolver import MoritzSolver, RoundPerformance
from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Model.Step import Step


class TestMoritzSolverPermutationCreation(TestCase):
    def test_create_all_permutations_equal_size_length(self):
        ships = [1, 2, 3]
        quests = [1, 2, 3]
        expected = 9
        assert len(MoritzSolver.create_all_permutations(ships, quests)) == expected

    def test_create_all_permutations_equal_size_content(self):
        ships = [1, 2, 3]
        quests = [1, 2, 3]

        expected_tuples = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
        print(expected_tuples)
        tuple_result = {base_step.get_as_tuple() for base_step in MoritzSolver.create_all_permutations(ships, quests)}
        print(tuple_result)
        assert expected_tuples == tuple_result

    def test_create_all_permutations_quests_longer_length(self):
        ships = [1, 2]
        quests = [1, 2, 3]

        expected = 6
        assert len(MoritzSolver.create_all_permutations(ships, quests)) == expected

    def test_create_all_permutations_quests_longer_content(self):
        ships = [1, 2]
        quests = [1, 2, 3]

        expected_tuples = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)}
        print("expected_tuples: ", expected_tuples)
        tuple_result = {base_step.get_as_tuple() for base_step in MoritzSolver.create_all_permutations(ships, quests)}
        print("tuple_result: ", tuple_result)
        assert expected_tuples == tuple_result

    def test_create_all_permutations_ships_longer_dif_1_length(self):
        ships = [1, 2, 3]
        quests = [1, 2]

        expected = 9
        assert len(MoritzSolver.create_all_permutations(ships, quests)) == expected

    def test_create_all_permutations_ships_longer_dif_1_content(self):
        ships = [1, 2, 3]
        quests = [1, 2]

        expected_tuples = {(1, 1), (1, 2), (1, None), (2, 1), (2, 2), (2, None), (3, 1), (3, 2), (3, None)}
        print("expected_tuples: ", expected_tuples)
        tuple_result = {base_step.get_as_tuple() for base_step in MoritzSolver.create_all_permutations(ships, quests)}
        print("tuple_result: ", tuple_result)

        assert expected_tuples == tuple_result


    def test_create_all_permutations_ships_longer_dif_greater_1_length(self):
        ships = [1, 2, 3, 4]
        quests = [1, 2]

        expected = 12
        output = len(MoritzSolver.create_all_permutations(ships, quests))
        print(output)
        assert output == expected

    def test_create_all_permutations_ships_longer_dif_greater_1_content(self):
        ships = [1, 2, 3, 4]
        quests = [1, 2]

        expected_tuples = {(1, 1), (1, 2), (1, None), (2, 1), (2, 2), (2, None), (3, 1), (3, 2), (3, None), (4, 1), (4, 2), (4, None)}
        print("expected_tuples: ", expected_tuples)
        tuple_result = {base_step.get_as_tuple() for base_step in MoritzSolver.create_all_permutations(ships, quests)}
        print("tuple_result: ", tuple_result)

        assert expected_tuples == tuple_result


class TestMoritzSolverRemainingResources(TestCase):
    def test_calculate_remaining_resources(self):
        ships = [
            Ship("TestUser","ship1","id_1",True, 100),
            Ship("TestUser", "ship2", "id_2", True, 100),
            Ship("TestUser", "ship3", "id_3", True, 100),
        ]

        quests = [
            Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 200),
            Quest("TestUser", "quest2", "id_2", True, "Holz", 1, 120),
            Quest("TestUser", "quest3", "id_3", True, "Münzen", 1, 110),
        ]

        steps = [
            Step(ships[0].id, quests[0].id, quests[0].demand),
            Step(ships[1].id, quests[1].id, quests[1].demand),
            Step(ships[2].id, quests[2].id, quests[2].demand)
        ]

        # 200 - 100 = 100
        # 120 - 100 = 20
        # 110 - 100 = 10
        expected = RoundPerformance(130)
        output = MoritzSolver.calculate_remaining_resources(ships, steps)
        print(output)
        assert expected.outstanding == output.outstanding
        assert expected.performance == output.performance

    def test_calculate_remaining_resources_zero(self):
        ships = [
            Ship("TestUser","ship1","id_1",True, 200),
            Ship("TestUser", "ship2", "id_2", True, 120),
            Ship("TestUser", "ship3", "id_3", True, 110),
        ]

        quests = [
            Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 200),
            Quest("TestUser", "quest2", "id_2", True, "Holz", 1, 120),
            Quest("TestUser", "quest3", "id_3", True, "Münzen", 1, 110),
        ]

        steps = [
            Step(ships[0].id, quests[0].id, quests[0].demand),
            Step(ships[1].id, quests[1].id, quests[1].demand),
            Step(ships[2].id, quests[2].id, quests[2].demand)
        ]

        expected = RoundPerformance(0)
        output = MoritzSolver.calculate_remaining_resources(ships, steps)
        print(output)
        assert expected.outstanding == output.outstanding
        assert expected.performance == output.performance

    def test_calculate_remaining_resources_outstanding(self):
        ships = [
            Ship("TestUser","ship1","id_1",True, 100),
            Ship("TestUser", "ship2", "id_2", True, 120),
            Ship("TestUser", "ship3", "id_3", True, 80),
        ]

        quests = [
            Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 100),
            Quest("TestUser", "quest2", "id_2", True, "Holz", 1, 100),
            Quest("TestUser", "quest3", "id_3", True, "Münzen", 1, 100),
        ]

        steps = [
            Step(ships[0].id, quests[0].id, quests[0].demand),
            Step(ships[1].id, quests[1].id, quests[1].demand),
            Step(ships[2].id, quests[2].id, quests[2].demand)
        ]

        expected = RoundPerformance(20, 0)
        output = MoritzSolver.calculate_remaining_resources(ships, steps)
        print(output)
        assert expected.outstanding == output.outstanding
        assert expected.performance == output.performance

    def test_calculate_remaining_resources_finished_and_negative_performance(self):
        ships = [
            Ship("TestUser","ship1","id_1",True, 100),
            Ship("TestUser", "ship2", "id_2", True, 120),
            Ship("TestUser", "ship3", "id_3", True, 100),
        ]

        quests = [
            Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 100),
            Quest("TestUser", "quest2", "id_2", True, "Holz", 1, 100),
            Quest("TestUser", "quest3", "id_3", True, "Münzen", 1, 100),
        ]

        steps = [
            Step(ships[0].id, quests[0].id, quests[0].demand),
            Step(ships[1].id, quests[1].id, quests[1].demand),
            Step(ships[2].id, quests[2].id, quests[2].demand)
        ]

        expected = RoundPerformance(0, -20)
        output = MoritzSolver.calculate_remaining_resources(ships, steps)
        print(output)
        assert expected.outstanding == output.outstanding
        assert expected.performance == output.performance

    def test_calculate_remaining_resources_not_finished_and_negative_performance(self):
        ships = [
            Ship("TestUser","ship1","id_1",True, 100),
            Ship("TestUser", "ship2", "id_2", True, 120),
            Ship("TestUser", "ship3", "id_3", True, 90),
        ]

        quests = [
            Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 100),
            Quest("TestUser", "quest2", "id_2", True, "Holz", 1, 100),
            Quest("TestUser", "quest3", "id_3", True, "Münzen", 1, 100),
        ]

        steps = [
            Step(ships[0].id, quests[0].id, quests[0].demand),
            Step(ships[1].id, quests[1].id, quests[1].demand),
            Step(ships[2].id, quests[2].id, quests[2].demand)
        ]

        expected = RoundPerformance(10, -10)
        output = MoritzSolver.calculate_remaining_resources(ships, steps)
        print(output)
        assert expected.outstanding == output.outstanding
        assert expected.performance == output.performance

class TestMoritzSolutionCalculateOptimalRessource(TestCase):
    def test_calculate_optimal_quest_solutions(self):
        ships = [
            Ship("TestUser", "ship1", "id_1", True, 20),
            Ship("TestUser", "ship2", "id_2", True, 50),
            Ship("TestUser", "ship3", "id_3", True, 10),
        ]

        quest = Quest("TestUser", "quest1", "id_1", True, "Stein", 1, 100)
        #print(len(set(MoritzSolver.calculate_optimal_quest_solutions(quest, ships))))
        #print(MoritzSolver.calculate_optimal_quest_solutions(quest, ships))

    def test_calculate_resource_optimized(self):
        ships = [
            Ship("TestUser", "ship1", "id_1", True, 20),
            Ship("TestUser", "ship2", "id_2", True, 50),
            Ship("TestUser", "ship3", "id_3", True, 10),
        ]
        print([1,2,3][3:])
        quests = [Quest("TestUser", "quest1", "quest_id_1", True, "Stein", 1, 100),
                  Quest("TestUser", "quest2", "quest_id_2", True, "Stein", 1, 100)]
        print(len(MoritzSolver._calculate_resource_optimized(quests, ships)))

