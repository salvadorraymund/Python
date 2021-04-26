from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# timedelta = time based mathematics

print(timedelta(days=354, hours=5, minutes=1))

now = datetime.now()
print("Today is " + str(now))
print("One year from now it will be " + str(now + timedelta(days=365)))
print("In two days and three weeks it will be "
      + str(now + timedelta(days=2, weeks=3)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was " + s)

today = date.today()
nyd = date(today.year, 1, 1)

if nyd < today:
    print("New Year's Day already went by %d days ago" % ((today - nyd).days))
    # % is  a string method, .days is a property of the timedelta object
    nyd = nyd.replace(year=today.year + 1)

# time_to_nyd = nyd - today
print("It's just %d days until the new year" % ((nyd - today).days))

bday = date(today.year, 10, 31)
diff = (bday - today).days  # turns a date format to days
print(diff)
if diff > 0:
    print("Birthday in %d days" % diff)
else:
    print("Birthday in %d days" % diff + 365)

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print("Tomorrow will be " + days[(today.weekday() + 1) % 7])

print(datetime.date(datetime.now()))
