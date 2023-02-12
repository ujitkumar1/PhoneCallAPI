import json

from flask import request, Response
from flask_restful import Resource

from json_validator import validateJson
from log import log
from models.model import CallDetails
from src import db


class initiate_call(Resource):
    def post(self):
        """
            Endpoint for initiating a call report based on the form phone number and to phone number .

            This function initiating a call report based on the form phone number and to phone number and returns them
            in the form of a JSON response. It handles the following scenarios:
             - First it validated whether the request is in correct json format or not, if it's not is correct format,
                then it returns a 400 Bad Request response.
             - If the request is validated then it check whether the data type of resopnse is correct or not, if it's
               not correct then it returns a 400 Bad Request response.
             - If the request is validated successfully then it stores the information in the database.
             - After storing the request data in database, it makes a response with status code 200, with response
                message "Data saved from number: " + str(request_json["from_number"]) + " to number: " + str(
            request_json["to_number"])
            Args:

            Returns:
                flask.Response: Flask response object containing the initiating a call data or error message.
        """
        request_json = validateJson(request)

        # Checking whether the request_json is an instance of dict data type or not
        if not isinstance(request_json, dict):
            return Response(
                status=400,
                response=json.dumps(request_json),
                content_type="application/json"
            )

        # Adding the call details to the database
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
