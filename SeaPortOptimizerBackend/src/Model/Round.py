
class Round:
    def __init__(self, steps):
        self.steps = steps

    def add_step(self, step):
        self.steps.append(step)

    def __dict__(self):
        round_list = []
        for step in self.steps:
            round_list.append(step.__dict__())
        return round_list
