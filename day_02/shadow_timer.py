import time
def countdown(minutes):
    print("Focus Task: ", input())
    with open("time_logs.txt", "w") as file:
        minutes = minutes-1
        while(minutes>0):
            print(f"Time left: {minutes}s")
            file.write(f"Time left: {minutes}s")
            minutes = minutes-1
            time.sleep(1)
        
        print("TIME'S UP WARRIOR.")

countdown(60)