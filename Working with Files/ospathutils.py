import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


print(os.name)

# Check for item existence and type
print("Item exists: " + str(path.exists("textfile.txt")))
print("Item is a file: " + str(path.isfile("textfile.txt")))
print("Item is a directory: " + str(path.isdir("textfile.txt")))

# Check path
print("Item path: " + str(path.realpath("textfile.txt")))
print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print("It has been " + str(td) + "since the file was modified")