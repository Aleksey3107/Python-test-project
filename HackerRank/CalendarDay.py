import calendar

date = list(input().split())
day = calendar.weekday(year=int(date[-1]), day=int(date[-2]), month=int(date[0]))
print((calendar.day_name[day]).upper())
