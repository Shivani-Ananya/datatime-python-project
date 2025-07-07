from datetime import datetime
import time
from plyer import notification

reminder_input = input("Enter your reminder time (HH:MM): ")
message = input("What should I remind you about? ")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == reminder_input:
        
        notification.notify(
            title = "Time's up!!",
            message = message,
            timeout = 10
            )
        print(f"Reminder: {message}")
        break
