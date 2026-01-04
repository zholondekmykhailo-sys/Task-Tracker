from storage import *
from TaskClass import Task

while True:
    event = input('Choose an option: ')
    if event == 'stop':
        break
    if event == 'add':
        tasks = load_tasks()
        NewTask = Task(
            name = input('name '),
            description = input('description '),
            status = (input('status ')),
            id = task_id()
        )
        tasks.append(NewTask)
        print(tasks)
        save_tasks(tasks)

    if event == 'remove':
        name = input('remove what? ')
        tasks = load_tasks()
        tasks = [t for t in tasks if t.name != name]
        save_tasks(tasks)

    if event == 'upd':
        taskName = input('upd what task? ')
        charName = input('which char? ')
        if charName not in ('name', 'description', 'status'):
            print('invalid attribute ')
            continue
        upd = input('enter upd ')
        tasks = load_tasks()
        for task in tasks:
            if task.name == taskName:
                setattr(task, charName, upd)
        save_tasks(tasks)

    if event == 'show':
        show_all_tasks()