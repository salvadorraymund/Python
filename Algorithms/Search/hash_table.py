items = ['mango', 'apple', 'banana', 'watermelon',
         'plum', 'orange', 'kiwi', 'pear', 'banana', 'mango']
print(items)
filter = dict()
for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)
