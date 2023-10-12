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
    id: Mapped[str] = mapped_column(db.String, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Ships(db.Model):
    id: Mapped[str] = mapped_column(db.String, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    isActive: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    capacity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    userID: Mapped[str] = mapped_column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'isActive': self.isActive,
            'capacity': self.capacity,
            'userID': self.userID
        }


class Quests(db.Model):
    id: Mapped[str] = mapped_column(db.String, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    isActive: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    resource: Mapped[str] = mapped_column(db.String, nullable=False)
    demand: Mapped[int] = mapped_column(db.Integer, nullable=False)
    userID: Mapped[str] = mapped_column(db.String, nullable=False)
    itemsPerCapacity: Mapped[int] = mapped_column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'isActive': self.isActive,
            'resource': self.resource,
            'demand': self.demand,
            'userID': self.userID,
            'itemsPerCapacity': self.itemsPerCapacity
        }


with app.app_context():
    db.create_all()
