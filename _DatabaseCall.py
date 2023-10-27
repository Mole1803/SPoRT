from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///project.db'
db.init_app(app)


class Users(db.Model):
    name: Mapped[str] = mapped_column(db.String, nullable=False, primary_key=True)
    password: Mapped[str] = mapped_column(db.String, nullable=False)
    salt: Mapped[str] = mapped_column(db.String, nullable=False)

    def serialize(self):
        return {
            'name': self.name,
            'password': self.password,
            'salt': self.salt
        }


class Ships(db.Model):
    id: Mapped[str] = mapped_column(db.String, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    isActive: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    capacity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    username: Mapped[str] = mapped_column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'isActive': self.isActive,
            'capacity': self.capacity,
            'username': self.username
        }


class Quests(db.Model):
    id: Mapped[str] = mapped_column(db.String, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    isActive: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    resource: Mapped[str] = mapped_column(db.String, nullable=False)
    demand: Mapped[int] = mapped_column(db.Integer, nullable=False)
    username: Mapped[str] = mapped_column(db.String, nullable=False)
    itemsPerCapacity: Mapped[int] = mapped_column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'isActive': self.isActive,
            'resource': self.resource,
            'demand': self.demand,
            'username': self.username,
            'itemsPerCapacity': self.itemsPerCapacity
        }


with app.app_context():
    db.create_all()
