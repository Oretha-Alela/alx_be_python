import datetime
from datetime import timedelta

def main():
    today_date = display_current_datetime()
    print(f"Current date and time: {today_date}")
    days = int(input("Enter the number of days to add to the current date: "))
    print(f"Future date: {calculate_future_date(days)}")

def display_current_datetime():
    current_date = datetime.datetime.now().replace(microsecond=0)
    return current_date


def calculate_future_date(num_days):
    future_date = datetime.datetime.now() + timedelta(days = num_days)
    return future_date.strftime("%Y-%m-%d")
