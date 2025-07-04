tasks = []
completed = []
for i in range(5):
    tasks.append(input(f"Enter task {i+1}: "))
    if input("Completed(Y/N): ").upper() == "Y":
        completed.append(tasks[i])
    
score = ((len(completed))/5)*100

with open("Shadow Task Tracker/task_report.txt", "w", encoding="utf-8") as file:
    file.write(f"🕶️ Task Report - Day 3\n")
    
    for task in tasks:
        if task in completed:
            file.write(f"Tasks: {task}✅\n")
        else:
            file.write(f"Tasks: {task}❌\n")

    file.write(f"Score: {score}%\n")
    if score < 60:
        file.write(f"Gotta work out more. You can do it. Try harder.")
    else:
        file.write(f"Almost there. You got this.")


    