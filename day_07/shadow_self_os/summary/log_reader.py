import json
import os

def read_all_logs():
    logs_dir = "data/logs"
    files = [f for f in os.listdir(logs_dir) if f.endswith(".json")]
    
    for f in sorted(files):
        with open(os.path.join(logs_dir, f)) as file:
            data = json.load(file)
            for name, entry in data.items():
                print(f"{f} | {name} | Score: {entry['score']} | Verdict: {entry['final_verdict']}")

if __name__ == "__main__":
    read_all_logs()
