from datetime import datetime

from src import db


class CallDetails(db.Model):
    """
        This is the Model of CallDetails table
        Attributes of the tables are:
        id -> id of the call
        from_number -> The phone number from which call is initiated
        to_number -> The phone number to which call is initiated
        start_time -> The start time of the phone call
    """
    __tablename__ = 'call_Details'
    id = db.Column(db.Integer, primary_key=True)
    from_number = db.Column(db.Integer, nullable=False)
    to_number = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
