days = int(input('Input the number of days: '))
print('Days = ', days)
def convert_days_to_minutes(days):
    global hours, minutes
    hours = days * 24
    minutes = hours * 60
    return hours
    return minutes
convert_days_to_minutes(days)
print('Hours = ', hours)
print('Minutes = ', minutes)
