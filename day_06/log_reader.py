import os
import json
import datetime

import json

def productivity_day(files, name):
    best_prod_score = float('-inf')  # lowest possible
    worst_prod_score = float('inf')  # highest possible

    for file in files:
        with open(f"logs/{file}", "r") as f:
            data = json.load(f)
            if name in data:
                score = data[name]["score"]
                if score > best_prod_score:
                    best_prod_score = score
                if score < worst_prod_score:
                    worst_prod_score = score

    print(f"\nBest Day score for {name}: {best_prod_score}")
    print(f"Worst Day score for {name}: {worst_prod_score}\n")


def display(name, files):
    for file in files:
        with open(f"logs/{file}", "r") as f:
            data = json.load(f)
            if name in data:
                print("\nFound matching file:")
                created_time = os.path.getctime(f"logs/{file}")
                readable_time = datetime.datetime.fromtimestamp(created_time)
                print(file,"\t", readable_time.date())
                print("Productivity Score: ", data[name]["score"])
                print("Verdict: ", data[name]["final_verdict"]) if data[name]["final_verdict"] != "" else print("No Verdict")
                print("Coding: ",data[name]["coding"])

def sort_by_productivity(name, files):
    scores = []
    for file in files:
        with open(f"logs/{file}", "r") as f:
            data = json.load(f)
            if name in data:
                scores.append({
                    "file": file,
                    "score": data[name]["score"]
                })

    sorted_scores = sorted(scores, key=lambda x:x["score"], reverse=True)
    print("\n------------Sorted Scores--------------")
    for score in sorted_scores:
        print(f"{score['file']}: {score['score']}")


name = input("Name: ")
log_dir = "logs/"
files = [f for f in os.listdir(log_dir) if f.endswith(".json")]
display(name, files)

productivity_day(files, name)
sort_by_productivity(name, files)
            

