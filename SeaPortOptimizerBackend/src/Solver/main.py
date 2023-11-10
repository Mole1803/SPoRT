from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Solver.TimSolver import TimSolver

if __name__ == '__main__':
    ships = [Ship("user", "ship1", "A", True, 50),
             Ship("user", "ship2", "B", True, 200),
             Ship("user", "ship3", "C", True, 100),
             Ship("user", "ship4", "D", True, 60), ]
    quests = [Quest("user", "quest1", "q1", True, "Fisch", 1, 150),
              Quest("user", "quest2", "q2", True, "Stein", 1, 200),
              Quest("user", "quest3", "q3", True, "Holz", 1, 400),
              ]
    tim_solver = TimSolver(ships, quests)
    result = tim_solver.calculate_resource_optimized()
    for round in result:
        print('Round: ' + result.index(round))
        for step in round:
            print(step.__dict__())
