#!/usr/bin/python3
"""Export data in json format """

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    employee_id = argv[1]
    file_name = employee_id + '.json'
    total_todos = 0
    completed_todos = 0
    completed_titles = []

    res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                       employee_id)
    employee_username = res.json().get('username')

    res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                       employee_id + '/todos')
    employee_todos = res.json()

    records = {str(employee_id): []}

    for item in employee_todos:
        total_todos += 1
        records[str(employee_id)].append({"task": item.get('title'),
                                         "completed": item.get("completed"),
                                          "username": employee_username})

    with open(file_name, 'w') as jsonfile:
        json.dump(records, jsonfile)
