# brute force approach
import sys

INT_MIN = -sys.maxsize - 1


def max_sum(arr, n, k):
    max_sum = INT_MIN

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
        max_sum = max(current_sum, max_sum)
    return max_sum


arr = [100, 200, 300, 400]
k = 2
n = len(arr)
print(max_sum(arr, n, k))

# Window sliding technique


def max_sum2(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid")
        return -1

    # compute sum of the first window
    window_sum = sum(arr[:k])

    # first sum available
    max_sum2 = window_sum

    # Compute the sum of the remaining windows by
    # removing first element of previous
    # window and adding last element of current window
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum2 = max(window_sum, max_sum2)
    return max_sum2


arr2 = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k2 = 4
print(max_sum2(arr2, k2))
