import calendar
from datetime import datetime

def display_month_calendar():
    try:
        year = datetime.now().year
        
        month = int(input("Enter the month (1-12): "))

        if not (1 <= month <= 12):
            print("Invalid month entered. Please enter a number between 1 and 12.")
            return

        print(f"\n--- Calendar for {calendar.month_name[month]} {year} ---")
        print(calendar.month(year, month))

    except ValueError:
        print("Invalid input. Please enter a numeric value for the month.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

display_month_calendar()
