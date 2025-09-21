from app import db

class UserType(db.Model):
    __tablename__ = 'user_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    users = db.relationship("User", back_populates="user_type", lazy="joined")

    def __repr__(self):
        return f"<UserType(name={self.name})>"
