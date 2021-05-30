import calendar

month, day, year = map(int, input().split())

answer_day = calendar.weekday(year, month, day)

day_list = list(calendar.day_name)

print(day_list[answer_day].upper())
