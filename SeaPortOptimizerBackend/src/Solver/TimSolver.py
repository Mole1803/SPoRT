from SeaPortOptimizerBackend.src.Solver.Solver import Solver


class TimSolver(Solver):
    def __init__(self, id, quests_para):
        super().__init__(id)
        self.quests = quests_para

    def calculate_time_optimized(self):
        pass

    def calculate_resource_optimized(self):
        pass