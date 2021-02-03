#!/usr/bin/env python
import json
import os
import glob

all_jsons_list = []
json_pattern = os.path.join('Synthea/', '*.json')
patient_json_list = glob.glob(json_pattern)
print("")
print("[INFO] Grabbing all Patient JSON files...")
for patient_json in patient_json_list:
    with open(patient_json, encoding="utf8") as patient_data:
        data = json.load(patient_data)
        all_jsons_list.append(data)

print("[INFO] Writing all Patient data into a singular JSON file...")
with open('all_json.json', 'w') as outfile:
    json.dump(all_jsons_list, outfile)
print("[INFO] Done. File containing all Patient data found at: Synthea/all_json.json")
