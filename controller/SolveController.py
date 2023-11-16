from flask import request,Blueprint
from flask_jwt_extended import jwt_required

from SeaPortOptimizerBackend.src.Solver.MarcelSolver import MarcelSolver
from SeaPortOptimizerBackend.src.Solver.MoritzSolver import MoritzSolver
from SeaPortOptimizerBackend.src.Solver.RubenSolver import RubenSolver
from SeaPortOptimizerBackend.src.Solver.TimSolver import TimSolver
from utils.utility_functions import UtilityFunctions

solver_controller = Blueprint('solver_controller', __name__, url_prefix='/solve')

class SolveController:
    def __init__(self,app):
        app.register_blueprint(solver_controller)
    @staticmethod
    @jwt_required()
    @solver_controller.route('', methods=["POST"])
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

        if not solver.verify_valid():

            return [], 200

        if "Time" in algorithm:
            results = solver.calculate_time_optimized()
        elif "Resource" in algorithm:
            results = solver.calculate_resource_optimized()
        else:
            return "Invalid calculation method", 418
        #results_list = {"results": []}
        results_list = []
        for result in results:
            #results_list["results"].append(results[i].dict())
            results_list.append(result.dict())
        print(results_list)
        print(len(results_list))
        return results_list, 200
