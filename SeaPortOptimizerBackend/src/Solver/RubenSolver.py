from math import inf

from SeaPortOptimizerBackend.src.Solver.Solver import Solver


def calculate_optimal_step_solution(quest,ships):
    spare=inf
    for



class RubenSolver(Solver):
    #def __init__(self,id):
    #    super().__init__(id)

    def __init__(self, ships, quests):
        super().__init__(ships, quests)

    def calculate_time_optimized(self):
        pass

    def calculate_resource_optimized(self):
        optimal_substeps={}
        for quest in self.quests:
            optimal_substeps[quest.id] = calculate_optimal_step_solution(quest,self.ships)

