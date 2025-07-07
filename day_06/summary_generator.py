import os
import json

def extract_details(name, files):
    extracted = {}
    for file in files:
        with open(f"logs/{file}", "r") as f:
            data = json.load(f)
            if name in data:
                extracted[file] = {}
                extracted[file]["sleep"] = data[name]["sleep"]
                extracted[file]["coding"] = data[name]["coding"]
                extracted[file]["study"] = data[name]["study"]
                extracted[file]["score"] = data[name]["score"]
    
    return extracted

def calculate_data(data, name, files):
    calculated_data = {}
    no_of_days = len(data.keys())
    total_coding_time = sum(entry["coding"] for entry in data.values())
    total_study_time = sum(entry["study"] for entry in data.values())
    total_score_time = sum(entry["score"] for entry in data.values())

    calculated_data["days"] = no_of_days
    calculated_data["avg_coding"] = round(total_coding_time / no_of_days, 2)
    calculated_data["avg_study"] = round(total_study_time / no_of_days, 2)
    calculated_data["avg_score"] = round(total_score_time / no_of_days, 2)
    calculated_data["sleep_frequency"] = len([entry["sleep"] for entry in data.values() if entry["sleep"] < 6])
    
    prod_score = 0
    for file in files:
        with open(f"logs/{file}", "r") as f:
            data = json.load(f)
            if name in data:
                if data[name]["score"] > prod_score:
                    prod_score = data[name]["score"]
                    prod_file = file
    
    best_day = prod_file
    calculated_data["best_day"] = best_day

    return calculated_data    

def display_summary(data, name):

    print(f'🧠 PRODUCTIVITY SUMMARY ({name}, {data["days"]})')
    print(f'Average Code: {data["avg_coding"]} hrs')
    print(f'Average Score: {data["avg_score"]}%')
    print(f'Days w/ <6 hrs sleep: {data["sleep_frequency"]}')
    print(f'Best Day: {data["best_day"]}')



name = input("Name: ")
file_path = "logs/"
files = [f for f in os.listdir(file_path) if f.endswith(".json")]

data = extract_details(name, files)

calculated_data = calculate_data(data, name, files)
display_summary(calculated_data, name)