#!/usr/bin/env python
import json
import os
import glob

all_jsons_list = []
json_dir_name = '/path/to/json/dir'

json_pattern = os.path.join('Synthea/', '*.json')
file_list = glob.glob(json_pattern)
for file in file_list:
    print(file)

    with open(file, encoding="utf8") as f:
        data = json.load(f)
        all_jsons_list.append(data)

with open('all_json.json', 'w') as outfile:
    json.dump(all_jsons_list, outfile)


def search(patient_id):
    patient_id = 'urn:uuid:' + patient_id
    for json_file_dict in all_jsons_list:
        if json_file_dict['entry'][0].get('fullUrl') == patient_id:
            return json_file_dict


# urn:uuid:d667bfac-fdc8-4e16-baea-ca11513bf2da
test = search('d667bfac-fdc8-4e16-baea-ca11513bf2da')
print(test)
