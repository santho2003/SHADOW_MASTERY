from utils.score import scoring, verdict
from utils.printer import printer
from utils.file_ops import save_log

def get_user_data():
    data = {}
    data["sleep"] = int(input("Sleep (hrs): "))
    data["coding"] = float(input("Coding (hrs): "))
    data["exercise"] = int(input("Exercise (min): "))
    data["study"] = int(input("Study (min): "))
    return data

def get_tasks():
    tasks = {}
    n = int(input("How many tasks? "))
    for i in range(n):
        task = input(f"Task {i+1}: ")
        tasks[task] = input("Completed? (Y/N): ").upper()
    return tasks

if __name__ == "__main__":
    name = input("Name: ")
    data = get_user_data()
    data["exercise"] /= 60
    data["study"] /= 60
    data["tasks"] = get_tasks()
    data["score"] = scoring(data)
    data["final_verdict"] = verdict(data)
    
    printer(data, name)
    save_log(data, name)
