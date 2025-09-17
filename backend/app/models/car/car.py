from app import db

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(50), unique=True, nullable=False)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('car_models.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body_type_id = db.Column(db.Integer, db.ForeignKey('body_types.id'))
    engine_type_id = db.Column(db.Integer, db.ForeignKey('engine_types.id'))
    transmission_type_id = db.Column(db.Integer, db.ForeignKey('transmission_types.id'))
    drive_type_id = db.Column(db.Integer, db.ForeignKey('drive_types.id'))

    engine_capacity = db.Column(db.Float)       # e.g., 2.0
    fuel_consumption = db.Column(db.Float)      # e.g., 7.0 L/100km
    mileage = db.Column(db.Float)               # in km
    color = db.Column(db.String(30))
    doors = db.Column(db.Integer)
    registration_year = db.Column(db.Integer)

    model = db.relationship("CarModel", back_populates="cars", lazy="joined")
    owner = db.relationship("User", back_populates="cars", lazy="joined")
    body_type = db.relationship("BodyType", lazy="joined")
    engine_type = db.relationship("EngineType", lazy="joined")
    transmission_type = db.relationship("TransmissionType", lazy="joined")
    drive_type = db.relationship("DriveType", lazy="joined")

    def __repr__(self):
        return f"<Car(VIN={self.vin}, model={self.model.name}, owner={self.owner.username})>"