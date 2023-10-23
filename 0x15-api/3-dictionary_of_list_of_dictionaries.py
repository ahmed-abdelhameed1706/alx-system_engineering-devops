#!/usr/bin/python3
"""
Script to fetch data from API
"""

import json
import requests


if __name__ == "__main__":
    user_url = f"https://jsonplaceholder.typicode.com/users"

    user_req = requests.get(user_url)

    user_json = user_req.json()

    user_ids = []

    all_users_obj = {}

    file_name = "todo_all_employees.json"

    for user in user_json:
        user_ids.append(user.get('id'))

    for id in user_ids:
        id_r = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        tasks_req = requests.get(f"https://jsonplaceholder."
                                 f"typicode.com/users/{id}/todos")

        id_user_json = id_r.json()

        username = id_user_json.get('username')
        task_json = tasks_req.json()

        task_list = []

        for task in task_json:
            task_obj = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                    }
            task_list.append(task_obj)

        all_users_obj[f'{id}'] = task_list

    with open(file_name, 'w') as f:
        json.dump(all_users_obj, f)
