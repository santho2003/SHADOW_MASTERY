import sys
from utils.time_utils import start_timer, stop_timer, show_logs, resume_timer, generate_report

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        print("Usage: python timer.py [start <task>] | stop | log")
        sys.exit()
    
    command = args[1]

    if command == "start":
        task_name = " ".join(args[2:]) if len(args) > 2 else "Unnamed Task"
        start_timer(task_name)
    elif command == "stop":
        stop_timer()
    elif command == "log":
        show_logs()
    elif command == "resume":
        resume_timer()
    elif command == "report":
        generate_report()
    else:
        print("Invalid command")