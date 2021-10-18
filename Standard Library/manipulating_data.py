from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    weight: float
    discount: float

    def discountPrice(self):
        return self.price - (self.price * self.discount)

    def __repr__(self):
        return repr((self.name, self.price, self.weight))


prodList = [
    Product("Doohickey", 40, 10, 0.15),
    Product("Widget", 50, 10, 0.05),
    Product("Doohickey", 40, 8, 0.15),
    Product("Thingamabob", 35, 12, 0.0),
    Product("Gadget", 65, 7, 0.20)
]

"""Sorting a list with sorted using a key"""


def prodsort(product):
    return product.price


print(sorted(prodList, key=prodsort))

"""Sorting a list with sorted function using lambda"""
# print(sorted(prodList, key=lambda p: p.price))

"""Sorting Stability"""
result = sorted(prodList, key=lambda p: p.weight)
# print(sorted(result, key=lambda p: p.price, reverse=True))

"""Using Operator Functions"""
from operator import attrgetter, methodcaller, itemgetter
print("Using attrgetter method:")
print(sorted(prodList, key=attrgetter("weight")))

print("Using methodcaller:")
print(sorted(prodList, key=methodcaller("discountPrice"), reverse=True))

inventory = [("Widget A", 5),
             ("Widget B", 7),
             ("Widget C", 4),
             ("Widget D", 3),
             ("Widget E", 4)
             ]
print(sorted(inventory, key=itemgetter(0)))
