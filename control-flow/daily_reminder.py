# daily_reminder.py

# Prompt user for task
task = input("Enter your task: ")

# Prompt user for priority with input validation
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority (high/medium/low).")

# Prompt user if task is time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    print("Please answer with yes or no.")
