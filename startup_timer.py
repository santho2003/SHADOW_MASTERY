from datetime import datetime
def path_to_goal(current_age, target_year):
    current_year = datetime.now().year
    if(target_year-current_year) > 10:
        print("Train harder")
    elif (target_year - current_year) < 5:
        print("Deploy mode: GO")
    else:
        print("Perfect timing")

path_to_goal(21, 2030)
    