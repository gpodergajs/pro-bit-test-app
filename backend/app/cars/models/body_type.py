from app import db

class BodyType(db.Model):
    __tablename__ = 'body_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)  # Sedan, SUV, Hatchback

    def __repr__(self):
        return f"<BodyType(type={self.type})>"
