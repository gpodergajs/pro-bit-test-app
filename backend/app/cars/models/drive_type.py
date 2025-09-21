from app import db

class DriveType(db.Model):
    __tablename__ = 'drive_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)  # FWD, AWD, RWD

    def __repr__(self):
        """Returns a string representation of the DriveType object."""
        return f"<DriveType(name={self.name})>"
