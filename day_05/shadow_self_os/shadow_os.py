import pprint as p
import json

# scoring
def scoring(data):

    data["exercise"] = data["exercise"] / 60
    data["study"] = data["study"] / 60
    prod_score = 0
    prod_score += 60 if data["sleep"] >= 6 else 10 * data["sleep"]
    prod_score += 10 if data["coding"] >= 1 else 10 * data["coding"]
    prod_score += 20 if data["exercise"] >= 0.5 else 20 * data["exercise"]
    prod_score += 10 if data["study"] >= 0.6 else 10 * data["study"]
    
    return prod_score
    
# verdict
def verdict(data):
    verdict = ""
    verdict += "Need more sleep to recover." if data["sleep"] < 6 else ""
    verdict += "Still have to power to solve more." if data["coding"] < 1 else ""
    verdict += "Less than 30 mins of study is not enough to grow." if data["study"] < 0.6 else ""

    return verdict

def printer(data, name):
    print("🕶️ SHADOW REPORT - DAY 5")
    print(f"Name: {name}")
    print(f'Sleep: {data["sleep"]} hrs ❌') if data["sleep"] < 6 else print(f'Sleep: {data["sleep"]} hrs ✅')
    print(f'Code: {data["coding"]} hrs ❌') if data["coding"] < 1 else print(f'Code: {data["coding"]} hrs ✅')
    print(f'Exercise: {data["exercise"]*60} mins ❌') if data["exercise"] < 0.5 else print(f'Exercise: {data["exercise"]*60} mins ✅')
    print(f'Study: {data["study"]*60} mins ❌') if data["study"] < 0.6 else print(f'Study: {data["study"]*60} mins ✅')

    print("\nTasks:")
    for i, ( task_name, status ) in enumerate(data["tasks"].items()):
        emoji = "✅" if status == 'Y' else "❌"
        print(f"{i+1}. {task_name}: {emoji}")

    print("Score: ", data["score"])
    print("Verdict: ", data["final_verdict"])

def get_user_data():
    data = {}
    data["sleep"] = int(input("Sleep (hrs): "))
    data["coding"] = float(input("Coding (hrs): "))
    data["exercise"] = int(input("Exercise (min): "))
    data["study"] = int(input("Study (min): "))
    return data

def get_tasks():
    tasks = {}
    n = int(input("How many tasks today? "))
    for i in range(n):
        task = input(f"Task {i+1}: ")
        done = input("Completed? (Y/N): ").upper()
        tasks[task] = done
    return tasks

def save_to_json(data, path):
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


# Call your functions here to keep main clean
data = {}
name = input("Name: ")
data[name] = {}
data[name] = get_user_data()
data[name]["tasks"] = get_tasks()

name_data = data[name]
data[name]["score"] = scoring(name_data)
data[name]["final_verdict"] = verdict(name_data)
printer(name_data, name)

save_to_json(data, "shadow_self_os/logs/day_05.json")
print("Saved to: day_05.json")