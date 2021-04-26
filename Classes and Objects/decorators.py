from datetime import datetime


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper


# def say_whee():
#     print("whee!")


# # below is an example of a simple decoration
# # it wraps a function, modifying its behavior
# say_whee = my_decorator(say_whee)
# say_whee()
# print(say_whee)

print(datetime.now().hour)


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

# example of a decorator
# structure: @ + name of the function you'd like to wrap around with


@not_during_the_night
def say_whee():
    print("Whee!")


say_whee()


def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv

    return wrapper


@func
def func2(x, y):
    print(x)
    return y

# line 58 syntax replaces block of codes 63


@func
def func3():
    print("i am func3")


# func3 = func(func3)
x = func2(5, 6)
print(x)

# decorators can be used to validate a function
