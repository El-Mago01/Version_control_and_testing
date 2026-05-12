# log_json.py

import json
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_FILE = os.path.join(PROJECT_ROOT, "logs", "logs.json")


def log(message):
    log_entry = {"Time": time.asctime(time.localtime(time.time())), "Message": message}
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "r+") as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file)
    else:
        with open(LOG_FILE, "w") as file:
            json.dump([log_entry], file)
