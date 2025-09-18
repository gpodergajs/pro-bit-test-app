from app import db

class TransmissionType(db.Model):
    __tablename__ = 'transmission_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)  # Automatic, Manual, CVT

    def __repr__(self):
        return f"<TransmissionType(type={self.type})>"