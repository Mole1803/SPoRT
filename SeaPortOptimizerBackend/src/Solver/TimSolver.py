from SeaPortOptimizerBackend.src.Solver.Solver import Solver
from SeaPortOptimizerBackend.src.Model.Result import Result
from SeaPortOptimizerBackend.src.Model.Round import Round
from SeaPortOptimizerBackend.src.Model.Step import Step


class TimSolver:
    def __init__(self, ships_para, quests_para):
        # super().__init__(id)
        self.ships = ships_para
        self.quests = quests_para

        self.temp_ships = self.ships[:]
        self.temp_quests = self.quests[:]
        self.shared_congruent_modulos = 1
        self.results = []

    def calculate_time_optimized(self):
        pass

    def calculate_resource_optimized(self):
        return self.start_resource_optimized_result()

    def start_resource_optimized_result(self):
        temp_result = Result([])
        while self.check_for_active_quests():
            current_round = self.fill_ships_optimized(Round([]))
            current_round = self.fill_ships_unoptimized(current_round)
            temp_result.rounds.append(current_round)
            self.reset_ship_status()
        return temp_result

    def fill_ships_optimized(self, round_para):
        for ship in self.ships:
            if ship.is_active:
                for quest in self.temp_quests:
                    if (ship.capacity == quest.demand) and quest.is_active:
                        # Set ship as used for this round and the quest as complete
                        ship.is_active = False
                        quest.is_active = False
                        quest.demand = 0
                        # Append Step to round
                        round_para.steps.append(Step(ship.id, quest.id, 0))
                        # Break Quest for loop because ship is used
                        break
        return round_para

    def fill_ships_unoptimized(self, round_para):
        for ship in self.ships:
            if ship.is_active:
                for quest in self.temp_quests:
                    if quest.demand % ship.capacity == 0 and quest.is_active and \
                            self.check_tolerance(ship, quest):
                        # Set ship as used for this round and substract the ship capacity from the quest demand
                        ship.is_active = False
                        quest.demand = quest.demand - ship.capacity
                        # Set quest to inactive if demand is 0
                        if quest.demand == 0:
                            quest.is_active = False
                        # Append Step to round
                        round_para.steps.append(Step(ship.id, quest.id, 0))
                        break
        return round_para

    def check_tolerance(self, ship_para, quest_para):
        temp_counter = 0
        for ship in self.ships:
            if ship.is_active:
                if ((ship.capacity % ship_para.capacity == 0) or\
                    (ship_para.capacity % ship.capacity == 0)) and \
                        ship.capacity % quest_para.demand == 0:
                    temp_counter += 1
        if temp_counter >= self.shared_congruent_modulos:
            return True
        else:
            return False

    def check_for_active_quests(self):
        for quest in self.temp_quests:
            if quest.is_active:
                return True
        return False

    def reset_ship_status(self):
        for ship in self.ships:
            ship.is_active = True
