#!/usr/bin/python3
"""
exports employee info to csv
"""
if __name__ == "__main__":
    import csv
    import requests
    import json
    from sys import argv

    USER_ID = argv[1]
    request = requests.get(f"https://jsonplaceholder.typicode.com/users/{USER_ID}")
    USERNAME = request.json()["username"]
    all_tasks = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
            )
    with open(f"{USER_ID}.csv", "w", encoding="UTF-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for dict in all_tasks.json():
            data = [
                    str(USER_ID),
                    str(USERNAME),
                    str(dict.get("completed")),
                    str(dict.get("title")),
                    ]
            writer.writerow(data)

