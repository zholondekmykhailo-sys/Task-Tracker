import json

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

def task_id():
    infom = load_json()
    if not infom['tasks']:
        return 1
    return max(task["id"] for task in infom["tasks"]) + 1

def add_task():
    infom = load_json()
    infom['tasks'].append({
        'name': (input('Name ')),
        'description': (input('Description ')),
        'id': (task_id()),
        'status': (input('Status '))
    })
    save_json(infom)

def remove_task():
    infom = load_json()
    dead_task = input('which task? ')
    for task in infom['tasks']:
        if task['name'] == dead_task:
            infom['tasks'].remove(task)
    save_json(infom)

def update_task():
    infom = load_json()
    upd = input('which task? ')
    new_char = input('what exactly? ')
    for task in infom['tasks']:
        for i in task:
            if task[i] != new_char:
                return print('You should choose from this parameters: \n  name  description  id  status  ')
        for task in infom['tasks']:
            if task['name'] == upd:
                task[new_char] = input('new char? ')
        save_json(infom)

def show_all_tasks():
    infom = load_json()
    for task in infom['tasks']:
        print(task)