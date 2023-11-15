from math import inf

from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Model.Step import Step
from SeaPortOptimizerBackend.src.Solver.Solver import Solver


def build_recursive_solutions_for_quest_ressource(ships, demand, quest_id, steps_result_list, result, lowestIndexForShip):
    remaining_demand = demand
    base_result = result.copy()
    for i in range(lowestIndexForShip, len(ships)):
        demand -= ships[i].capacity
        result.append(Step(ships[i].id, quest_id, ships[i].capacity))
        if demand > 0:
            steps_result_list = build_recursive_solutions_for_quest_ressource(ships, demand, quest_id, steps_result_list, result, i)
        else:
            if steps_result_list.remaining_demand == demand * -1:
                steps_result_list.addSteps([result])
            elif steps_result_list.remaining_demand > demand * -1:
                steps_result_list.setSteps([result])
                steps_result_list.remaining_demand = demand * -1
        demand = remaining_demand
        result = base_result.copy()
    return steps_result_list


def build_solutions_for_quest_ressource(ships, demand, quest_id):
    remaining_demand = demand
    # results_as_steps = []
    results_as_steps = Solutions()
    for i in range(len(ships)):
        demand -= ships[i].capacity
        steps = [Step(ships[i].id, quest_id, ships[i].capacity)]
        if demand > 0:
            results_as_steps = build_recursive_solutions_for_quest_ressource(ships, demand, quest_id, results_as_steps, steps, i)
        else:
            if results_as_steps.remaining_demand == demand * -1:
                results_as_steps.addSteps([steps])
            elif results_as_steps.remaining_demand > demand * -1:
                results_as_steps.setSteps([steps])
                results_as_steps.remaining_demand = demand * -1
        demand = remaining_demand
    return results_as_steps


def build_recursive_solutions_for_quest_time_critical(ships, demand, quest_id, steps_result_list, result, lowestIndexForShip):
    remaining_demand = demand
    base_result = result.copy()
    for i in range(lowestIndexForShip, len(ships)):
        demand -= ships[i].capacity
        result.append(Step(ships[i].id, quest_id, ships[i].capacity))
        if demand > 0:
            steps_result_list = build_recursive_solutions_for_quest_time_critical(ships, demand, quest_id, steps_result_list, result,
                                                                    i)
        else:
            steps_result_list.append((result, demand * -1))
        demand = remaining_demand
        result = base_result.copy()
    return steps_result_list


def build_solutions_for_quest_time_critical(ships, demand, quest_id):
    remaining_demand = demand
    results_as_steps = []
    for i in range(len(ships)):
        demand -= ships[i].capacity
        steps = [Step(ships[i].id, quest_id, ships[i].capacity)]
        if demand > 0:
            results_as_steps = build_recursive_solutions_for_quest_time_critical(ships, demand, quest_id, results_as_steps, steps, i)
        else:
            results_as_steps.append((steps, demand * -1))
        demand = remaining_demand
    return results_as_steps


def ship_not_in_round(ship_id, round):
    for step in round:
        if step.ship_id == ship_id:
            return False
    return True


def build_result_with_solutions_ressource(result):
    rounds = [Round([])]
    for step in result:
        added = False
        for round in rounds:
            if ship_not_in_round(step.ship_id, round):
                round.add_step(step)
                added = True
                break
        if not added:
            rounds.append(Round([step]))

    return rounds


def build_result_with_solutions_time_critical(result):
    rounds = [Round([])]
    for step in result[0]:
        added = False
        for round in rounds:
            if ship_not_in_round(step.ship_id, round):
                round.add_step(step)
                added = True
                break
        if not added:
            rounds.append(Round([step]))
    return [rounds, result[1]]


def connect_steps_to_results_ressource(solutions, results, index, result):
    base_result = result.copy()
    for possible_solutions in solutions[index]:
        result += possible_solutions
        if index == len(solutions) - 1:
            result = build_result_with_solutions_ressource(result)
            if len(results) == 0 or len(results[0]) == len(result):
                results.append(result)
            elif len(results) > 0 and len(results[0]) > len(result):
                results = [result]
        else:
            results = connect_steps_to_results_ressource(solutions, results, index + 1, result)
        result = base_result.copy()
    return results


def connect_steps_to_results_time_critical(solutions, results, index, result):
    base_result = result[0].copy()
    remaining_demand = result[1]
    for possible_solutions in solutions[index]:
        result[0] += possible_solutions[0]
        result[1] += possible_solutions[1]
        if index == len(solutions) - 1:
            result_ = build_result_with_solutions_time_critical(result)
            if len(results) > 0:
                if len(results[0][0]) > len(result_[0]):
                    results = [result_]
                elif len(results[0][0]) == len(result_[0]):
                    if results[0][1] == result_[1]:
                        results.append(result_)
                    elif results[0][1] > result_[1]:
                        results = [result_]
            else:
                results.append(result_)
        else:
            results = connect_steps_to_results_time_critical(solutions, results, index + 1, result)
        result[0] = base_result.copy()
        result[1] = remaining_demand
    return results


class Solutions:
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
        solutions = []
        for quest in self.quests:
            solutions.append(build_recursive_solutions_for_quest_time_critical(self.ships, quest.demand, quest.id, [], [], 0))
        results = connect_steps_to_results_time_critical(solutions, [], 0, [[], 0])
        solution_return = []
        for result in results:
            solution_return.append(Result(result[0]))
        return solution_return

    def calculate_resource_optimized(self):
        solutions = []
        for quest in self.quests:
            solutions.append(build_solutions_for_quest_ressource(self.ships, quest.demand, quest.id))

        results = connect_steps_to_results_ressource(solutions, [], 0, [])
        solution_return = []
        for result in results:
            solution_return.append(Result(result))
        return solution_return
