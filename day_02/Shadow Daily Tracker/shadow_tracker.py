def scoring(sleep, exercise_min, study_min):
    init_sleep = 10
    init_exercise = 20
    init_study = 20

    exercise = exercise_min // 60
    study = study_min // 60

    prod_score = (sleep * init_sleep) + (exercise * init_exercise) + (study * init_study)

    with open("Shadow Daily Tracker/day_02.txt", "w", encoding="utf-8") as file:
        file.write(f"Shadow Tracker - Day 2\n")
        file.write(f"Sleep: {sleep} hrs\n")
        file.write(f"Exercise: {exercise_min} mins\n")
        file.write(f"Study: {study_min} mins\n")
        file.write(f"Productivity Score: {prod_score}%\n")

        if sleep < 6:
            file.write(f"Status: ⚠️ Sleep needs improvement\n")
        elif study_min < 60:
            file.write(f"Status: ⚠️ Study needs improvement\n")
        elif exercise_min < 5:
            file.write(f"Status: ⚠️ Need to struggle a bit\n")

sleep = int(input("How many hours have you slept? "))
exercise_min = int(input("How many minutes have you exercised? "))
study_min = int(input("How many minutes have you studied? "))

scoring(sleep, exercise_min, study_min)
