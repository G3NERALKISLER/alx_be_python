# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date, formatted

def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')

def main():
    current_date, formatted_now = display_current_datetime()
    print(f"Current date and time: {formatted_now}")

    try:
        days_input = input("Enter the number of days to add to the current date: ").strip()
        days = int(days_input)
        future = calculate_future_date(current_date, days)
        print(f"Future date: {future}")
    except (ValueError, OSError):
        print("Invalid input or input not supported in this environment.")

if __name__ == "__main__":
    main()
