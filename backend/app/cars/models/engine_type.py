from app import db

class EngineType(db.Model):
    __tablename__ = 'engine_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)  # Petrol, Diesel, Electric, Hybrid

    def __repr__(self):
        return f"<EngineType(type={self.type})>"
