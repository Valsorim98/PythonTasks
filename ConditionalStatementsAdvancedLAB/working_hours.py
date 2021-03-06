import sys

HOUR = int(input("Please type an hour of the day "))
DAY = str(input("Please type a day of the week "))

work_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekend = ("Saturday", "Sunday")

def is_working_day(DAY):
    """If the input is a work day this function will return True.

    Args:
        DAY (str): Day of the week.

    Returns:
        bool: Returns True if its a working day, else False.
    """    

    return DAY in work_days

def is_weekend(DAY):
    """If the input is a day of the weekend this function will return True.

    Args:
        DAY (str): Day of the week.

    Returns:
        bool: Returns True if its a day of the weekend, else False.
    """    

    return DAY in weekend

if 10 <= HOUR <= 18:
    if is_working_day(DAY):
        print("It's open")

    elif is_weekend(DAY):
        print("It's closed")
else:
    print("closed")
