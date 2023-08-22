#!/usr/bin/python3
"""This module contains the task 2"""


from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":

    new_json = {}
    root_url = f"https://jsonplaceholder.typicode.com"

    users = get(f"{root_url}/users").json()
    todos = get(f"{root_url}/todos").json()

    new_json = {u.get("id"): [{"username": u.get("username")} ] for u in users}

    with open("todo_all_employees.json", "w") as f:
        dump(new_json, f)
