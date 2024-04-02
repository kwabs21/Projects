
#This code calculates the number of days in a month when given the year and month, taking into account the leap years
def is_leap_year(Year):
    if Year % 4 == 0 :
        if Year % 100 == 0 :
            if Year % 400 == 0 :
                return True
            else: return False
        else: return True
    else: return False


def days_in_month(Year, month):
    if month > 12 or month < 1:
        return "Invalid month input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
    if is_leap_year(Year) and month == 2:
        return 29
    return month_days[month-1]
Year = int(input("Enter the year" ))
month = int(input("Enter month" ))

days = days_in_month(Year, month)
print(days)