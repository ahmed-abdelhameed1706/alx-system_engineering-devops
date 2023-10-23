#!/usr/bin/python3
"""
Script to fetch data from API
"""


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

    todos_len = len(todos_r_json)

    completed_tasks = 0
    completed_tasks_titles = []

    for task in todos_r_json:
        if task.get('completed') is True:
            completed_tasks += 1
            completed_tasks_titles.append(task.get('title'))

    msg = (f"Employee {emp_name} is done with "
           f"tasks({completed_tasks}/{todos_len}):")
    print(msg)

    for title in completed_tasks_titles:
        print(f"\t {title}")
