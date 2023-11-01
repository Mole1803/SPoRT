from _DatabaseCall import db, Users as UserDB
from hashlib import sha256
import os


class AuthService:

    def create_user(self, username, password) -> UserDB:
        salt = self.__create_salt()
        password_hash = sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        user = UserDB(name=username, password=password_hash, salt=salt)
        db.session.add(user)
        db.session.commit()
        return user

    def verify_user(self, username, password) -> UserDB:
        salt = self.__get_salt(username)
        password_hash = sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        return UserDB.query.filter_by(name=username, password=password_hash).first()

    @staticmethod
    def __get_salt(username):
        return UserDB.query.filter_by(name=username).first().salt

    @staticmethod
    def __create_salt():
        return os.urandom(32).hex()

