def fixx_buxx(axd):
    if axd % 20 == 0:
        pass
    elif axd % 10 == 0:
        pass
    elif axd % 2 == 0:
        pass
    else:
        pass
# Figuring out the core conditionals and structure of the
# problem using pass makes it easier to decide how the
# implementation should work


def fizz_buzz(idx):
    if idx % 15 == 0:
        print("fizz-buzz")
    elif idx % 5 == 0:
        print("fizz")
    elif idx % 3 == 0:
        print("buzz")
    else:
        print(idx)


a = 30
fizz_buzz(a)

# callback


def get_square(val):
    """The callback"""
    return val ** 2


def caller(func, val):
    return func(val)


print(caller(get_square, 5))

for x in range(100):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)
