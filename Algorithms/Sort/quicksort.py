from random import randint
import statistics


def quicksort(array):
        # base case
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # start at 0, stop at the end, move 1 step
    pivot = array[randint(0, (len(array)) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # recursion
    return quicksort(low) + same + quicksort(high)


array = [8, 2, 4, 6, 5]
print(quicksort(array))
