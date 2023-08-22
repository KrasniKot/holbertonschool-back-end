#!/usr/bin/python3
"""This module contains the task 0"""

from csv import writer, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":

    root_url = f"https://jsonplaceholder.typicode.com"
    EMPLOYEE_NAME = get(f"{root_url}/users/{argv[1]}").json().get("name")

    request = get(f"{root_url}/todos?userId={argv[1]}").json()

    with open(f"{argv[1]}.csv", "w") as f:
        writing = writer(f, quoting=QUOTE_ALL)
        for result in request:
            writing.writerow([
                    argv[1],
                    EMPLOYEE_NAME,
                    result["completed"],
                    result["title"]
                    ])
