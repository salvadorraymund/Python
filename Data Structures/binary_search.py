import math

my_list = [n for n in range(0, 100)]
t = 100
n = len(my_list)


def binary_search(a, n, t):
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] < t:
            l = m + 1
        elif a[m] > t:
            r = m - 1
        else:
            return m
    return None


answer = binary_search(my_list, n, t)
if answer is None:
    print("Element %d is not present in the array" % t)
else:
    print("Element %d is in index %s" % t, answer)
