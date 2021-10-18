# Recursive

def count_leaf_items(item_list):
    """Recursively counts and returns the number of leaf items in (a potentially nested) list"""

    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)
        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1
    print(f"->Returning count {count}")
    return count


names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'],
         'Alex', ['Bea', 'Bill'], 'Ann']

# leaf_items = count_leaf_items(names)
# print(leaf_items)

# Iterative


def count_leaf(item_list):
    count = 0
    stack = []
    current_list = item_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1

        if isinstance(current_list[i], list):
            print(f"Encountered sublist \"{current_list[i]}\"")
            stack.append([current_list, i])
            print(stack)
            current_list = current_list[i]
            i = 0
        else:
            print(f"Leaf item -> \"{current_list[i]}\" -> " + str(i))

        count += 1
        i += 1


print(names)
iterative_method = count_leaf(names)
print(iterative_method)
