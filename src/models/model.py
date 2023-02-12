from datetime import datetime

from src import db


class CallDetails(db.Model):
    __tablename__ = 'call_Details'
    id = db.Column(db.Integer, primary_key=True)
    from_number = db.Column(db.Integer, nullable=False)
    to_number = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
