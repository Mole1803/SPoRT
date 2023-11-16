from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Model.Step import Step
from SeaPortOptimizerBackend.src.Solver.Solver import Solver

import copy


class TimSolver(Solver):
    def __init__(self,id):
        super().__init__(id)

        self.possible_steps = []
        self.possible_results = []

    def filter_best_results(self):
        fastest_result = self.possible_results[0]
        best_possible_results = []
        for result in self.possible_results:
            if len(result.rounds) < len(fastest_result.rounds):
                fastest_result = result
        for result in self.possible_results:
            if len(result.rounds) == len(fastest_result.rounds):
                best_possible_results.append(result)
        self.possible_results = best_possible_results

    def calculate_time_optimized(self):
        self.possible_results = []
        self.start_time_optimized_round([], copy.deepcopy(self.ships), copy.deepcopy(self.quests))
        if len(self.possible_results) > 0:
            self.filter_best_results()
            return self.possible_results
        return []

    def calculate_resource_optimized(self):
        self.possible_results = []
        self.start_resource_optimized_round([], copy.deepcopy(self.ships), copy.deepcopy(self.quests))
        if len(self.possible_results) > 0:
            self.filter_best_results()
            return self.possible_results
        return []

    def start_time_optimized_round(self, rounds_list_para, ships_para, quests_para):
        rounds_list_para.append(Round())
        quests = copy.deepcopy(quests_para)
        start_steps, ships, quests = self.fill_ships_ideal([], ships_para, quests)
        if len(quests) == 0:
            rounds_list_para.remove(rounds_list_para[-1])
            self.possible_results.append(Result(rounds_list_para))
            return
        steps_list = self.fill_ships_optimized(start_steps, self.remove_used_ships(start_steps, ships), quests)
        if len(steps_list) == 0:
            final_steps_list = self.fill_remaining_ships_time_opt(start_steps,
                                                                  self.remove_used_ships(start_steps, ships),
                                                                  quests)
            if len(final_steps_list) == 0:
                if len(start_steps) == 0:
                    return
                else:
                    rounds_list_para[-1].steps = start_steps
                    self.start_time_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                    quests)
            else:
                for final_steps in final_steps_list:
                    quests = self.update_quest_demands(final_steps, copy.deepcopy(quests))
                    rounds_list_para[-1].steps = final_steps
                    self.start_time_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                    quests)
        else:
            for steps in steps_list:
                quests = self.remove_completed_quests(steps, quests)
                if len(quests) == 0:
                    rounds_list_para[-1].steps = steps
                    self.possible_results.append(Result(copy.deepcopy(rounds_list_para)))
                    return
                final_steps_list = self.fill_remaining_ships_time_opt(steps, self.remove_used_ships(steps, ships),
                                                                      quests)
                if len(final_steps_list) == 0:
                    rounds_list_para[-1].steps = steps
                    self.start_time_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                    quests)
                else:
                    for final_steps in final_steps_list:
                        quests = self.update_quest_demands(final_steps, copy.deepcopy(quests))
                        rounds_list_para[-1].steps = final_steps
                        self.start_time_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                        quests)

    def start_resource_optimized_round(self, rounds_list_para, ships_para, quests_para):
        rounds_list_para.append(Round())
        quests = copy.deepcopy(quests_para)
        start_steps, ships, quests = self.fill_ships_ideal([], ships_para, quests)
        if len(quests) == 0:
            rounds_list_para.remove(rounds_list_para[-1])
            self.possible_results.append(Result(rounds_list_para))
            return
        steps_list = self.fill_ships_optimized(start_steps, self.remove_used_ships(start_steps, ships), quests)
        if len(steps_list) == 0:
            final_steps_list = self.fill_remaining_ships_resource_opt(start_steps,
                                                                      self.remove_used_ships(start_steps, ships),
                                                                      quests)
            if len(final_steps_list) == 0:
                if len(start_steps) == 0:
                    return
                else:
                    rounds_list_para[-1].steps = start_steps
                    self.start_resource_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                        quests)
            else:
                for final_steps in final_steps_list:
                    quests = self.update_quest_demands(final_steps, copy.deepcopy(quests))
                    rounds_list_para[-1].steps = final_steps
                    self.start_resource_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                        quests)
        else:
            for steps in steps_list:
                quests = self.remove_completed_quests(steps, quests)
                if len(quests) == 0:
                    rounds_list_para[-1].steps = steps
                    self.possible_results.append(Result(copy.deepcopy(rounds_list_para)))
                    return
                final_steps_list = self.fill_remaining_ships_resource_opt(steps, self.remove_used_ships(steps, ships),
                                                                          quests)
                if len(final_steps_list) == 0:
                    rounds_list_para[-1].steps = steps
                    self.start_resource_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                        quests)
                else:
                    for final_steps in final_steps_list:
                        quests = self.update_quest_demands(final_steps, copy.deepcopy(quests))
                        rounds_list_para[-1].steps = final_steps
                        self.start_resource_optimized_round(copy.deepcopy(rounds_list_para), copy.deepcopy(self.ships),
                                                            quests)

    @staticmethod
    def fill_ships_ideal(lilst_of_steps, list_of_ships, list_of_quests):
        for ship in list_of_ships:
            if ship.is_active:
                for quest in list_of_quests:
                    if (ship.capacity == quest.demand) and quest.is_active:
                        # Set ship as used for this round and the quest as complete
                        ship.is_active = False
                        list_of_quests.remove(quest)
                        # Append Step to round
                        lilst_of_steps.append(Step(ship.id, quest.id, 0))
                        # Break Quest for loop because ship is used
                        break
        return lilst_of_steps, list_of_ships, list_of_quests

    def fill_ships_optimized(self, list_of_steps, list_of_ships, list_of_quests):
        list_of_possible_steps = []
        for quest in list_of_quests:
            self.try_opt_fill_sequences(copy.deepcopy(list_of_steps), quest,
                                        copy.deepcopy(list_of_ships), 0, len(list_of_ships))
            list_of_possible_steps += self.possible_steps
            self.possible_steps = []
        if len(list_of_possible_steps) > 0:
            list_of_possible_steps = self.merge_possible_steps_together(copy.deepcopy(list_of_possible_steps))
            list_of_possible_steps = self.remove_permutations(copy.deepcopy(list_of_possible_steps))
        return list_of_possible_steps

    def try_opt_fill_sequences(self, list_of_steps, quest, list_of_ships, fullfilled_demand, tries):
        for ship in list_of_ships:
            if ship.capacity <= (quest.demand - fullfilled_demand):
                temp_fullfilled_demand = fullfilled_demand + ship.capacity
                temp_list_of_steps = copy.deepcopy(list_of_steps)
                temp_list_of_ships = copy.deepcopy(list_of_ships)
                temp_list_of_steps.append(Step(ship.id, quest.id, 0))
                temp_list_of_ships = self.remove_ship_by_id(ship.id, temp_list_of_ships)
                temp_tries = tries - 1
                if temp_fullfilled_demand == quest.demand:
                    self.possible_steps.append(temp_list_of_steps)
                if tries != 0:
                    self.try_opt_fill_sequences(copy.deepcopy(temp_list_of_steps),
                                                copy.deepcopy(quest),
                                                copy.deepcopy(temp_list_of_ships),
                                                temp_fullfilled_demand, temp_tries)

    def fill_remaining_ships_resource_opt(self, list_of_steps, list_of_ships, list_of_quests):
        list_of_possible_steps = []
        for quest in list_of_quests:
            self.try_poss_fill_sequences_resource_opt(copy.deepcopy(list_of_steps), copy.deepcopy(quest),
                                                      self.remove_used_ships(list_of_steps,
                                                                             copy.deepcopy(list_of_ships)), 0)
            list_of_possible_steps += self.possible_steps
            self.possible_steps = []
        if len(list_of_possible_steps) > 0:
            list_of_possible_steps = self.merge_possible_steps_together(copy.deepcopy(list_of_possible_steps))
            list_of_possible_steps = self.remove_permutations(copy.deepcopy(list_of_possible_steps))
        return list_of_possible_steps

    def try_poss_fill_sequences_resource_opt(self, list_of_steps, quest, list_of_ships, capacity_sum):
        for ship in list_of_ships:
            if ship.capacity + capacity_sum <= quest.demand:
                temp_sum = capacity_sum + ship.capacity
                temp_list_of_steps = copy.deepcopy(list_of_steps)
                temp_list_of_ships = copy.deepcopy(list_of_ships)
                temp_list_of_steps.append(Step(ship.id, quest.id, 0))
                temp_list_of_ships = self.remove_ship_by_id(ship.id, temp_list_of_ships)
                if (ship.capacity == quest.demand / 2 and len(list_of_steps) == 0) or \
                        self.check_ship_options(quest.demand - temp_sum, self.ships, True):
                    self.possible_steps.append(copy.deepcopy(temp_list_of_steps))
                if self.check_ship_options(quest.demand - temp_sum, temp_list_of_ships, False):
                    self.try_poss_fill_sequences_resource_opt(copy.deepcopy(temp_list_of_steps),
                                                              copy.deepcopy(quest),
                                                              copy.deepcopy(temp_list_of_ships), temp_sum)
                else:
                    if self.check_for_congruenz(quest.demand - temp_sum):
                        self.possible_steps.append(copy.deepcopy(temp_list_of_steps))

    def fill_remaining_ships_time_opt(self, list_of_steps, list_of_ships, list_of_quests):
        list_of_possible_steps = []
        for quest in list_of_quests:
            self.try_poss_fill_sequences_time_opt(copy.deepcopy(list_of_steps), copy.deepcopy(quest),
                                                  self.remove_used_ships(list_of_steps, copy.deepcopy(list_of_ships)),
                                                  0)
            list_of_possible_steps += self.possible_steps
            self.possible_steps = []
        if len(list_of_possible_steps) > 0:
            list_of_possible_steps = self.merge_possible_steps_together(copy.deepcopy(list_of_possible_steps))
            list_of_possible_steps = self.remove_permutations(copy.deepcopy(list_of_possible_steps))
        return list_of_possible_steps

    def try_poss_fill_sequences_time_opt(self, list_of_steps, quest, list_of_ships, capacity_sum):
        for ship in list_of_ships:
            if capacity_sum < quest.demand:
                temp_sum = capacity_sum + ship.capacity
                temp_list_of_steps = copy.deepcopy(list_of_steps)
                temp_list_of_ships = copy.deepcopy(list_of_ships)
                if temp_sum > quest.demand:
                    temp_list_of_steps.append(Step(ship.id, quest.id, abs(quest.demand - temp_sum)))
                    self.possible_steps.append(copy.deepcopy(temp_list_of_steps))
                else:
                    temp_list_of_steps.append(Step(ship.id, quest.id, 0))
                    temp_list_of_ships = self.remove_ship_by_id(ship.id, temp_list_of_ships)
                    if len(temp_list_of_ships) != 0:
                        self.try_poss_fill_sequences_time_opt(copy.deepcopy(temp_list_of_steps),
                                                              copy.deepcopy(quest),
                                                              copy.deepcopy(temp_list_of_ships), temp_sum)
                    else:
                        self.possible_steps.append(copy.deepcopy(temp_list_of_steps))

    def check_for_congruenz(self, quest_demand):
        tolerance = int(len(self.ships) / 2)
        for ship in self.ships:
            if ((quest_demand % ship.capacity == 0) or
                (ship.capacity % quest_demand == 0)) and \
                    ship.capacity <= quest_demand:
                if ship.capacity == quest_demand:
                    return True
                tolerance -= 1
        if tolerance <= 0:
            return True
        else:
            return False

    def update_quest_demands(self, list_of_steps, list_of_quests):
        for quest in list_of_quests:
            for step in list_of_steps:
                if step.quest_id == quest.id:
                    for ship in self.ships:
                        if ship.id == step.ship_id:
                            quest.demand -= ship.capacity
                            break
            if quest.demand <= 0:
                list_of_quests.remove(quest)
        return list_of_quests

    @staticmethod
    def check_ship_options(demand, list_of_ships, check):
        for ship in list_of_ships:
            if check:
                if ship.capacity == demand:
                    return True
            else:
                if ship.capacity <= demand:
                    return True
        return False

    @staticmethod
    def remove_ship_by_id(id, list_of_ships):
        for ship in list_of_ships:
            if ship.id == id:
                list_of_ships.remove(ship)
                break
        return list_of_ships

    @staticmethod
    def remove_used_ships(list_of_steps, list_of_ships):
        for step in list_of_steps:
            for ship in list_of_ships:
                if step.ship_id == ship.id:
                    list_of_ships.remove(ship)
                    break
        return list_of_ships

    @staticmethod
    def remove_completed_quests(list_of_steps, list_of_quests):
        for step in list_of_steps:
            for quest in list_of_quests:
                if step.quest_id == quest.id:
                    list_of_quests.remove(quest)
        return list_of_quests

    @staticmethod
    def remove_permutations(list_of_steps):
        permutated_list_of_steps = list_of_steps[:]
        new_list_of_steps = []
        while True:
            new_list_of_steps.append(permutated_list_of_steps[0])
            permutated_list_of_steps.remove(permutated_list_of_steps[0])
            counter = len(new_list_of_steps[-1])
            for steps in permutated_list_of_steps:
                if len(steps) == len(new_list_of_steps[-1]):
                    for step in steps:
                        for new_step in new_list_of_steps[-1]:
                            if step.ship_id == new_step.ship_id and \
                                    step.quest_id == new_step.quest_id and \
                                    step.spare_capacity == new_step.spare_capacity:
                                counter -= 1
                    if counter == 0:
                        permutated_list_of_steps.remove(steps)
            if len(permutated_list_of_steps) == 0:
                break
        return new_list_of_steps

    @staticmethod
    def merge_possible_steps_together(list_of_steps):
        merged_list_of_steps = []
        check = False
        for steps in list_of_steps:
            for other_steps in list_of_steps:
                for step in steps:
                    if check:
                        break
                    for other_step in other_steps:
                        if step.ship_id == other_step.ship_id:
                            check = True
                            break
                if check is not True:
                    merged_list_of_steps.append(steps + other_steps)
                check = False
        return list_of_steps