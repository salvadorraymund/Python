from random import randint
from timeit import repeat


def run_sorting_algo(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time:{min(times)}")

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    # instead of using while len(result) < len(left) + len(right)
    while True:
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += (left[index_left:])
            break
        if index_left == len(left):
            # instead of using append, the remaining items in left/right were added to the list result
            result += (right[index_right:])
            # if break will be removed, index_left and index_right will continuously increase, thereby causing list index
            # to be out of range
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    left = array[:midpoint]
    right = array[midpoint:]
    # print(left)
    # print(right)
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


array = [8, 2, 4, 6, 5]
print(merge_sort(array))

array_length = 10000
if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(array_length)]
    run_sorting_algo(algorithm="merge_sort", array=array)