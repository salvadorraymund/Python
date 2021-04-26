import time
import functools
# from export_decorators import do_twice


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         rv = func()
#         total = time.time() - start
#         print("Time:", total)
#         return rv

#     return wrapper


# @timer
# def test():
#     for _ in range(1000000):
#         pass


# @timer
# def test2():
#     time.sleep(2)


# test()
# test2()


# @do_twice
# def say_whee():
#     print("Wheee!")


# say_whee()


# @do_twice
# def greet(name):
#     print(f"Hello {name}")


# greet("Raymund")


# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"


# hi_raymund = return_greeting("Raymnund")
# print(hi_raymund)

# help(say_whee)

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for x in range(num_times):
        # this is called list comprehension
        sum([i**2 for i in range(10000)])


waste_some_time(1)

waste_some_time(100)

x = 0x0a
y = 0x01
z = x >> y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
