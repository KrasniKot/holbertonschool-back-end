#!/usr/bin/python3
"""This module contains the task 2"""


from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":

    new_json = {}
    root_url = f"https://jsonplaceholder.typicode.com"

    users = get(f"{root_url}/users").json()

    for user in users:
        USER_ID = user.get("id")

        todos = get(f"{root_url}/todos?userId={USER_ID}").json()

        usr_dicts = [{
            "username": user.get("username"),
            "task": todo.get("title"),
            "completed": todo.get("completed")} for todo in todos]

        new_json[USER_ID] = usr_dicts

    with open("todo_all_employees.json", "w") as f:
        dump(new_json, f)
