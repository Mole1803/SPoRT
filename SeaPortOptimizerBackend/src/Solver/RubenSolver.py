from math import inf

from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Model.Step import Step
from SeaPortOptimizerBackend.src.Solver.Solver import Solver


def parse_solutions_to_results(best_solutions, number_of_rounds):
    """Takes the best solutions and parses them into Result and add them to the result list
    :param best_solutions of type map<ship_id,Step[]>
    :param number_of_rounds of type int
    :return of type Result[]
    """
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


def get_best_solutions(solutions_by_ships):
    """filter out solutions with more rounds than the best solution
    :param solutions_by_ships of type map<ship_id,Step[]>
    :return list of all best solutions of type map<ship_id,Step[]>
    :return minimum number of rounds of type int
    """
    min = inf
    best_solutions = []
    for solution in solutions_by_ships:
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


def combine_steps(quests, ships):
    """Takes all possible step combinations for each quest and combines them with all step combinations from the other quests
    :param quests: with additional attribute all_steps
    :param ships: all available and active ships
    :return: of type map<ship_id,Step[]>
    """
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
    solutions_by_ships = []
    for solution in solutions:
        ship_quests = {}
        for ship in ships:
            ship_quests[ship.id] = []
        for step in solution:
            ship_quests[step.ship_id].append(step)
        solutions_by_ships.append(ship_quests)
    return solutions_by_ships


def filter_steps(quest):
    """filter out step combinations with more spare capacity than the best step combination
    :param quest: with additional attribute all_steps
    :return: no return modification by reference
    """
    min = inf
    best_steps = []
    for steps in quest.all_steps:
        sum = 0
        for step in steps:
            sum += step.quest_capacity
        if sum < min:
            best_steps = [steps]
            min = sum
        elif sum == min:
            best_steps.append(steps)
    quest.all_steps = best_steps


def filter_solutions_by_capacity(solutions_by_ships, quests):
    """filter out step combinations with more spare capacity than the best step combination
    :param solutions_by_ships: solutions of type map<ship_id,Step[]>
    :param quests: quests with demand
    :return: all solutions of type map<ship_id,Step[]>
    """
    best_solutions = []
    min_spare = inf
    for solution in solutions_by_ships:
        sums = {}
        for quest in quests:
            sums[quest.id] = -1 * quest.demand
        for ship in solution:
            for step in solution[ship]:
                sums[step.quest_id] += step.quest_capacity
        total_sum = 0
        for s_id in sums:
            total_sum += sums[s_id]
        if total_sum < min_spare:
            best_solutions = [solution]
            min_spare = total_sum
        elif total_sum == min_spare:
            best_solutions.append(solution)
    return best_solutions


def calculate_all_steps(quest, ships, steps, index=0):
    """
    :param quest: all quests
    :param ships: all ships
    :param steps: all current steps
    :param index: start index for next ship
    :return: index of the ship / modification on the quest
    """
    i = index
    while i < len(ships):
        if quest.remaining_demand > 0:
            ship = ships[i]
            if ship.capacity < 1:
                return i + 1
            quest.remaining_demand -= quest.items_per_capacity * ship.capacity
            step = Step(ship.id, quest.id, quest.items_per_capacity * ship.capacity)
            if quest.remaining_demand < 0:
                step.set_spare_capacity(-quest.remaining_demand)
            steps.append(step)
            i = calculate_all_steps(quest, ships, steps, i)
        else:
            quest.all_steps.append(steps.copy())
            if len(steps) > 0:
                last_step = steps.pop(-1)
                quest.remaining_demand += last_step.quest_capacity
            return i + 1
    if len(steps) > 0:
        last_step = steps.pop(-1)
        quest.remaining_demand += last_step.quest_capacity
    return index + 1


class RubenSolver(Solver):
    def __init__(self, id):
        super().__init__(id)

    def calculate_time_optimized(self):
        for quest in self.quests:
            quest.all_steps = []
            calculate_all_steps(quest, self.ships, [])
        solutions = combine_steps(self.quests, self.ships)
        best_solutions, rounds = get_best_solutions(solutions)
        ships_by_solutions = filter_solutions_by_capacity(best_solutions, self.quests)
        results = parse_solutions_to_results(ships_by_solutions, rounds)
        return results

    def calculate_resource_optimized(self):
        for quest in self.quests:
            quest.all_steps = []
            calculate_all_steps(quest, self.ships, [])
            filter_steps(quest)
        solutions = combine_steps(self.quests, self.ships)
        best_solutions, rounds = get_best_solutions(solutions)
        results = parse_solutions_to_results(best_solutions, rounds)
        return results
