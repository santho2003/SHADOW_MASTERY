import json
import os
from datetime import datetime

def save_log(data, name):
    os.makedirs("data/logs", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/logs/{today}_{name.lower()}.json"
    with open(filename, "w") as file:
        json.dump({name: data}, file, indent=4)
    print(f"\nSaved to: {filename}")
