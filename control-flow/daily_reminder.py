# daily_reminder.py

# Prompt user for task
task = input("📝 Enter your task: ").strip()

# Prompt for priority
priority = ""
while True:
    priority = input("🔥 Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("❗ Please enter a valid priority (high/medium/low).")

# Prompt for time-bound
time_bound = ""
while True:
    time_bound = input("⏰ Is this task time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("❗ Please answer with yes or no.")

# Replace match-case with if-elif-else for priority
if priority == "high":
    priority_note = "⚠️ This is a high-priority task. Give it immediate attention!"
elif priority == "medium":
    priority_note = "🔔 This is a medium-priority task. Schedule it soon."
else:
    priority_note = "📝 This is a low-priority task. Complete it when possible."

# Check if task is time-bound
if time_bound == "yes":
    urgency = "⏳ Time-sensitive! Consider setting a deadline."
else:
    urgency = "⛱️ No immediate time pressure."
    
    print("\n📌 TASK REMINDER")
print(f"Task: {task}")
print(f"Priority: {priority.capitalize()}")
print(priority_note)
print(f"Time-bound: {'Yes' if time_bound == 'yes' else 'No'}")
print(urgency)
