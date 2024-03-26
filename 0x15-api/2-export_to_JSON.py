#!/usr/bin/python3
""" A script that exports data in the JSON format."""

import requests
from sys import argv
from json import dump


if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com'

    name_url = url1 + "/users/{}".format(argv[1])
    name_res = requests.get(name_url).json()
    todo_url = url1 + "/user/{}/todos".format(argv[1])
    todo_res = requests.get(todo_url).json()

    todo_list = []
    for todo in todo_res:
        todo_dict = {}
        todo_dict.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": name_res.get("username")})
        todo_list.append(todo_dict)

    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: todo_list}, f)
