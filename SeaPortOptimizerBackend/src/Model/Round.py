
class Round:
    def __init__(self, steps=None):
        if steps is None:
            self.steps = []
        else:
            self.steps = steps

    def __getitem__(self, index):
        return self.steps[index]
