#!/usr/bin/python3
"""
exports employee info to csv
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    USER_ID = argv[1]
    request = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{USER_ID}")
    USERNAME = request.json()["username"]
    requestTasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={USER_ID}"
    )
    with open(f"{USER_ID}.json", "w", encoding="UTF-8") as file:
        data = {
                str(USER_ID): [
                    {
                        "task": dict.get("title"),
                        "completed": dict.get("completed"),
                        "username": USERNAME,
                    }
                    for dict in requestTasks.json()
                    ]
                }
        file.write(json.dumps(data))
