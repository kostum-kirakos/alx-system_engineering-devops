#!/usr/bin/python3
"""
Retrieves employee info using a REST API
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id = argv[1]
    request = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    EMPLOYEE_NAME = request.json()["name"]
    requestTasks = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    TOTAL_NUMBER_OF_TASKS = len(requestTasks.json())
    TASK_TITLE = ""
    NUMBER_OF_DONE_TASKS = 0
    for dict in requestTasks.json():
        for key, val in dict.items():
            if key == "completed" and val is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE += "\n"
                TASK_TITLE += "\t"
                TASK_TITLE += f"{dict['title']}"
    print(
            "Employee {} is done with tasks({}/{}):".format(
                EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
                ), end="")
    print(TASK_TITLE)



