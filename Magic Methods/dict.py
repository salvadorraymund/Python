NBA_team = {
    "Boston": "Celtics",
    "Chicago": "Bulls",
    "Toronto": "Raptors",
    "Memphis": "Grizzlies",
    "Los Angeles": "Lakers"
}

NCAA = dict([
    ("UNC", "Tar Heels"),
    ("Duke", "Blue Devils"),
    ("Baylor", "Bears"),
    ("Texas", "Longhorns"),
    ("Kentucky", "Wildcats"),
    ("Kansas", "Blejays")
])

# print(NCAA["UNC"])
# print(NBA_team["Boston"])
# NBA_team["New England"] = "Patriots"
# print(NBA_team)
# del NBA_team["New England"]
# print(NBA_team)

# integers can be used as key
# in the example below, it seems that values are accessed
# through indices
d = {0: "a", 1: "b", 2: "c", 3: "d"}
print(d)

# values contained need not to be of the same type
# in the example below, some are strings, numbers, or even
# another dictionary
person = {}
person["fname"] = "Joe"
person["lname"] = "Ingles"
person["age"] = 32
person["spouse"] = "Elena"
person["children"] = ["Raplh", "Betty", "Joey", "Alex"]
person["pets"] = {"dog": "Goofy", "cat": "Felix"}

# print(person["fname"])
# print(person["pets"])
# print(person["pets"]["dog"])

# print("age" in person)
print(NBA_team)
NBA_team.clear()
print(NBA_team)


def Digits(x):
    d = 1
    if (x >= 10):
        d = d + 1
    elif (x >= 100):
        d = d + 1
    elif (x >= 1000):
        d = d + 1
    elif (x >= 10000):
        d = d + 1
    return(d)


print(Digits(50))

print(497 % 16)

print(~13)
