#!/usr/bin/python3
"""This module contains the task 0"""

from requests import get
from sys import argv

if __name__ == "__main__":

    root_url = f"https://jsonplaceholder.typicode.com"
    EMPLOYEE_NAME = get(f"{root_url}/users/{argv[1]}").json().get("name")

    request = get(f"{root_url}/todos?userId={argv[1]}").json()
    TOTAL_NUMBER_OF_TASKS = len(request)

    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0

    for result in request:
        if result.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(result.get("title"))

    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print(f"\t {title}")
