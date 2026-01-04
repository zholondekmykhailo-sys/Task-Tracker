# Task Tracker
## Simple CLI program to control your tasks. 
With Task Tracker, you coud easly add or remove your assingments from the list. You coud also update already existed task. 
Program saves data in JSON format.
##Installation
###Clone the Git repo
```bash
git clone https://github.com/zholondekmykhailo-sys/Task-Tracker
```
Make sure you have installed Python 3.10+
##Usage
start the main.py
```bash
main.py
```
###Available commands:
 - add (adding task with the name, description, status and id) 
 - remove (removing task by name)
 - upd (updates given part of task)
 - show (showing all the tasks)
###Example of usage
```bash
Choose an option: add
name: Buy groceries
description: Milk, eggs, bread
status: todo

Choose an option: show
{'name': 'go to gym', 'description': 'push, pull, legs', 'status': 'planned', 'id': 1}
