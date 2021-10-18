# you can create a dict using a set(a1) and a list(a2)
# zip creates a tuple
a1 = {1, 2, 3, 4, 5}
a2 = ["one", "two", "three", "four", "five"]
dict1 = {key: value for key, value in zip(a1, a2)}
print(dict1)
# example of turning key to value. switch up their position in the expression
new_dict = {value: key for key, value in dict1.items()}
print(new_dict)
# Doing Calculations
# REMEMBER: when using dict functions, it's always plural!
students = "A", "B", "C", "D", "E"
marks = 87, 85, 92, 95, 74
student_marks = {key: value for key, value in zip(students, marks)}
avg_student_marks = print("{:.2f}".format(
    (sum(values for values in student_marks.values())) / 3))
# variable student_marks is an iterable and in here, it was passed as an argument to the
# function sum()
print("{:.2f}".format(sum(student_marks.values()) / 3))
# Removing Specific Items
# interesting to note that after every build, the order in updated_inventory gets changed
# Does this mean that when I used a set operation, the dict turned to a set?
shoes = "Nike", "Adidas", "New Balance", "Puma", "Asics"
quantity = 25.00, 37.00, 28.00, 20.00, 18.00
shoes_inventory = {key: value for key, value in zip(shoes, quantity)}
print(shoes_inventory)
updated_inventory = {key: shoes_inventory[key]
                     for key in shoes_inventory.keys() - {"Asics"}}
print(updated_inventory)
# Sorting Dictionaries
# Instead of sorting based on value, it sorted alphabetically its keys
# Sorted() sorts alphabetically! This is an example of sorting by keys
sorted_shoes_inventory = {
    k: shoes_inventory[k] for k in sorted(shoes_inventory)}
print(sorted_shoes_inventory)
# sorting by value using generator expression
sorted_by_value = list(value for value in sorted(shoes_inventory.values()))
print(sorted_by_value)
# sorting by values without keys
for value in sorted(shoes_inventory.values()):
    print(value)
# sorting by values including keys
# sort by descencing order
# used items() instead of values()
# two arguments were passed to sorted()
# second argument is key which uses a function to get the values of the elements for comparison


def get_value(values):
    return values[1]


for k, v in sorted(shoes_inventory.items(), key=get_value):
    print(k, "->", v)
# Popping an item using .popitem()
color = ["red", "orange", "yellow", "green", "blue"]
value = 1, 2, 3, 4, 5
color_value = {key: value for key, value in zip(color, value)}
print(color_value)
while True:
    try:
        print(f"Dictionay has {len(color_value)} values")
        item = color_value.popitem()
        print(f"{item} has been removed")
    except KeyError:
        print("The dictionary has no more item")
        break
# Using python's built-in functions
# map()
# map() is defined using -> map(function, iterable)
# use a function to each item of the iterable
# map() is a generator expression as it yields result on demand
brand = ["Brooks", "Nike", "Asics", "Franco", "Hoka"]
price = 6500, 10000, 6000, 2500, 2100
shoe_rotation = {key: value for key, value in zip(brand, price)}
print(shoe_rotation)


def discount(item):
    return (item[0], round(item[1] * .70, 2))


discounted_price = dict(map(discount, shoe_rotation.items()))
print(discounted_price)
# filter()
# same format as map, filter(function, iterable)


def below_2000(key):
    return discounted_price[key] > 2000


updated_shoe_rotation = list(filter(below_2000, discounted_price.keys()))
print(updated_shoe_rotation)
# when you use functions key and values, a list of the keys or values are returned
