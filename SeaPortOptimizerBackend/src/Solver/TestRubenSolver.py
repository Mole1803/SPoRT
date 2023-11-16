from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Solver.RubenSolver import RubenSolver


class TestRubenSolver:
    def test_calculate_resource_optimized(self):
        ships = [Ship("user", "ship1", "s1", True, 100),
                 Ship("user", "ship2", "s2", True, 50),
                 Ship("user", "ship3", "s3", True, 20), ]
        quests = [Quest("user", "quest1", "q1", True, "Stein", 1, 200),
                  Quest("user", "quest2", "q2", True, "Holz", 1, 120),
                  Quest("user", "quest3", "q3", True, "Münzen", 1, 110),
                  ]
        ruben_solver = RubenSolver(None)
        ruben_solver.set(ships, quests)
        results = ruben_solver.calculate_resource_optimized()
        assert len(results) == 3
        for result in results:
            assert len(result.rounds) == 4

    def test_calculate_resource_optimized2(self):
        ships = [Ship("user", "ship1", "A", True, 50),
                 Ship("user", "ship2", "B", True, 200),
                 Ship("user", "ship2", "C", True, 100),
                 Ship("user", "ship2", "D", True, 60), ]
        quests = [Quest("user", "quest1", "q1", True, "Fisch", 1, 150),
                  Quest("user", "quest2", "q2", True, "Stein", 1, 200),
                  Quest("user", "quest3", "q3", True, "Holz", 1, 400),
                  ]
        ruben_solver = RubenSolver(None)
        ruben_solver.set(ships, quests)
        results = ruben_solver.calculate_resource_optimized()
        print(results)
        assert len(results) == 8
        for result in results:
            assert len(result.rounds) == 3

    def test_calculate_resource_optimized3(self):
        ships = [Ship("user", "ship1", "s1", True, 20),
                 Ship("user", "ship2", "s2", True, 50),
                 Ship("user", "ship3", "s3", True, 10),
                 Ship("user", "ship4", "s4", True, 25),
                 Ship("user", "ship5", "s5", True, 12),
                 Ship("user", "ship6", "s6", True, 16),
                 ]
        quests = [Quest("user", "quest1", "q1", True, "Stein", 1, 100),
                  Quest("user", "quest2", "q2", True, "Stein", 1, 77),
                  Quest("user", "quest3", "q3", True, "Stein", 1, 83),
                  Quest("user", "quest4", "q4", True, "Stein", 1, 47),
                  Quest("user", "quest5", "q5", True, "Stein", 1, 63),
                  Quest("user", "quest6", "q6", True, "Stein", 1, 104),
                  ]
        ruben_solver = RubenSolver(None)
        ruben_solver.set(ships, quests)
        results = ruben_solver.calculate_resource_optimized()
        assert len(results) == 14
        for result in results:
            assert len(result.rounds) == 5

    def test_calculate_time_optimized(self):
        ships = [Ship("user", "ship1", "s1", True, 100),
                 Ship("user", "ship2", "s2", True, 50),
                 Ship("user", "ship3", "s3", True, 20), ]
        quests = [Quest("user", "quest1", "q1", True, "Stein", 1, 200),
                  Quest("user", "quest2", "q2", True, "Holz", 1, 120),
                  Quest("user", "quest3", "q3", True, "Münzen", 1, 110),
                  ]
        ruben_solver = RubenSolver(None)
        ruben_solver.set(ships, quests)
        results = ruben_solver.calculate_time_optimized()
        assert len(results) == 3
        for result in results:
            assert len(result.rounds) == 3

    def test_calculate_time_optimized2(self):
        ships = [Ship("user", "ship1", "A", True, 50),
                 Ship("user", "ship2", "B", True, 200),
                 Ship("user", "ship2", "C", True, 100),
                 Ship("user", "ship2", "D", True, 60), ]
        quests = [Quest("user", "quest1", "q1", True, "Fisch", 1, 150),
                  Quest("user", "quest2", "q2", True, "Stein", 1, 200),
                  Quest("user", "quest3", "q3", True, "Holz", 1, 400),
                  ]
        ruben_solver = RubenSolver(None)
        ruben_solver.set(ships, quests)
        results = ruben_solver.calculate_time_optimized()
        print(results)
        assert len(results) == 6
        for result in results:
            assert len(result.rounds) == 2

    def test_calculate_time_optimized3(self):
        ships = [Ship("user", "ship1", "s1", True, 20),
                 Ship("user", "ship2", "s2", True, 50),
                 Ship("user", "ship3", "s3", True, 10),
                 Ship("user", "ship4", "s4", True, 25),
                 ]
        quests = [Quest("user", "quest1", "q1", True, "Stein", 1, 100),
                  Quest("user", "quest2", "q2", True, "Stein", 1, 77),
                  Quest("user", "quest3", "q3", True, "Stein", 1, 83),
                  Quest("user", "quest4", "q4", True, "Stein", 1, 47),
                  ]
        ruben_solver = RubenSolver(None)
        ruben_solver.set(ships, quests)
        results = ruben_solver.calculate_time_optimized()
        assert len(results) == 16
        for result in results:
            assert len(result.rounds) == 3