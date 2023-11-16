
class Round:
    def __init__(self, steps=None):
        if steps is None:
            steps = []
        self.steps = steps

    def add_step(self, step):
        self.steps.append(step)

    def dict(self):
        round_list = {"steps": []}
        for step in self.steps:
            round_list["steps"].append(step.dict())
        return round_list

    def step_in_round(self, step):
        for _step in self.steps:
            if _step.ship_id == step.ship_id:
                return True
        return False
