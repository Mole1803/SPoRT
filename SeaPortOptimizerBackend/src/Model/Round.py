
class Round:
    def __init__(self, steps):
        self.steps = steps

    def __getitem__(self, index):
        return self.steps[index]
