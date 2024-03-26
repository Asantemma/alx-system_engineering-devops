#!/usr/bin/python3
"""A script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
from sys import argv


if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com'

    name_url = url1 + "/users/{}".format(argv[1])
    name_res = requests.get(name_url).json()
    todo_url = url1 + "/user/{}/todos".format(argv[1])
    todo_res = requests.get(todo_url).json()

    todo_num = len(todo_res)
    complete_todo = len([todo for todo in todo_res
                         if todo.get("completed")])
    name = name_res.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete_todo, todo_num))
    for todo in todo_res:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
