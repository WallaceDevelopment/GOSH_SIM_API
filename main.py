#!/usr/bin/env python
from flask import Flask, jsonify, make_response
import json

app = Flask(__name__)

# Load file with all synthetic Patient data
with open('all_json.json') as infile:
    all_patient_data = json.load(infile)


# 404 JSON
not_found_response = [
    {
        "Error": "Job Not Found"
    }
]


# # Return all patients
# @app.route('/api/v1/patient/all', methods=['GET'])
# def api_all():
#     """
#     :return: Return all available patient data in JSON
#     """
#
#     print(' [INFO] /api/v1/jobs/oldest API Query: {}'.format(all_patient_data))
#     return make_response(jsonify(all_patient_data), 200)  # jsonify automatically sets mimetype to application/json


# Return specific patient data
@app.route('/api/v1/patient/<patient_id>', methods=['GET'])
def api_patient(patient_id):
    """
    :param patient_id: Requested patient_id for data
    :return: Response from patient data search (JSON format)
    """

    response = None
    patient_id = 'urn:uuid:' + patient_id
    for patient_dict in all_patient_data:
        if patient_dict['entry'][0].get('fullUrl') == patient_id:
            response = patient_dict

    if not response:
        print(" [INFO] (404) /api/v1/patient/<patient_id> API Query: {}".format(patient_id))
        return make_response(jsonify(not_found_response), 404)

    print(" [INFO] /api/v1/patient/<patient_id> API Query: {}".format(response))
    return make_response(jsonify(response), 200)


app.run()
