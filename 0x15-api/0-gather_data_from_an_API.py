#!/usr/bin/python3
"""fetch json data from an api with alist of dicts"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    employee_url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    employee_dict = requests.get(employee_url).json()
    employee_name = employee_dict.get("name")
    employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    employee_todo = employee_todo.json()
    total_todo = 0
    completed_titles = []
    number_completed = 0

    for item in employee_todo:
        if item.get("userId") == int(employee_id):
            total_todo += 1
            if item.get("completed") is True:
                number_completed += 1
                completed_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_completed, total_todo))
    for title in completed_titles:
        print("\t {}".format(title))
