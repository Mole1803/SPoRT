from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Solver.Solver import Solver
from SeaPortOptimizerBackend.src.Model.Quest import Quest
from SeaPortOptimizerBackend.src.Model.Ship import Ship
from SeaPortOptimizerBackend.src.Model.Step import Step


class BestSolution:
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

    def calculate_time_optimized(self) -> list[Result]:
        for quest in self.quests:
            quest.demand = quest.demand / quest.items_per_capacity

        return MoritzSolver._calculate_time_optimized(self.quests, self.ships)

    def calculate_resource_optimized(self):
        return MoritzSolver._calculate_resource_optimized(self.quests, self.ships)

    @staticmethod
    def _calculate_time_optimized(quests: [Quest], ships: [Ship]) -> list[Result]:
        best_solution = BestSolution(float("inf"))
        max_round_dict = {}
        for ship in ships:
            max_round_dict[ship.id] = 0
        MoritzSolver.time_optimized_rec(quests[0].demand, ships, [], best_solution, 0, quests, 0, [],max_round_dict)
        filtered_best_solutions = MoritzSolver._time_optimized_filtered_by_resource(best_solution)
        filtered_best_solutions.results = MoritzSolver.filter_permutations(filtered_best_solutions.results)
        print(filtered_best_solutions.results)
        steps_list = MoritzSolver.solution_to_steps(filtered_best_solutions.results, quests)
        build_rounds = MoritzSolver.build_rounds(steps_list, best_solution.value)
        return build_rounds


    @staticmethod
    def _time_optimized_filtered_by_resource(bestSolution: BestSolution) -> BestSolution:
        filtered_best_solutions = BestSolution(float("inf"))
        for solution in bestSolution.results:
            filtered_best_solutions.append_solution_inverted(solution, MoritzSolver.calculate_performance(solution))
        return filtered_best_solutions

    @staticmethod
    def calculate_performance(solution: tuple[tuple]):
        performance = 0
        for i, quest in enumerate(solution):
            for ship in quest:
                performance += ship.capacity
        return performance

    @staticmethod
    def time_optimized_rec(remaining_resource: float, ships: list[Ship], current_steps: list,
                           best_solution: BestSolution, current_ship: int, quests: list[Quest], current_quest: int,
                           current_solution: list, max_value_dict):

        max_rounds = MoritzSolver.max_rounds_from_map(max_value_dict)
        if max_value_dict[ships[current_ship].id] > best_solution.value:
            return


        if current_quest >= len(quests):
            # Todo prüfe ob aktuelle quest lösung besser ist als bisherige
            #max_rounds = MoritzSolver.max_rounds_from_map(max_value_dict)#MoritzSolver.calculate_max_rounds_from_array(current_solution)
            best_solution.append_solution_inverted(current_solution, max_rounds)
            return

        if remaining_resource <= 0:
            current_solution.append(tuple(current_steps))
            new_remaining_resource = 0
            if current_quest < len(quests)-1:
                new_remaining_resource = quests[current_quest + 1].demand
            MoritzSolver.time_optimized_rec(new_remaining_resource, ships, [], best_solution, 0, quests,
                                            current_quest + 1, current_solution, max_value_dict)
            current_solution.pop()
            return

        for i, ship in enumerate(ships):
            if ship in current_steps and ship is not current_steps[-1]:
                continue
            max_value_dict[ship.id] = max_value_dict.get(ship.id) + 1
            current_steps.append(ship)
            MoritzSolver.time_optimized_rec(remaining_resource - ship.capacity, ships, current_steps, best_solution, i,
                                            quests, current_quest, current_solution, max_value_dict)
            max_value_dict[ship.id] = max_value_dict.get(ship.id) - 1
            current_steps.pop()


    @staticmethod
    def max_rounds_from_map(map: dict[str: int]):
        return max(map.values())

    @staticmethod
    def _calculate_resource_optimized(quests, ships):
        solutions_per_quest = {}
        for quest in quests:
            solutions_per_quest[quest.id] = MoritzSolver.calculate_optimal_quest_solutions(quest, ships)
        best_resource_solution = BestSolution(float("inf"))
        MoritzSolver.permutate_quest_solutions(solutions_per_quest, list(solutions_per_quest.keys()), [],
                                               best_resource_solution)
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
        results: list[list] = [[Round() for y in range(max_rounds)] for x in range(len(steps_list))]
        for i, solution in enumerate(steps_list):
            for step in solution:
                for round_index in range(len(results[i])):
                    if results[i][round_index].step_in_round(step):
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
    def permutate_quest_solutions(solutions: dict[str: list[list]], keys: list[str], current_solution: [],
                                  bestResourceSolution: BestSolution):
        key = keys.pop()
        for solution in solutions[key]:
            if len(keys) == 0:
                current_solution.append(solution)
                bestResourceSolution.append_solution_inverted(current_solution,
                                                              MoritzSolver.calculate_max_rounds_from_array(
                                                                  current_solution))
                current_solution.pop()
                continue
            current_solution.append(solution)
            MoritzSolver.permutate_quest_solutions(solutions, keys, current_solution, bestResourceSolution)
            current_solution.pop()

        keys.append(key)

    @staticmethod
    def calculate_max_rounds_from_array(solution: list[list]) -> int:
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
        best_solutions = BestSolution()
        MoritzSolver.calculate_optimal_quest_solutions_rec(quest.demand / quest.items_per_capacity, ships, [],
                                                           best_solutions)
        return best_solutions.results

    @staticmethod
    def calculate_optimal_quest_solutions_rec(remaining_resources: int, ships: list[Ship], current_steps: list[Ship],
                                              bestSolution: BestSolution, currentIndex=0):
        if remaining_resources <= 0:
            bestSolution.append_solution(current_steps, remaining_resources)
            return

        for i in range(currentIndex, len(ships)):
            ship = ships[i]
            # if ship in current_steps and ship is not current_steps[-1]:
            #    continue
            current_steps.append(ship)
            MoritzSolver.calculate_optimal_quest_solutions_rec(remaining_resources - ship.capacity, ships,
                                                               current_steps, bestSolution, i)
            current_steps.pop()


if __name__ == '__main__':
    ships = [
        Ship("TestUser", "ship1", "id_1", True, 20),
        Ship("TestUser", "ship2", "id_2", True, 50),
        Ship("TestUser", "ship3", "id_3", True, 10),
    ]

    quests = [Quest("TestUser", "quest1", "quest_id_1", True, "Stein", 1, 100),
              Quest("TestUser", "quest2", "quest_id_2", True, "Stein", 1, 100)]

    print(len(MoritzSolver._calculate_time_optimized(quests, ships)))
