from storage import *

while True:
    event = input('Choose an option: ')
    if event == 'stop':
        break
    if event == 'add':
        add_task()
    if event == 'remove':
        remove_task()
    if event == 'upd':
        update_task()
    if event == 'show':
        show_all_tasks()