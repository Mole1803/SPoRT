
class Round:
    def __init__(self, steps=None):
        if steps is None:
            steps = []
        self.steps = steps

    def add_step(self, step):
        self.steps.append(step)

    def __dict__(self):
        round_list = {"steps": []}
        #round_list = []
        for step in self.steps:
            round_list["steps"].append(step.__dict__())
            #round_list.append(step.__dict__())
        return round_list

    def step_in_round(self, step):
        #print(self.steps)
        for _step in self.steps:
            if _step.ship_id == step.ship_id:
                #print(_step.ship_id, step.ship_id)
                return True
        return False
