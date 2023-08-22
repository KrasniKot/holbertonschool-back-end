#!/usr/bin/python3
"""This module contains the task 0"""


import csv
from requests import get
from sys import argv

if __name__ == "__main__":

    root_url = f"https://jsonplaceholder.typicode.com"
    USERNAME = get(f"{root_url}/users/{argv[1]}").json().get("username")

    request = get(f"{root_url}/todos?userId={argv[1]}").json()

    with open(argv[1] + ".csv", "w") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in request:
            w.writerow([argv[1], USERNAME, i.get("completed"), i.get("title")])
