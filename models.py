from meterapp.__init__ import db
from datetime import datetime


class Meters(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(100),nullable=False)

    def __repr__(self) -> str:
        return f'<Meter {self.label}>'


class Meter_Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    value = db.Column(db.Integer, nullable=False)
