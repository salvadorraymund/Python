# RECURSIVE
# def factorial(n):
#     print(f"factorial() with n = {n}")
#     return_value = 1 if n <= 1 else n * factorial(n - 1)
#     print(f"-> factorial({n}) returns {return_value}")
#     return return_value


# factorial(4)

# setup_string = """
# print("Recursive:")
# def factorial(n):
#     return 1 if n <= 1 else n * factorial(n - 1)
# """


# from timeit import timeit
# print(timeit("factorial(4)", setup=setup_string, number=100000))

# ITERATIVE
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value


print(factorial(4))
