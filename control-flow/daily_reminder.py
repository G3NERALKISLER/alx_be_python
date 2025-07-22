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

match priority:
    case "high":
        priority_note = "⚠️ This is a high-priority task. Give it immediate attention!"
    case "medium":
        priority_note = "🔔 This is a medium-priority task. Schedule it soon."
    case "low":
        priority_note = "📝 This is a low-priority task. Complete it when possible."

# 6. Check if task is time-bound and modify reminder
if time_bound == "yes":
    urgency = "⏳ Time-sensitive! Consider setting a deadline."
else:
    urgency = "⛱️ No immediate time pressure."

# 7. Final customized reminder output
print("\n📌 TASK REMINDER")
print(f"Task: {task}")
print(f"Priority: {priority.capitalize()}")
print(priority_note)
print(f"Time-bound: {'Yes' if time_bound == 'yes' else 'No'}")
print(urgency)