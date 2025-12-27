import json
import os

local_data = [
    {

    }
]

def load_json():
    if not os.path.exists('data_path'):
        return local_data

    with open('data_path') as json_file:
        data = json.load(json_file)
    return data

def save_json(data):
    with open('data_path', 'w') as json_file:
        json.dump(data, json_file, indent=4)

while True:
    event = input('Talk to me Goose ')
    if event == 'stop':
        break

    if event == 'add':
        name = input('Name ')
        local_data[0][name] = {
            'description':input('lil description '),
            'time':input('when start '),
            'status':input('status ')
        }
        save_json(local_data)