import os

existing_logs = [f for f in os.listdir("Digital Journal Generator") if f.startswith("day_") and f.endswith(".txt")]
next_day = len(existing_logs)+1
filename = f"day_{next_day:02d}.txt"

name = input("Name: ")
daily_goal = input("Daily Goal: ")
time_spent = input("Time spent: ")
today_win = input("Today's win: ")
one_challenge = input("One Challenge: ")

with open(f"Digital Journal Generator/{filename}", "w") as file:
    file.write(f"SHADOW LOG - DAY {next_day}\n")
    file.write(f"Name: {name}\nDaily Goal: {daily_goal}\nTime Spent: {time_spent} hrs\nToday's Win: {today_win}\nOne Challenge: {one_challenge}\n")