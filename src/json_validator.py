import json
import os

import jsonschema
from jsonschema import validate

from log import log

script_dir = os.path.dirname(__file__)
rel_path = "json_schema.json"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    schema = json.load(f)


def validateJson(jsonData):
    """
        This function validates the input JSON data.
        The data is first decoded from bytes to a string and loaded into a Python object using the `json` module.
        The loaded data is then validated against a predefined JSON schema using the `jsonschema` library.
        Args:
            jsonData: The JSON data to be validated.
        Returns:
            If the data is valid, returns the loaded Python object. If the data is invalid, returns a string error message.
    """
    try:
        # loading the request
        jsonData = jsonData.get_data().decode("utf-8")
        req_obj = json.loads(jsonData)
    except Exception as error:
        log.error("Error while reading the data " + str(error.args[0]))
        err_msg = "invalid input : " + error.args[0]
        return err_msg

    try:
        # validating the request with json_schema
        validate(instance=req_obj, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        log.error("Error while validating the data \n ERROR :" + str(err.args[0]))
        err_msg = "invalid input : " + err.args[0]
        return err_msg

    return req_obj
