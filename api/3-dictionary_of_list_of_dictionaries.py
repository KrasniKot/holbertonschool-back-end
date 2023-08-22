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

	new_json = [user.get("id"): {"idk": user.get("name")} for user in users]

	with open(argv[1] + ".json", "w") as f:
        	dump(new_json, f)
