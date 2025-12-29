import json

info = {
            'tasks' : []
        }
k = 0

def load_json():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return info

def save_json(dataf):
    with open('dataf', 'w') as json_file:
        json.dump(dataf, json_file, indent=4)

def task_id(ka):
    return k + 1

def add_task():
    load_json()
    info['tasks'].append({
        'name': (input('Name ')),
        'description': (input('Description ')),
        'id': (k),
        'status': (input('Status '))
    })
    save_json(info)

def remove_task():
    dead_task = input('which task? ')
    for task in info['tasks']:
        if task['name'] == dead_task:
            info['tasks'].remove(task)
    save_json(info)

def update_task():
    load_json()
    upd = input('which task? ')
    new_char = input('what exactly? ')
    for task in info['tasks']:
        if task['name'] == upd:
            task[new_char] = input('new char? ')
    save_json(info)

def show_all_tasks():
    for task in info['tasks']:
        print(task)
while True:
    event = input('Choose an option: ')
    if event == 'stop':
        break
    if event == 'add':
        k = task_id(k)
        add_task()
    if event == 'remove':
        remove_task()
    if event == 'update':
        update_task()
    if event == 'show all tasks':
        show_all_tasks()