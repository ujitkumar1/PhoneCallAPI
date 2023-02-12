import json

from flask import Response, request
from flask_restful import Resource
from sqlalchemy import or_

from log import log
from models.model import CallDetails


class call_report(Resource):
    def get(self):
        page = request.args.get("page", 1, type=int)
        per_page = 1
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

        start = (page - 1) * per_page
        end = start + per_page
        items = details[start:end]

        result = {}

        if items:
            data = []

            for one_detail in range(len(items)):
                info = {
                    "id": items[one_detail].id,
                    "from_number": items[one_detail].from_number,
                    "to_number": items[one_detail].to_number,
                    "start_time": str(items[one_detail].start_time)
                }
                data.append(info)

            result["Success"] = True
            result["data"] = data

            next_start = end
            next_end = next_start + per_page
            next_page_data = details[next_start:next_end]

            if next_page_data:
                result["next_url"] = request.host_url + "call-report?phone=1234567812&page=" + str(page + 1)

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
