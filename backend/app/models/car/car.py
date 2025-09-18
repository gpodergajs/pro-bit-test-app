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

    engine_capacity = db.Column(db.Float)
    fuel_consumption = db.Column(db.Float)
    mileage = db.Column(db.Float)
    color = db.Column(db.String(30))
    doors = db.Column(db.Integer)
    registration_year = db.Column(db.Integer)
    price = db.Column(db.Float)

    # Relationships (use string names to avoid circular imports)
    model = db.relationship("CarModel", back_populates="cars", lazy="joined")
    owner = db.relationship("User", back_populates="cars", lazy="joined")
    body_type = db.relationship("BodyType", lazy="joined")
    engine_type = db.relationship("EngineType", lazy="joined")
    transmission_type = db.relationship("TransmissionType", lazy="joined")
    drive_type = db.relationship("DriveType", lazy="joined")

    def __repr__(self):
        model_name = self.model.name if self.model else "Unknown"
        owner_name = self.owner.username if self.owner else "Unknown"
        return f"<Car(VIN={self.vin}, model={model_name}, owner={owner_name})>"
