import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
import random
from app import db
from app.models.car_model import Car


fake = Faker()

class CarFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Car
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    make = factory.Iterator(["Toyota", "Ford", "Tesla", "BMW", "Audi", "Mercedes"])
    model = factory.Faker("word")
    year = factory.LazyAttribute(lambda _: random.randint(1995, 2025))
    price = factory.LazyAttribute(lambda _: random.randint(5000, 100000))