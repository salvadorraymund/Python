# import random
# Encounters import errors when sourcing TypeVar from typing.py in lib

# from typing import Optional, Set, Sequence
# # from Search import T, S, Key, identity
# from typing import Callable, Typevar, Union

# T = Typevar("T")
# S = Typevar("S")


# def identity(element: T) -> Union[T, S]:
#     """Identity function serving as a default key provider"""
#     return element


# def find_index(
#         elements: Sequence[T], value: S, key: Key = identity
# ) -> Optional[int]:
#     """Return the index of value in elements or None."""
#     visited: Set[int] = set()
#     while len(visited) < len(elements):
#         random_index = random.randint(0, len(elements) - 1)
#         visited.add(random_index)
#         if key(elements[random_index]) == value:
#             return random_index
#     return None

import random


def find(elements, value):
    while True:
        random_element = random.choice(elements)
        if random_element == value:
            return random_element
