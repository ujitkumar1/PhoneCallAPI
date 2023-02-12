import json

from flask import Response, request
from flask_restful import Resource
from sqlalchemy import or_

from log import log
from models.model import CallDetails


class call_report(Resource):
    def get(self):
        phone = request.args.get('phone')
        if (len(phone) != 10) or (phone is None) or (not phone.isdigit()):
            msg = "Phone number is not in correct format"
            log.error(msg)
            return Response(
                status=400,
                response=json.dumps(msg),
                content_type="application/json"
            )
        phone = int(phone)
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
                    "to_number": details[one_deatil].to_number,
                    "start_time": str(details[one_deatil].start_time)
                }
                data.append(info)
            result["Success"] = True
            result["data"] = data

            return Response(
                status=200,
                response=json.dumps(result),
                content_type="application/json"
            )

        result["msg"] = "number not found in database"
        return Response(
            status=404,
            response=json.dumps(result),
            content_type="application/json"
        )
