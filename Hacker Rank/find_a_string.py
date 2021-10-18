def count_substring(string, sub_string):
    return (sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i + len(sub_string)] == sub_string]))


def count_substring2(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count
