from flask import request
from flask_restful import Resource

from models.model import CallDetails
from src import db


class initiate_call(Resource):
    def post(self):
        data = request.get_json()

        new_detail = CallDetails(from_number=data['from_number'], to_number=data['to_number'])
        db.session.add(new_detail)
        db.session.commit()

        return data
