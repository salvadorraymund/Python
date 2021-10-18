n = 5
name = "Harry", "Barry", "Cherry", "Corry", "Jerry"
marks = 10, 20, 30, 15, 18
student_marks = {}
student_marks = dict((name[i], marks[i]) for i in range(n))
print(student_marks)
# items_student_marks = student_marks.items()
# print(items_student_marks)
# for items in items_student_marks:
#     print(items)
# use .items() to access and modify values. in order to access value from a dict,
# key has to called first by indexing[]
# for k, v in student_marks.items():
#     if v > 20:
#         student_marks[k] = round(v * .5, 2)
# print(student_marks)
# convert a dict to a list and use .keys function to modify a key. if you dont change it
# to a list, it'll encounter a RunTime error because the size has been changed
# during iteration
for key in (list(student_marks.keys())):
    if key == "Harry":
        del student_marks[key]
print(student_marks)
new_marks = {}
for key, value in student_marks.items():
    new_marks[value] = key
print(new_marks)
fruits_available = {}
fruits = "apple", "oranges", "grapes", "mango", "banana"
price = 30, 25, 100, 75, 20
fruits_available = (dict((fruits[i], price[i]) for i in range(len(fruits))))
print(fruits_available)
updated_fruits = {}
for key, value in fruits_available.items():
    if value >= 25:
        updated_fruits[key] = value
print(updated_fruits)
total_price = 0.00
for value in updated_fruits.values():
    total_price += value
print("$" + "{:.2f}".format(total_price))
NBA_teams = "Los Angeles", "New York", "Cleveland", "Denver", "Miami"
players = "Lebron", "Drose", "Klove", "Jokic", "Butler"
nba = {keys: values for keys, values in zip(NBA_teams, players)}
print(nba)
