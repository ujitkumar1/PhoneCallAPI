import json

from flask import Response, request
from flask_restful import Resource
from sqlalchemy import or_

from log import log
from models.model import CallDetails


class call_report(Resource):
    def get(self):
        """
            Endpoint for retrieving call report based on phone number.

            This function retrieves call reports based on phone number and returns them
            in the form of a JSON response. It handles the following scenarios:
             - If the phone number is not in the correct format (10 digits), it returns a 400 Bad Request response with
               a message "Phone number is not in correct format".
             - If the phone number is in the correct format but not found in the database, it returns a 404 Not Found
               response with a message "number not found in database".
             - If the phone number is found in the database, it returns a 200 OK response with a JSON object containing
               the call report data and the next URL if there is more data available.
            Args:

            Returns:
                flask.Response: Flask response object containing the call report data or error message.
        """
        page = request.args.get("page", 1, type=int)
        per_page = 1
        phone = request.args.get('phone')

        # Checking the phone number is in the correct format or not
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

        # Checking if items is not none
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

            # Checking there is next page or not, if there is , then adding the url of next page
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
