import json
import os

def generate_summary():
    logs_dir = "data/logs"
    total_logs = 0
    total_score = 0
    total_code = 0
    low_sleep_days = 0

    for f in os.listdir(logs_dir):
        if not f.endswith(".json"):
            continue
        with open(os.path.join(logs_dir, f)) as file:
            data = json.load(file)
            for _, entry in data.items():
                total_logs += 1
                total_score += entry["score"]
                total_code += entry["coding"]
                if entry["sleep"] < 6:
                    low_sleep_days += 1

    print(f"\n🧠 PRODUCTIVITY SUMMARY")
    print(f"Total Days Logged: {total_logs}")
    print(f"Average Score: {total_score // total_logs}%")
    print(f"Average Coding Time: {round(total_code / total_logs, 2)} hrs")
    print(f"Days with <6 hrs Sleep: {low_sleep_days}")

if __name__ == "__main__":
    generate_summary()
