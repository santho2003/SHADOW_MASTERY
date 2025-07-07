def printer(data, name):
    print("🕶️ SHADOW REPORT - DAY 5")
    print(f"Name: {name}")
    print(f'Sleep: {data["sleep"]} hrs ❌') if data["sleep"] < 6 else print(f'Sleep: {data["sleep"]} hrs ✅')
    print(f'Code: {data["coding"]} hrs ❌') if data["coding"] < 1 else print(f'Code: {data["coding"]} hrs ✅')
    print(f'Exercise: {round(data["exercise"]*60, 2)} hrs ❌') if data["exercise"] < 0.5 else print(f'Exercise: {data["exercise"]*60} mins ✅')
    print(f'Study: {round(data["study"]*60,2)} hrs ❌') if data["study"] < 0.6 else print(f'Study: {data["study"]*60} mins ✅')

    print("\nTasks:")
    for i, ( task_name, status ) in enumerate(data["tasks"].items()):
        emoji = "✅" if status == 'Y' else "❌"
        print(f"{i+1}. {task_name}: {emoji}")

    print("Score: ", data["score"])
    print("Verdict: ", data["final_verdict"])
