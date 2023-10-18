from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Solver.RubenSolver import RubenSolver


def test_calculate_resource_optimized():
    ships = [Ship("user", "ship1", "s1", True, 100),
             Ship("user", "ship2", "s2", True, 50),
             Ship("user", "ship3", "s3", True, 20),]
    quests = [Quest("user", "quest1", "q1", True, "Stein", 1, 200),
              Quest("user", "quest2", "q2", True, "Holz", 1, 120),
              Quest("user", "quest3", "q3", True, "Münzen", 1, 110),
              ]
    ruben_solver = RubenSolver(ships,quests)
    result = ruben_solver.calculate_resource_optimized()