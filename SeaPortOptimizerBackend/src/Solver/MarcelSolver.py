from math import inf

from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Model.Step import Step
from SeaPortOptimizerBackend.src.Solver.Solver import Solver


def create_step_combinations_for_quest_resource_optimized(ships, demand, quest_id, steps_result_list, result, lowestIndexForShip):
    remaining_demand = demand
    base_result = result.copy()
    for i in range(lowestIndexForShip, len(ships)):
        demand -= ships[i].capacity
        result.append(Step(ships[i].id, quest_id, ships[i].capacity))
        if demand > 0:
            steps_result_list = create_step_combinations_for_quest_resource_optimized(ships, demand, quest_id, steps_result_list, result, i)
        else:
            if steps_result_list.remaining_demand == demand * -1:
                steps_result_list.addSteps([result])
            elif steps_result_list.remaining_demand > demand * -1:
                steps_result_list.setSteps([result])
                steps_result_list.remaining_demand = demand * -1
        demand = remaining_demand
        result = base_result.copy()
    return steps_result_list


def create_step_combinations_for_quest_time_optimized(ships, demand, quest_id, steps_result_list, result, lowestIndexForShip):
    remaining_demand = demand
    base_result = result.copy()
    for i in range(lowestIndexForShip, len(ships)):
        demand -= ships[i].capacity
        result.append(Step(ships[i].id, quest_id, ships[i].capacity))
        if demand > 0:
            steps_result_list = create_step_combinations_for_quest_time_optimized(ships, demand, quest_id, steps_result_list, result,
                                                                                  i)
        else:
            steps_result_list.append((result, demand * -1))
        demand = remaining_demand
        result = base_result.copy()
    return steps_result_list


def build_result_from_step_combination(result):
    rounds = [Round([])]
    for step in result:
        added = False
        for round in rounds:
            if not round.step_in_round(step):
                round.add_step(step)
                added = True
                break
        if not added:
            rounds.append(Round([step]))

    return Result(rounds)


def connect_steps_and_create_all_results_resource_optimized(solutions, results, index, result):
    base_result = result.copy()
    for possible_solutions in solutions[index]:
        result += possible_solutions
        if index == len(solutions) - 1:
            build_result = build_result_from_step_combination(result)
            if len(results) == 0 or len(results[0]) == len(build_result):
                results.append(build_result)
            elif len(results) > 0 and len(results[0]) > len(build_result):
                results = [build_result]
        else:
            results = connect_steps_and_create_all_results_resource_optimized(solutions, results, index + 1, result)
        result = base_result.copy()
    return results


def connect_steps_and_create_all_results_time_optimized(solutions, results, index, result):
    base_result = result[0].copy()
    remaining_demand = result[1]
    for possible_solutions in solutions[index]:
        result[0] += possible_solutions[0]
        result[1] += possible_solutions[1]
        if index == len(solutions) - 1:
            build_result = [build_result_from_step_combination(result[0]), result[1]]
            if len(results) > 0:
                if len(results[0][0]) > len(build_result[0]):
                    results = [build_result]
                elif len(results[0][0]) == len(build_result[0]):
                    if results[0][1] == build_result[1]:
                        results.append(build_result)
                    elif results[0][1] > build_result[1]:
                        results = [build_result]
            else:
                results.append(build_result)
        else:
            results = connect_steps_and_create_all_results_time_optimized(solutions, results, index + 1, result)
        result[0] = base_result.copy()
        result[1] = remaining_demand
    return results


class PossibleResultInSteps:
    def __init__(self):
        self.steps = []
        self.remaining_demand = inf

    def setSteps(self, steps):
        self.steps = steps

    def addSteps(self, steps):
        for step in steps:
            self.steps.append(step)

    def __iter__(self):
        for step in self.steps:
            yield step


class MarcelSolver(Solver):
    def __init__(self, id):
        super().__init__(id)

    def calculate_time_optimized(self):
        if not self.ships or not self.quests:
            return [Result([Round()])]
        step_combinations = []
        for quest in self.quests:
            step_combinations.append(create_step_combinations_for_quest_time_optimized(self.ships, quest.demand, quest.id, [], [], 0))
        results_unprepared = connect_steps_and_create_all_results_time_optimized(step_combinations, [], 0, [[], 0])
        results = []
        for result in results_unprepared:
            results.append(Result(result[0]))
        return results

    def calculate_resource_optimized(self):
        if not self.ships or not self.quests:
            return [Result([Round()])]
        step_combinations = []
        for quest in self.quests:
            step_combinations.append(create_step_combinations_for_quest_resource_optimized(self.ships, quest.demand, quest.id, PossibleResultInSteps(), [], 0))

        return connect_steps_and_create_all_results_resource_optimized(step_combinations, [], 0, [])
