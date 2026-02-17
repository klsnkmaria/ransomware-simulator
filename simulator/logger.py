import json
import os
import datetime
from config import SANDBOX_DIR, LOG_NAME

def log_event(event_name, payload):
    log_path = os.path.join(SANDBOX_DIR, LOG_NAME)
    entry = {
        "time": str(datetime.datetime.now()),
        "event": event_name,
        "payload": payload
    }
    
    logs = []
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            try:
                logs = json.load(f)
            except: logs = []
    
    logs.append(entry)
    with open(log_path, "w") as f:
        json.dump(logs, f, indent=4)
