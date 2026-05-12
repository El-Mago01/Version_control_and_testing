# log_csv.py

import csv
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_FILE = os.path.join(PROJECT_ROOT, "logs", "logs.csv")


def log(message):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode="a") as file:
        fieldnames = ["Time", "Message"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow(
            {"Time": time.asctime(time.localtime(time.time())), "Message": message}
        )
