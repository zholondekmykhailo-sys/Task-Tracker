import json
from TaskClass import Task

info = {
            'tasks' : []
        }

def load_json():
    try:
        with open('dataf', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError) :
        return info

def save_json(dataf):
    with open('dataf', 'w') as json_file:
        json.dump(dataf, json_file, indent=4)

def load_tasks():
    data = load_json()
    return [Task.from_dict(t) for t in data['tasks']]

def save_tasks(tasks):
    data =  {'tasks': [t.to_dict() for t in tasks]}
    save_json(data)

def task_id():
    infom = load_json()
    if not infom['tasks']:
        return 1
    return max(task["id"] for task in infom["tasks"]) + 1

def show_all_tasks():
    infom = load_json()
    for task in infom['tasks']:
        print(task)