from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from app.models.user import User, UserType

class UserTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserType
        load_instance = True
        include_fk = True

class UserSchema(SQLAlchemyAutoSchema):
    user_type = Nested("UserTypeSchema")
    cars = Nested("CarSchema", many=True, exclude=("owner",))

    class Meta:
        model = User
        load_instance = True
        include_fk = True
