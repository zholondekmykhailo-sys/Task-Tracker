import json
import os


def load_json():
    if not os.path.exists('data_path'):
        os.makedirs('data_path', exist_ok=True)
        os.path.join('data_path', 'data.json')

    with open('data_path') as json_file:
        data = json.load(json_file)
    return data

local_data = load_json()

def save_json(data):
    with open('data_path', 'w') as json_file:
        json.dump(data, json_file, indent=4)

while True:
    event = input('Talk to me Goose  git')
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