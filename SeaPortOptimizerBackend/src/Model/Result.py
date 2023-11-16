class Result:
    def __init__(self, rounds):
        self.rounds = rounds

    def __dict__(self):
        result_list = {"rounds": []}
        for round in self.rounds:
            result_list["rounds"].append(round.__dict__())
        return result_list

    def __getitem__(self, item):
        return self.rounds[item]

    def __len__(self):
        return len(self.rounds)

    def __iter__(self):
        for round in self.rounds:
            yield round

    def __eq__(self, other):
        for round in self.rounds:
            if round not in other:
                return False
        return True
