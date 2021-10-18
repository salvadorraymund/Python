def binary_search(my_list, val):
    # if len(my_list) < 2:
    #     return my_list
    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]
    if val == mid:
        for i in range(len(my_list)):
            if my_list[i] == mid:
                return i
    else:
        for i in range(0, len(my_list)):
            if val < mid:
                return binary_search(left, val)
            elif val > mid:
                return binary_search(right, val)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 2))


def binary_search2(my_list, val):
    pass
#     mid = len(my_list) // 2
#     left = my_list[:mid]
#     right = my_list[mid:]
#     for i in range(0, len(my_list)):
#     	if my_list[mid] == val:
# 	        return mid
# 	    elif my_list[mid] < val:
# 	        return binary_search2(right, val)
# 	    elif my_list[mid] > val:
# 	        return binary_search2(left, val)
# 	    else:
# 	return None


# print(binary_search2(my_list, 5))
