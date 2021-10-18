def find_index(elements, value):
    """Searching elements by value"""
    left, right = 0, len(elements) - 1
    while left < right:
        middle = (left + right) // 2
        if elements[middle] == value:
            return middle
        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1


def identity(x): return x


def find_by_key(elements, value, key):
    """Searching elements by key"""
    left, right = 0, len(elements) - 1
    while left < right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])
        if middle_element == value:
            return middle
        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1


def contains(elements, value, key=identity):
    return find_by_key(elements, value, key) is not None


def find(elements, value, key):
    index = find_by_key(elements, value, key)
    return None if index is None else elements[index]


"""Functions to address searching for duplicate entries in an element"""
from dataclasses import dataclass
from operator import attrgetter


@dataclass(order=True)
class Person:
    first_name: str
    surname: str


first_name = ['Bob', 'John', 'Paul', 'Alice', 'John']
surname = ['Williams', 'Doe', 'Brown', 'Smith', 'Smith']


people = [Person(f, s) for f, s in zip(first_name, surname)]
by_surname = attrgetter('surname')
people.sort(key=by_surname)

find_people = find(people, value='Smith', key=by_surname)
print(find_people)
print(by_surname(people[2]))


def find_leftmost_index(elements, value, key):
    index = find_by_key(elements, value, key)
    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        index += 1
    return index


def find_rightmost_index(elements, value, key):
    index = find_by_key(elements, value, key)
    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index += 1
        index -= 1
    return index


def find_all_indices(elements, value, key):
    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)
    if left and right:
        return set(range(left + right + 1))
    return set()
