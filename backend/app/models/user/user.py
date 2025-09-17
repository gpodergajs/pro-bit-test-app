from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # hashed password
    email = db.Column(db.String(100), unique=True, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'))

    user_type = db.relationship("UserType", back_populates="users", lazy="joined")
    cars = db.relationship("Car", back_populates="owner", lazy="joined")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)