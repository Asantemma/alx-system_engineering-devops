#!/usr/bin/python3
"""  A script that exports data in the CSV format."""

from csv import DictWriter, QUOTE_ALL
import requests
from sys import argv


if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com'

    name_url = url1 + "/users/{}".format(argv[1])
    name_res = requests.get(name_url).json()
    todo_url = url1 + "/user/{}/todos".format(argv[1])
    todo_res = requests.get(todo_url).json()

    todo_list = []
    for todo in todo_res:
        todo_dict = {}
        todo_dict.update({"user_ID": argv[1], "username": name_res.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)
