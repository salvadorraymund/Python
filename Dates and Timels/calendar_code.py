import calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2021, 3, 0, 0)
print(st)

for x in c.itermonthdays(2021, 3):
    print(x)

for month in calendar.month_name:
    print(month)

print("Team meetings will be held on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    # print(cal)
    weekone = cal[0]
    weektwo = cal[1]
    weekthree = cal[2]

    if weekone[calendar.MONDAY] == 0:
        meetday = weekthree[calendar.MONDAY]
    else:
        meetday = weektwo[calendar.MONDAY]

    print("%s %d" % (calendar.month_name[m], meetday))
