#!/usr/bin/python3
""" This script uses REST API to retrieve the task completed
    by a given employee ID """

import requests
from sys import argv


def toDo():
    """ Function retrieves the todos list from api """
    emp_id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        employee_name = data["name"]
        done_tasks = sum(1 for item in data if item["completed"])
        total_tasks = len(data)

        print(f"Employee {employee_name} is done with"
              f" tasks({done_tasks}/{total_tasks}):")

        for item in data:
            print(f'\t {item["title"]}')

    else:
        print("Error: Unable to fetch data.")


if __name__ == "__main__":
    toDo()
