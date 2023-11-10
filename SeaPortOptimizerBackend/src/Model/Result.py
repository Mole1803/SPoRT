class Result:
    def __init__(self, rounds):
        self.rounds = rounds


    def __dict__(self):
        result_list = {"rounds": []}
        #result_list = []
        for round in self.rounds:
            result_list["rounds"].append(round.__dict__())
            #result_list.append(self.rounds[i].__dict__())
        return result_list
