import os
import jwt as jwt_lib

secret_key = str(os.getenv('SECRET_KEY'))


class UtilityFunctions:
    @staticmethod
    def get_user_from_jwt(_request):
        token = _request.headers.get("Authorization")[7::]
        return jwt_lib.decode(token, secret_key, algorithms=["HS256"])["sub"]#app.config["JWT_SECRET_KEY"]
