from datetime import datetime, timedelta
import time

target_input = input("Enter your target time (YYYY-MM-DD HH:MM:SS): ")
target = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    diff = target - now
    
    if diff.total_seconds() <= 0:
        print("Countdown Finished!!")
        break

    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60

    print(f"{days}d {hours}h {minutes}m {seconds}s remaining", end='\n')
    time.sleep(1)

