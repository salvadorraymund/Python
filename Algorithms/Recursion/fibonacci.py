from functools import lru_cache


@lru_cache(maxsize=None)
def fibonnaci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=" ")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci_recursive(n - 1) + fibonnaci_recursive(n - 2)


print(fibonnaci_recursive(5))
