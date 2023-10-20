class Result:
    def __init__(self, rounds):
        self.rounds = rounds

    def __str__(self):
        res = ""
        for i in range(len(self.rounds)):
            res += f"Round {i+1}: \n"
            for step in self.rounds[i].steps:
                res += f"ship: {step.ship_id}, quest: {step.quest_id}, capacity: {step.quest_capacity} "
            res += "\n"
        return res