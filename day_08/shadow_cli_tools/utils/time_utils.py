import os
import csv
from datetime import datetime, timedelta
from collections import defaultdict
from colorama import Fore, Style, init

init(autoreset=True)

session_file = "logs/current_session.txt"
log_file = "logs/time_log.csv"

def start_timer(task):
    os.makedirs("logs", exist_ok=True)
    start_time = datetime.now()
    with open(session_file, "w") as f:
        f.write(f"{task}|{start_time.isoformat()}")
    print(f"Started : {task} at {start_time.strftime('%I:%M %p')}")

def stop_timer():
    if not os.path.exists(session_file):
        print("No active sessions")
        return
    
    with open(session_file, "r") as f:
        task, start_time_str = f.read().split("|")
        start_time = datetime.fromisoformat(start_time_str)

    end_time = datetime.now()
    duration = end_time - start_time
    minutes = int(duration.total_seconds()//60)
    os.remove(session_file)

    os.makedirs("logs", exist_ok=True)
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().date(), task, minutes])

    print(f'Stopped: {task} at {end_time.strftime("%I:%M %p")}')
    print(f"Duration : {minutes//60}h {minutes % 60}m")
    print("Saved to time_log.csv")

def resume_timer():
    if not os.path.exists(session_file):
        print(f"{Fore.RED}No paused session to resume.")
        return
    
    with open(session_file, "r") as f:
        task, _ = f.read().split("|")
    
    new_start = datetime.now()
    with open(session_file, "w") as f:
        f.write(f"{task}|{new_start.isoformat()}")
    
    print(f"{Fore.BLUE}Resumed: {task} at {new_start.strftime("%I:%M %p")}")


def show_logs():
    if not os.path.exists(log_file):
        print(f"{Fore.RED}No logs found.")
        return
    
    print(f"{Style.BRIGHT}{Fore.MAGENTA}🕶️ SHADOW TIME LOG")
    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            date, task, mins = row
            print(f"{Fore.YELLOW}- {date} |{Fore.CYAN}{task} | {int(mins)//60}h {int(mins)%60}m")

def generate_report():
    if os.path.exists(session_file):
        print(f"{Fore.RED} No logs to generate report.")
        return
    
    weekly_totals = defaultdict(int)

    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            date_str, _, mins = row
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            week = dt.strftime("%Y-w%U")
            weekly_totals[week] += int(mins)

    print(f"{Fore.GREEN}📊 Weekly Productivity Report")
    for week in sorted(weekly_totals):
        hours = weekly_totals[week] // 60
        mins = weekly_totals[week] % 60
        print(f"{Fore.CYAN} - {week}: {hours}h {mins}m")