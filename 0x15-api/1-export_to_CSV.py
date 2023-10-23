#!/usr/bin/python3
"""
Script to fetch data from API
"""


import csv
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

    file_name = f"{emp_id}.csv"

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todos_r_json:
            writer.writerow([emp_id, emp_username, task.get('completed'),
                            task.get('title')])
