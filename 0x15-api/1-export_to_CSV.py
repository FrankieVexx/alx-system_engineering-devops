#!/usr/bin/python3
"""Converting extracted data into a csv format"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    employee_url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    employee_dict = requests.get(employee_url).json()
    employee_name = employee_dict.get("username")
    employee_todo = requests.get("{}/todos".format(employee_url))
    employee_todo = employee_todo.json()
    file_name = employee_id + ".csv"

    with open(file_name, 'w') as csvfile:
        for item in employee_todo:
            csvfile.write('"{}","{}","{}","{}"\n'.format(item.get(
                "userId"), employee_name, item.get("completed"),
                item.get("title")))
