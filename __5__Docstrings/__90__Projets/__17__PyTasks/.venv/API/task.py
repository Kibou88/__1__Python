# task.py
# --------------
# Purpose:
# Create the API for PyTask
# ---------------------------
# Creation date: 2025-07-23
# Modification date: 2025-07-23
# ------------------------------
# Version V1.0.0:

import os
from pathlib import Path
import json

from misc.logs import Logs

current_dir = os.path.dirname(os.path.dirname(__file__))

api_logs = Logs(application_name="Tasks_API", log_dir=f"{current_dir}\\Logs")

TASK_DIR = os.path.join(current_dir, ".todo")
TASK_FILEPATH = os.path.join(TASK_DIR, "task.json")

def get_tasks():
    if os.path.exists(TASK_FILEPATH):
        with open(TASK_FILEPATH, "r") as f:
            return json.load(f)
    return {}

def add_tasks(name):
    tasks = get_tasks()
    if name in tasks.keys():
       api_logs.log_error(f"{name} already added")
       return False

    tasks[name] = False
    _write_tasks_to_disk(tasks=tasks)
    return True

def remove_tasks(name):
    tasks = get_tasks()
    if name not in tasks:
        api_logs.log_error(f"{name} not found")
        return False

    del tasks[name]
    _write_tasks_to_disk(tasks=tasks)
    return True

def set_tasks_statut(name, done=True):
    tasks = get_tasks()
    if name not in tasks:
        api_logs.log_error(f"{name} not found")
        return False

    tasks[name] = done
    _write_tasks_to_disk(tasks=tasks)
    return True

def _write_tasks_to_disk(tasks):
    if not os.path.exists(TASK_DIR):
        os.makedirs(TASK_DIR)

    with open(TASK_FILEPATH, "w") as f:
        json.dump(tasks, f, indent=4)
        api_logs.log_info(f"{tasks} removed")


if __name__ == "__main__":
    task = "Apprendre Pthon"
    # add_tasks(task)
    # set_tasks_statut(task)
    remove_tasks(task)
    # print(test_tache)