from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Solver.Solver import Solver
from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Model.Step import Step


class BaseStep:
    def __init__(self, quest, ship):
        self.ship = ship
        self.quest = quest

    def get_as_tuple(self):
        return (self.ship, self.quest)

    def __dict__(self):
        return {"shipId": self.ship,
                "questId": self.quest
                }

    def __hash__(self):
        return hash(self.get_as_tuple())

    def __eq__(self, other):
        return self.get_as_tuple() == other.get_as_tuple()

class Performance:
    pass


class RoundPerformance(Performance):
    def __init__(self, outstanding, performance=None):
        self.outstanding = outstanding
        self.performance = outstanding
        if performance is not None:
            self.performance = performance

    def __str__(self):
        return "(outstanding: " + str(self.outstanding) + ", performance: " + str(self.performance) + ")"

class BestResourceSolution:
    def __init__(self, value=float('-inf')):
        self.value = value
        self.results = []

    def append_solution(self, solution, value):
        if float(value) > float(self.value):
            self.results = [tuple(solution[:])]
            self.value = value
            return
        if value == self.value:
            self.results.append((tuple(solution[:])))
            return

    def append_solution_inverted(self, solution, value):
        if float(value) < float(self.value):
            self.results = [tuple(solution[:])]
            self.value = value
            return
        if value == self.value:
            self.results.append(tuple(solution[:]))
            return



class MoritzSolver(Solver):
    def __init__(self, id):
        super().__init__(id)

    def solve(self):
        pass

    def calculate_time_optimized(self):
        pass


    def calculate_resource_optimized(self):
        return MoritzSolver._calculate_resource_optimized(self.quests, self.ships)

    @staticmethod
    def _calculate_resource_optimized(quests, ships):
        solutions_per_quest = {}
        for quest in quests:
            solutions_per_quest[quest.id] = MoritzSolver.calculate_optimal_quest_solutions(quest, ships)
        best_resource_solution = BestResourceSolution(float("inf"))
        MoritzSolver.permutate_quest_solutions(solutions_per_quest, list(solutions_per_quest.keys()), [], best_resource_solution)
        best_resource_solution.results = MoritzSolver.filter_permutations(best_resource_solution.results)
        steps_list = MoritzSolver.solution_to_steps(best_resource_solution.results, quests)
        build_rounds = MoritzSolver.build_rounds(steps_list, best_resource_solution.value)
        return build_rounds

    @staticmethod
    def solution_to_steps(solutions: list[tuple[tuple]], quests: list[Quest]):
        _solutions = []
        for solution in solutions:

            cache = []
            for i, quest in enumerate(solution):
                for ship in quest:

                    cache.append(Step(ship.id, quests[i].id, ship.capacity))
            _solutions.append(cache)

        return _solutions

    @staticmethod
    def build_rounds(steps_list: list[list[Step]], max_rounds: int):
        print(max_rounds)
        results: list[list] = [[Round() for y in range(max_rounds)] for x in range(len(steps_list))]
        print(results)
        for i, solution in enumerate(steps_list):
            for step in solution:
                for round_index in range(len(results[i])):
                    if results[i][round_index].step_in_round(step):
                        print("continue")
                        continue
                    results[i][round_index].add_step(step)
                    break
        _results = []
        for result in results:
            _results.append(Result(result))

        return _results


    @staticmethod
    def filter_permutations(results: list[tuple[tuple]]) -> list[tuple[tuple]]:
        for result_index in range(len(results)):
            results[result_index] = list(results[result_index])
            result = results[result_index]
            for quest_index in range(len(result)):
                quest = list(result[quest_index])
                quest.sort(key=lambda x: x.id)
                result[quest_index] = tuple(quest)
            results[result_index] = tuple(result)
        return set(results)






    @staticmethod
    def permutate_quest_solutions(solutions: dict[str: list[list]], keys: list[str], current_solution: [], bestResourceSolution: BestResourceSolution):
        key = keys.pop()
        for solution in solutions[key]:
            if len(keys) == 0:
                current_solution.append(solution)
                bestResourceSolution.append_solution_inverted(current_solution, MoritzSolver.calculate_max_rounds_from_array(current_solution))
                current_solution.pop()
                continue
            current_solution.append(solution)
            MoritzSolver.permutate_quest_solutions(solutions, keys, current_solution, bestResourceSolution)
            current_solution.pop()

        keys.append(key)

    @staticmethod
    def calculate_max_rounds_from_array(solution: list[list]):
        _solution = sum([list(ele) for ele in solution], [])
        _map = {}
        for element in _solution:
            if element in _map:
                _map[element] += 1
            else:
                _map[element] = 1

        return max(_map.values())






    @staticmethod
    def calculate_optimal_quest_solutions(quest: Quest, ships: list[Ship]) -> list:
        best_solutions = BestResourceSolution()
        MoritzSolver.calculate_optimal_quest_solutions_rec(quest.demand, ships, [], best_solutions)
        return best_solutions.results


    @staticmethod
    def calculate_optimal_quest_solutions_rec(remaining_resources: int, ships: list[Ship], current_steps: list[Ship], bestSolution: BestResourceSolution, currentIndex=0):
        if remaining_resources <= 0:
            bestSolution.append_solution(current_steps, remaining_resources)
            return

        for i in range(currentIndex, len(ships)):
            ship = ships[i]
            #if ship in current_steps and ship is not current_steps[-1]:
            #    continue
            current_steps.append(ship)
            MoritzSolver.calculate_optimal_quest_solutions_rec(remaining_resources - ship.capacity, ships, current_steps, bestSolution, i)
            current_steps.pop()





    @staticmethod
    def calculate_remaining_resources(ships: list[Ship], steps: list[Step]) -> RoundPerformance:
        performance = RoundPerformance(0)
        for step in steps:
            MoritzSolver.apply_step(
                MoritzSolver.get_ship_by_id(step.ship_id, ships),
                step)
            performance.outstanding += step.quest_capacity
            performance.performance += step.spare_capacity
        return performance

    @staticmethod
    def apply_step(ship: Ship, step: Step):
        step.spare_capacity = step.quest_capacity - ship.capacity
        step.quest_capacity = max(step.quest_capacity - ship.capacity, 0)

    @staticmethod
    def create_all_permutations(ships, quests) -> set:
        mapping = []
        if ships > quests:
            while len(quests) < len(ships):
                quests.append(None)
        for ships in ships:
            for quest in quests:
                mapping.append(BaseStep(quest, ships))

        return set(mapping)


    @staticmethod
    def sort_mapping_by_quest_id(mapping: set[BaseStep]):
        sorted_mapping = {}
        for element in mapping:
            if not element.quest in mapping:
                sorted_mapping[element.quest] = []
            sorted_mapping[element.quest].append(element.ship)
        return sorted_mapping

    @staticmethod
    def get_ship_by_id(ship_id: str, ships: list[Ship]) -> Ship:
        if ship_id == None:
            return None
        for ship in ships:
            if ship.id == ship_id:
                return ship
        return None

    @staticmethod
    def get_quest_by_id(quest_id: str, quests: list[Quest]) -> Quest:
        for quest in quests:
            if quest.id == quest_id:
                return quest
        return None
