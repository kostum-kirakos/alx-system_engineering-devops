#!/usr/bin/python3
"""
exports todos of all employees info to json
"""
if __name__ == "__main__":
    import json
    import requests

    request = requests.get(f"https://jsonplaceholder.typicode.com/users/")
    data = {}
    for user in request.json():
        userId = user["id"]
        username = user["username"]
        requestTasks = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={userId}"
        )
        data[userId] = [
            {
                "username": username,
                "task": dict.get("title"),
                "completed": dict.get("completed"),
            }
            for dict in requestTasks.json()
        ]
    with open("todo_all_employees.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(data))
