# /backend/app/schemas/car_schemas.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from app.models.car import Car, CarModel, CarBrand, BodyType, EngineType, TransmissionType, DriveType

class BodyTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BodyType
        load_instance = True
        include_fk = True

class EngineTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EngineType
        load_instance = True
        include_fk = True

class TransmissionTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TransmissionType
        load_instance = True
        include_fk = True

class DriveTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DriveType
        load_instance = True
        include_fk = True

class CarBrandSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CarBrand
        load_instance = True
        include_fk = True

class CarModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CarModel
        load_instance = True
        include_fk = True

class CarSchema(SQLAlchemyAutoSchema):
    model = Nested("CarModelSchema", only=("id", "name"))
    body_type = Nested("BodyTypeSchema")
    engine_type = Nested("EngineTypeSchema")
    transmission_type = Nested("TransmissionTypeSchema")
    drive_type = Nested("DriveTypeSchema")
    owner = Nested("UserSchema", only=("id", "username"))

    class Meta:
        model = Car
        load_instance = True
        include_fk = True
