#!/usr/bin/python3
"""This module contains the task 0"""

from csv import writer, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":

    root_url = f"https://jsonplaceholder.typicode.com"
    NAME = get(f"{root_url}/users/{argv[1]}").json().get("name")

    request = get(f"{root_url}/todos?userId={argv[1]}").json()

    with open(argv[1] + ".csv", "w") as f:
        w = writer(f, quoting=QUOTE_ALL)
        for r in request:
            w.writerow([argv[1], NAME, r.get("completed"), r.get("title")])
