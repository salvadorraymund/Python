from datetime import date
from datetime import time
from datetime import datetime

# today = date.today()
# print("Today's date is ", today)

# print("Date components: ", today.day, today.month, today.year)

# print("Today's weekday # is ", today.weekday())
# days = ["Monday", "Tuesday", "Wednesday",
#         "Thursday", "Friday", "Saturday", "Sunday"]
# print("which is a", days[today.weekday()])

today = datetime.now()
print(today)
t = datetime.time(datetime.now())
print("Time right now is", t)
