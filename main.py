from flask import Flask, jsonify, request
import json
# import functions

app = Flask(__name__)

# API Methods

# ROOT METHODS
@app.route("/", methods=["GET"])
def root():
    try:
        return jsonify(json.load(open('src/API-Dump.json', 'r')))
    except FileNotFoundError:
        return jsonify({'error': 'API not found'}), 404

@app.route("/root", methods=["GET"])
def get_root():
    try:
        return jsonify(json.load(open('src/API-Dump.json', 'r')))
    except FileNotFoundError:
        return jsonify({'error': 'API not found'}), 404

# Classes Container
@app.route("/classes", methods=["GET"])
def get_classes():
    try:
        f = json.load(open('src/API-Dump.json', 'r'))
        return jsonify(f["Classes"])
    except FileNotFoundError:
        return jsonify({'error': 'Classes container not found'}), 404

# Instances
@app.route("/instance", methods=["GET"])
def get_instances():
    instance = request.args.get('target')

    data = json.load(open('src/API-Dump.json', 'r'))
    for index, class_data in enumerate(data["Classes"]):
        # print(class_name)
        if class_data["Name"].lower() == instance.lower():
            return jsonify(data["Classes"][index])
    return jsonify({'error': 'Instance not found'}), 404

# Properties
@app.route("/properties", methods=["GET"])
def get_properties():
    instance = request.args.get('target')
    properties = {}

    data = json.load(open('src/API-Dump.json', 'r'))
    for index, class_data in enumerate(data["Classes"]):
        # print(class_name)
        if class_data["Name"].lower() == instance.lower():
            if class_data["Members"]:
                for member in class_data["Members"]:
                    if member["MemberType"] == "Property":
                        p_temp = {
                            "Name": member["Name"],
                        "ValueType": member["ValueType"]["Name"],
                        "ReadOnly": (member["Security"]["Read"] == "None"),
                        "Tags": member["Tags"] if "Tags" in member else {},
                        }

                        if member["Capabilities"]:
                            p_temp["Capabilities"] = member["Capabilities"]["Read"] if "Read" in member["Capabilities"] else {}
                        if not properties.get(member["Name"]):
                            properties[member["Name"]] = p_temp

    if properties != {}: return jsonify(properties)
    return jsonify({'error': 'Instance not found'}), 404

if __name__ == '__main__':
    app.run()