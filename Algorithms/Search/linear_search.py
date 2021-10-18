def linear_search(my_list, element):
    if type(element) != int:
        raise Exception("Error: Your input is not an integer!")
    for i in range(0, len(my_list)):
        if my_list[i] == element:
            return i
    return False


lys = [1, 2, 3, 4, 5, 6, 7]
# print(linear_search(lys, 1))

# Using enumerate function


def line_search(iterable, element):
    for index, value in enumerate(iterable):
        if value == element:
            return index


print(line_search(lys, 4))
print(lys.index(4))
