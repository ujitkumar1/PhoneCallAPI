from flask_restful import Resource
from sqlalchemy import or_
from model import CallDetails


class call_report(Resource):
    def get(self,phone):
        # User.query.filter_by(username=username).first()
        # detail = CallDetails.query.filter_by(from_number=phone)
        detail = CallDetails.query.filter(
            or_(CallDetails.from_number == phone,
                CallDetails.to_number == phone,
                )
        ).all()
        return {1:1}