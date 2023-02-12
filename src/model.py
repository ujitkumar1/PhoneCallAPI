from datetime import datetime

from src import db

class CallDetails(db.Model):
    __tablename__ = 'call_dDetails'
    id = db.Column(db.Integer, primary_key=True)
    from_number = db.Column(db.Integer,nullable=False)
    to_number = db.Column(db.Integer,nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
