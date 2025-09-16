import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
import random

from app.models import Car


fake = Faker()

class CarFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Car
        ##sqlalchemy_session = Car.query.session  # the SQLAlchemy session object
        sqlalchemy_session_persistence = "flush"

    make = factory.Iterator(["Toyota", "Ford", "Tesla", "BMW", "Audi", "Mercedes"])
    model = factory.Faker("word")
    year = factory.LazyAttribute(lambda _: random.randint(1995, 2025))
    price = factory.LazyAttribute(lambda _: random.randint(5000, 100000))