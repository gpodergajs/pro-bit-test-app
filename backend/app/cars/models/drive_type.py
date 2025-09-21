from app import db

class DriveType(db.Model):
    __tablename__ = 'drive_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)  # FWD, AWD, RWD

    def __repr__(self):
        return f"<DriveType(type={self.type})>"
