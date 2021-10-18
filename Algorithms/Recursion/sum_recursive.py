# Threading

def sum_recursive(current_number, accumulated_sum):
    if current_number == 11:
        return accumulated_sum
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


print(sum_recursive(1, 0))

# Global call
current_number = 1
accumulated_sum = 0


def recursive_sum():
    global current_number
    global accumulated_sum
    if current_number == 11:
        return accumulated_sum
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return recursive_sum()


print(recursive_sum())
my_list = [1, 2, 3]
# print(sum(my_list))


def list_sum_recursive(your_list):
    if your_list == []:
        return 0
    else:
        head = your_list[0]
        smaller_list = your_list[1:]
        return head + list_sum_recursive(smaller_list)


print(list_sum_recursive(my_list))

# Recursive Data Structures
"""Return a new list that is a result of a adding a new element to the list"""


def attach_head(element, input_list):
    return [element] + input_list


print(attach_head(-31, attach_head("hello", [])))
