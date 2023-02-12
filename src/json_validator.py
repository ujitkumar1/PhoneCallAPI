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
    try:
        jsonData = jsonData.get_data().decode("utf-8")
        req_obj = json.loads(jsonData)
    except Exception as error:
        log.error("Error while reading the data " + str(error.args[0]))
        err_msg = "invalid input : " + error.args[0]
        return err_msg

    try:
        validate(instance=req_obj, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        log.error("Error while validating the data \n ERROR :" + str(err.args[0]))
        err_msg = "invalid input : " + err.args[0]
        return err_msg

    return req_obj

# jsonData = json.loads('{"from_number": 1234567890, "to_number": 1234567809}')
# isValid = validateJson(jsonData)
# if isValid:
#     print(jsonData)
#     print("Given JSON data is Valid")
# else:
#     print(jsonData)
#     print("Given JSON data is InValid")
