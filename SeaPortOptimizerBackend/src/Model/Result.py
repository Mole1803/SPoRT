class Result:
    def __init__(self, rounds=None):
        self.rounds = rounds

    def append(self, round_para):
        self.rounds.append(round_para)

    def __getitem__(self, index):
        return self.rounds[index]
