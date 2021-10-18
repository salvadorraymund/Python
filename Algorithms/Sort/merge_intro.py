from random import randint
from timeit import repeat


def run_sorting_algo(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time:{min(times)}")


def merge(array):
        # base case of the recursion
    if len(array) > 2:
        mid = len(array) // 2
        leftarr = array[:mid]
        rightarr = array[mid:]

        merge(leftarr)
        merge(rightarr)

        i = 0
        j = 0
        k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                array[k] = leftarr[i]
                i += 1
            else:
                array[k] = rightarr[j]
                j += 1
            k += 1
        while i < len(leftarr):
            array[k] = leftarr[i]
            i += 1
            k += 1
        while j < len(rightarr):
            array[k] = rightarr[j]
            j += 1
            k += 1


items = [8, 2, 4, 6, 5]
print(items)
merge(items)
print(items)

array_length = 10000
if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(array_length)]
    run_sorting_algo(algorithm="merge", array=array)
