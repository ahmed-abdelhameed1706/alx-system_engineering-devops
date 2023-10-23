#!/usr/bin/python3
"""
Script to fetch data from API
"""

import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]

    name_req_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_req_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    name_r = requests.get(name_req_url)
    todos_r = requests.get(todo_req_url)

    name_r_json = name_r.json()
    todos_r_json = todos_r.json()

    emp_name = name_r_json.get('name')
    emp_username = name_r_json.get('username')

    file_name = f"{emp_id}.json"

    task_list = []

    for task in todos_r_json:
        task_obj = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': emp_username
                }
        task_list.append(task_obj)

    obj = {
            f"{emp_id}": task_list
            }

    with open(file_name, 'w') as f:
        json.dump(obj, f)
