
class Round:
    def __init__(self, steps):
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

    def __iter__(self):
        for step in self.steps:
            yield step

    def __eq__(self, other):
        for step in self.steps:
            if step not in other:
                return False
        return True
