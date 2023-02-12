from flask import make_response
from flask_restful import Resource
from sqlalchemy import or_

from models.model import CallDetails


class call_report(Resource):
    def get(self, phone):
        details = CallDetails.query.filter(
            or_(CallDetails.from_number == phone,
                CallDetails.to_number == phone,
                )
        ).all()

        result = {}

        if details:
            data = []

            for one_deatil in range(len(details)):
                info = {
                    "id": details[one_deatil].id,
                    "from_number": details[one_deatil].from_number,
                    "to_number": details[one_deatil].to_number
                }
                data.append(info)
            result["Success"] = True
            result["data"] = data

            return make_response(result, 200)

        else:
            result["Success"] = False
            return make_response(result, 403)
