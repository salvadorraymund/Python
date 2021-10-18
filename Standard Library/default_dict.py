# Grouping items - use list type as the default
# Pass a valid callable to default dict to handle missing keys
from collections import defaultdict

dd = defaultdict(list)
dd['key'].append(1)
print(dd)
dd['key'].append(2)
print(dd)
dd['key'].append(3)
print(dd)

# Grouping items using list
employees = [('Sales', 'John Doe'),
             ('Sales', 'Martin Smith'),
             ('Accounting', 'Jane Doe'),
             ('Marketing', 'Queen Elizabeth'),
             ('Marketing', 'Adam Eve')
             ]

department_sorter = defaultdict(list)
for department, employee in employees:
    department_sorter[department].append(employee)
print(department_sorter)

# Grouping items using set. This eliminates duplicate values

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(set)
for department, employee in dep:
    dep_dd[department].add(employee)
print(dep_dd)

"""Counting items. Use int as the argument. If you don't call the function int(), initialization starts at 0"""
dep_counter = defaultdict(int)
for department, employee_count in dep:
    dep_counter[department] += 1
print(dep_counter)

"""Accumulating values. Use float instead of int when dealing with currencies"""


def sales_total(accounting):
    """Calculate the total sales for each product sold"""
    dept_sales = defaultdict(float)
    for product, price in accounting:
        dept_sales[product] += price
    for product, total in dept_sales.items():
        print(f'Total income for product {product}: ${total:,.2f}')


incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00), ]

sales_total(incomes)

lst = [1, 1, 2, 1, 2, 2, 3, 4, 3, 3, 4, 4]
# lambda returns a default value of 1
# if you use int, answer will be incorrect as int has a default value of 0
def_d = defaultdict(lambda: 1)
for number in lst:
    def_d[number] *= number
print(def_d)
