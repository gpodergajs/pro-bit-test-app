from app import db

class BodyType(db.Model):
    __tablename__ = 'body_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)  # Sedan, SUV, Hatchback

    def __repr__(self):
        """Returns a string representation of the BodyType object."""
        return f"<BodyType(name={self.name})>"
