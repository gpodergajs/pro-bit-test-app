# /backend/app/database/seed/factories.py

from faker import Faker
import factory
from app import db
import random

# Import your models
from app.cars.models import Car, CarBrand, CarModel, EngineType, TransmissionType, BodyType, DriveType
from app.users.models import User, UserType
from werkzeug.security import generate_password_hash

from app.common.enums.user_type_enum import UserTypeEnum

fake = Faker()

# --- Functions to lazily load database choices ---
def get_user_types():
    return UserType.query.all()

def get_engine_types():
    return EngineType.query.all()

def get_transmission_types():
    return TransmissionType.query.all()

def get_drive_types():
    return DriveType.query.all()

def get_body_types():
    return BodyType.query.all()


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"
        abstract = True


class UserFactory(BaseFactory):
    class Meta:
        model = User

      # Placeholder username; real username set after flush
    username = factory.LazyFunction(lambda: "tempuser")
    email = factory.LazyFunction(fake.email)
    user_type = factory.LazyAttribute(lambda o: random.choice(get_user_types()))
    password_hash = factory.LazyFunction(lambda: generate_password_hash("userPassword"))

    @factory.post_generation
    def set_username(obj, create, extracted, **kwargs):
        # Ensure the object has an ID
         if obj.id:
            if obj.user_type.id == UserTypeEnum.ADMIN.value:
                obj.username = f"admin{obj.id}"
                obj.set_password("adminPassword")  # hashed
            else:
                obj.username = f"user{obj.id}"
                obj.set_password("userPassword")  # hashed
                
            db.session.add(obj)
            db.session.flush()    
            
class CarBrandFactory(BaseFactory):
    class Meta:
        model = CarBrand

    name = factory.LazyFunction(lambda: fake.company())

class CarModelFactory(BaseFactory):
    class Meta:
        model = CarModel

    name = factory.LazyFunction(lambda: fake.word().title())
    brand = factory.SubFactory(CarBrandFactory)

class CarFactory(BaseFactory):
    class Meta:
        model = Car

    vin = factory.LazyFunction(lambda: fake.unique.bothify(text="??######??????"))
    license_plate = factory.LazyFunction(lambda: fake.unique.bothify(text="???-####"))
    owner = factory.SubFactory(UserFactory)
    model = factory.SubFactory(CarModelFactory)

    body_type = factory.LazyAttribute(lambda o: random.choice(get_body_types()))
    engine_type = factory.LazyAttribute(lambda o: random.choice(get_engine_types()))
    transmission_type = factory.LazyAttribute(lambda o: random.choice(get_transmission_types()))
    drive_type = factory.LazyAttribute(lambda o: random.choice(get_drive_types()))

    engine_capacity = factory.LazyFunction(lambda: round(random.uniform(1.0, 5.0), 1))
    fuel_consumption = factory.LazyFunction(lambda: round(random.uniform(5.0, 15.0), 1))
    mileage = factory.LazyFunction(lambda: round(random.uniform(0, 200_000), 1))
    color = factory.LazyFunction(lambda: fake.color_name())
    doors = factory.LazyFunction(lambda: random.choice([2, 3, 4, 5]))
    registration_year = factory.LazyFunction(lambda: random.randint(2000, 2025))
    price = factory.LazyFunction(lambda: round(random.uniform(0, 100000), 2))
