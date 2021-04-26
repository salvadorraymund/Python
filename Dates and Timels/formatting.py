from datetime import datetime

# %Y/%y - Year, %A/%a - weekday, %B/%b - month, %d - day of month
now = datetime.now()
print(now.strftime("The current year is: %Y"))

print(now.strftime("%d, %a %B, %y"))

# %c - local date and time, %x - local date, %X - local time
print(now.strftime("Local date and time: %c"))
print(now.strftime("Local date: %x"))
print(now.strftime("Local time: %X"))

# %I/%H - 12/24 hour, %M - minute, %S - second
# %p - locale's AM/PM
print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("Current time: %H:%M:%S"))
