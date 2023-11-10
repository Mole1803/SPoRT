from flask import request
from flask_jwt_extended import jwt_required

from SeaPortOptimizerBackend.src.Solver.MarcelSolver import MarcelSolver
from SeaPortOptimizerBackend.src.Solver.MoritzSolver import MoritzSolver
from SeaPortOptimizerBackend.src.Solver.RubenSolver import RubenSolver
from SeaPortOptimizerBackend.src.Solver.TimSolver import TimSolver
from controller.BaseController import BaseController
from utils.utility_functions import UtilityFunctions


class SolveController(BaseController, base_route="/solve"):
    @staticmethod
    @jwt_required()
    @BaseController.controllerRoute('', methods=["POST"])
    def Solve():
        user = UtilityFunctions.get_user_from_jwt(request)
        body = request.get_json()
        developer = body["developer"]
        algorithm = body["algorithm"]
        print("dev: ", developer, "algo: ", algorithm)
        if developer == "Ruben":
            solver = RubenSolver(user)
        elif developer == "Marcel":
            solver = MarcelSolver(user)
        elif developer == "Moritz":
            solver = MoritzSolver(user)
        elif developer == "Tim":
            solver = TimSolver(user)
        else:
            return "Invalid developer", 418

        if "Time" in algorithm:
            results = solver.calculate_time_optimized()
        elif "Resource" in algorithm:
            results = solver.calculate_resource_optimized()
        else:
            return "Invalid calculation method", 418
        #results_list = {"results": []}
        results_list = []
        for result in results:
            #results_list["results"].append(results[i].__dict__())
            results_list.append(result.__dict__())
        print(results_list)
        return results_list, 200
