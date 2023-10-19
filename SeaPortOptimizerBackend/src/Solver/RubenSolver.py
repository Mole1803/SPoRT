from math import inf

from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Solver.Solver import Solver
from SeaPortOptimizerBackend.src.Model.Step import Step


class RubenSolver(Solver):
    # def __init__(self,id):
    #    super().__init__(id)

    def __init__(self, ships, quests):
        super().__init__(ships, quests)

    def calculate_time_optimized(self):
        pass

    def calculate_resource_optimized(self):
        optimal_substeps = {}
        for quest in self.quests:
            quest.all_steps = []
            self.calculate_all_steps(quest, self.ships, [])
            optimal_substeps[quest.id] = quest.all_steps
            self.filter_steps(quest)
        solutions = self.arrange_steps(self.quests)
        ships_by_solutions = self.filter_solutions_by_ships(solutions, self.ships)
        best_solutions, rounds = self.get_best_solutions(ships_by_solutions)
        results = self.parse_solutions_to_results(best_solutions, rounds)
        print(results)

    def parse_solutions_to_results(self, best_solutions, number_of_rounds):
        results = []
        for solution in best_solutions:
            rounds = []
            for round_index in range(number_of_rounds):
                round = Round([])
                for ship in solution:
                    if len(solution[ship]) > round_index:
                        round.add_step(solution[ship][round_index])
                rounds.append(round)
            results.append(Result(rounds))
        return results

    def get_best_solutions(self, ships_by_solutions):
        min = inf
        best_solutions = []
        for solution in ships_by_solutions:
            take_rounds = 0
            for ship in solution:
                if len(solution[ship]) > take_rounds:
                    take_rounds = len(solution[ship])
            if take_rounds < min:
                min = take_rounds
                best_solutions = [solution]
            elif take_rounds == min:
                best_solutions.append(solution)
        return best_solutions, min

    def filter_solutions_by_ships(self, solutions, ships):
        ships_by_solutions = []
        for solution in solutions:
            ship_quests = {}
            for ship in ships:
                ship_quests[ship.id] = []
            for step in solution:
                ship_quests[step.ship_id].append(step)
            ships_by_solutions.append(ship_quests)
        return ships_by_solutions

    def arrange_steps(self, quests):
        solutions = []
        for quest in quests:
            if len(solutions) == 0:
                solutions = quest.all_steps
            else:
                new_solutions = []
                for solution in solutions:
                    for steps in quest.all_steps:
                        new_solutions.append(solution + steps)
                solutions = new_solutions
        return solutions

    def filter_steps(self, quest):
        min = inf
        best_steps = []
        for steps in quest.all_steps:
            sum = 0
            for step in steps:
                sum += step.spare_capacity
            if sum < min:
                best_steps = [steps]
                min = sum
            elif sum == min:
                best_steps.append(steps)
        quest.all_steps = best_steps

    def calculate_all_steps(self, quest, ships, steps, index=0):
        i = index
        while i < len(ships):
            if quest.remaining_demand > 0:
                ship = ships[i]
                quest.remaining_demand -= quest.items_per_capacity * ship.capacity
                step = Step(ship.id, quest.id, quest.items_per_capacity * ship.capacity)
                steps.append(step)
                i = self.calculate_all_steps(quest, ships, steps, i)
            else:
                quest.all_steps.append(steps.copy())
                last_step = steps.pop(-1)
                quest.remaining_demand += last_step.spare_capacity
                return i + 1
        if len(steps) > 0:
            last_step = steps.pop(-1)
            quest.remaining_demand += last_step.spare_capacity
        return index + 1
