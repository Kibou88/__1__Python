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

api_logs = Logs(application_name="Tasks_API", log_dir=f"{current_dir}\Logs")

TASK_DIR = os.path.join(current_dir, ".todo")
TASK_FILEPATH = os.path.join(TASK_DIR, "task.json")