from flask_restful import Resource

from src import db
from model import CallDetails


class initiate_call(Resource):
    def post(self,from_,to_):
        new_detail = CallDetails(from_number = from_,to_number = to_)
        db.session.add(new_detail)
        db.session.commit()
        return {"f":from_,"t":to_}

