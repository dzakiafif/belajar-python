from flask import jsonify, make_response

def success(data):
    response = {}
    response["status"] = "success"
    response["code"] = 200
    
    response["data"] = []
    
    if data:
        if "data" in data:
            response["data"] = data["data"]

    return make_response(jsonify(response)),200


def error(data):
    response = {}
    response["status"] = "error"
    response["code"] = 400
    response["message"] = data

    return make_response(jsonify(response)),200