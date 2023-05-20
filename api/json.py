# ------------------------------- #
#            Rest API             #
#    with JSON file as database   #
# ------------------------------- #

import json
import os.path

from flask import jsonify, request

JSON_DATABASE_PATH = "./database/json/db.json"

# GET Method
def get_item():
    # GET Request Query Parameters
    args = request.args
    name = args.get("name", default="", type=str)

    # Check if file exists
    check_file()

    # Read JSON file
    with open(JSON_DATABASE_PATH, 'r') as file:
        data = json.load(file)
    
    return jsonify(data)


# POST Method 
def add_item():
    # GET Request Query Body
    body = request.get_json()

    # Read and Write JSON file
    check_file()
    data = {}

    # Read JSON file
    with open(JSON_DATABASE_PATH, 'r') as file:
        data = json.load(file)

    # TODO
    data["item"] = "content"

    # Write JSON file
    with open(JSON_DATABASE_PATH, 'w') as file:
        json.dump(data, file)
        
    return jsonify(data)


# PUT Method
def update_item():
    # GET Request Query Body
    body = request.get_json()

    # Read and Write JSON file
    check_file()
    data = {}

    # Read JSON file
    with open(JSON_DATABASE_PATH, 'r') as file:
        data = json.load(file)

    # TODO
    data["item"] = "content"

    # Write JSON file
    with open(JSON_DATABASE_PATH, 'w') as file:
        json.dump(data, file)
        
    return jsonify(data)


# DELETE Method
def delete_item():
    # GET Request Query Body
    body = request.get_json()

    # Read and Write JSON file
    check_file()
    data = {}

    # Read JSON file
    with open(JSON_DATABASE_PATH, 'r') as file:
        data = json.load(file)

    # TODO
    data["item"] = "content"

    # Write JSON file
    with open(JSON_DATABASE_PATH, 'w') as file:
        json.dump(data, file)
        
    return jsonify(data)


# Check if one file exists, else create it
def check_file(path=JSON_DATABASE_PATH):
    if not os.path.exists(path):
        folder = "/".join(path.split("/")[:-1])
        os.makedirs(folder, exist_ok=True)
        with open(path, 'w') as f:
            json.dump({}, f)
    return True