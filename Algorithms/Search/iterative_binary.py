def contains(elements, value):
    """A function that will check if a value is present in an element"""
    """A nested function was created instead to avoid re-using copies of the elements during recursion"""
    """Reminder: before using binary search, make sure the elements are sorted"""
    def recursive(left, right):
        if left <= right:
            middle = (left + right) // 2
            if elements[middle] == value:
                return True
            if elements[middle] < value:
                return recursive(middle + 1, right)
            elif elements[middle] > value:
                return recursive(left, middle - 1)
        return False
    return recursive(0, len(elements) - 1)


my_list = ['apple', 'mango', 'banana', 'watermelon']
is_it_there = contains(sorted(my_list), 'banana')
print(is_it_there)
