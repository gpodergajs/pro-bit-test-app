from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'))

    user_type = db.relationship("UserType", back_populates="users", lazy="joined")
    cars = db.relationship("Car", back_populates="owner", lazy="joined")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"