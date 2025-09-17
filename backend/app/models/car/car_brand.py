from app import db

class CarBrand(db.Model):
    __tablename__ = 'car_brands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    models = db.relationship("CarModel", back_populates="brand", lazy="joined")

    def __repr__(self):
        return f"<CarBrand(name={self.name})>"