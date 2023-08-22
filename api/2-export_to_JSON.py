#!/usr/bin/python3
"""This module contains the task 2"""


from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":

    root_url = f"https://jsonplaceholder.typicode.com"
    USERNAME = get(f"{root_url}/users/{argv[1]}").json().get("username")
    new_json = {}

    request = get(f"{root_url}/todos?userId={argv[1]}").json()
    new_json[argv[1]] = [{"task": result.get("title"),
                          "completed": result.get("completed"),
                          "username": USERNAME} for result in request]

    with open(argv[1] + ".json", "w") as f:
        dump(new_json, f)
