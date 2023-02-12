import json

from flask import request, Response
from flask_restful import Resource

from json_validator import validateJson
from log import log
from models.model import CallDetails
from src import db


class initiate_call(Resource):
    def post(self):
        request_json = validateJson(request)
        if not isinstance(request_json, dict):
            return Response(
                status=400,
                response=json.dumps(request_json),
                content_type="application/json"
            )
        detail = CallDetails(from_number=request_json["from_number"], to_number=request_json["to_number"])
        db.session.add(detail)
        db.session.commit()

        data = "Data saved from number: " + str(request_json["from_number"]) + " to number: " + str(
            request_json["to_number"])
        log.info(data)

        return Response(
            status=200,
            response=json.dumps(data),
            content_type="application/json"
        )
