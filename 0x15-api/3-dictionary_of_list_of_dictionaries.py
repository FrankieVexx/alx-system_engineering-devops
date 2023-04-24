#!/usr/bin/python3
"""fetching json data from an api"""

import json
import requests


if __name__ == "__main__":
    employee_url = "https://jsonplaceholder.typicode.com/users/"
    employee_dict = requests.get(employee_url).json()
    file_name = "todo_all_employees.json"
    new_dict = {}

    for elem in employee_dict:
        name = elem.get("username")
        employee_id = str(elem.get("id"))
        employee_data = requests.get("{}{}/todos".format(
                                     employee_url, employee_id))
        employee_data = employee_data.json()
        new_dict[employee_id] = []
        for item in employee_data:
            inner_dict = {}
            inner_dict["username"] = name
            inner_dict["task"] = item.get("title")
            inner_dict["completed"] = item.get("completed")
            new_dict[employee_id].append(inner_dict)

    with open(file_name, 'w') as f:
        json.dump(new_dict, f)
