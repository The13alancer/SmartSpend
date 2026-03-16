import json
import os


def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename):
        return {"pending": [], "completed": []}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {"pending": [], "completed": []}

        pending = data.get("pending", [])
        completed = data.get("completed", [])

        if not isinstance(pending, list) or not isinstance(completed, list):
            return {"pending": [], "completed": []}

        return {"pending": pending, "completed": completed}

    except (json.JSONDecodeError, OSError):
        return {"pending": [], "completed": []}


def save_tasks(data, filename="tasks.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        return False
