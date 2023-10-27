from app import app
import jwt as jwt_lib


class UtilityFunctions:
    @staticmethod
    def get_user_from_jwt(_request):
        token = _request.headers.get("Authorization")[7::]
        return jwt_lib.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])["sub"]
