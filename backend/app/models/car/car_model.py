from app import db

class CarModel(db.Model):
    __tablename__ = 'car_models'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('car_brands.id'))

    brand = db.relationship("CarBrand", back_populates="models", lazy="joined")
    cars = db.relationship("Car", back_populates="model", lazy="joined")

    def __repr__(self):
        return f"<CarModel(name={self.name}, brand={self.brand.name})>"