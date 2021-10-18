from emulate_default_dict import my_default_dict
dd_one = my_default_dict(list)
dd_one['missing']
dd_one.default_factory = str
dd_one['heart']
print(dd_one)
# dd_two = my_default_dict(None)
# dd_two['missing']

my_dict = my_default_dict(list, first=1)
print(my_dict)
my_dict['second'] = 2
print(my_dict)
# even setdefault cannot overrid setitem
my_dict.setdefault('third', 3)
print(my_dict)

# lst = [1, 1, 2, 1, 2, 2, 3, 4, 3, 3, 4, 4]
# def_d = my_default_dict(lambda: 1)
# for number in lst:
#     def_d[number] *= 1
