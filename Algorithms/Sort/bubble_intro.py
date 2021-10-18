def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # create a flag that will terminate the function if there's nothing left to sort
        already_sorted = True
        # Start looking at each element of the array and its adjacent value.
        # begin at the first element (i) until you reach the last element. move through each element one by one
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # if the item you're looking at is greater than its adjacent value, swap their positions
                array[j], array[j + 1] = array[j + 1], array[j]
                # set the flag to false since you've already swapped two elements
                # and avoid the function to prematurely terminate
                already_sorted = False
        # if there are no swaps in the last iteration, array is already sorted
        if already_sorted:
            break
    return array


array = [8, 2, 4, 6, 5]
sorted_array = bubble_sort(array)
print(sorted_array)
