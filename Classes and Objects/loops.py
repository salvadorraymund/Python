for x in range(5, 10):
    print(x)
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print(i, d)
for x in range(5, 10):
    # if (x == 7):
    #     break
    if(x % 2 == 0):
        continue
    print(x)


def say_hello(name):
    return f"Hello {name}"


name = "Raymund"
print(say_hello(name))


def be_awesome(name):
    return f"Yo {name}, together we are the strongest!"


print(be_awesome(name))


def greet_bob(say_hello):
    return say_hello("Bob")


print(greet_bob(say_hello))


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print('Printing from the second_child() function')

    second_child()
    first_child()


def Parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Hi, I am Liam"

    if num == 1:
        return first_child()
    else:
        return second_child


# parent()


first = Parent(1)
second = Parent(2)

print(first)
print(second())
