fruits = ["apples", "pears", "strawberry", 1, 2, 3]

for fruit in fruits:
    if fruit == "pears":
        print(fruit)
    else:
        print("not pears")

for x in range(len(fruits)):
    if fruits[x] == "pears":
        print(fruits[x])
    else:
        print("not a pear")
