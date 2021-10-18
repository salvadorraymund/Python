string = "The quick brown fox jumped over the lazy dog"
new_string = string.split()
# print(new_string)

"""Justification"""
# ljust, center, rjust
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)
# for name in names:
#     print(name.ljust(biggest + 2, "-") + ":")
# for name in names:
#     print(name.center(biggest + 2, "-") + ":")
# for name in names:
#     print(name.rjust(biggest + 2, "-") + ":")


"""Use a translation table to replace characters"""
trans_table = str.maketrans("abegilostz", "4636110572")
print(string.translate(trans_table))


"""Basic string operations"""
import string

test_string1 = "The quick brown fox jumped over the lazy dog on the 1st of December."
test_string2 = "Supercalifragilistic"
test_string3 = "90210"

result = "".join([c for c in test_string1 if c in string.ascii_letters])
print(result)

print(any([c.isalpha() for c in test_string1]))
print(biggest)

"""String Formatting"""
from string import Template

the_str = "The quick brown $animal $action jumped over the lazy dog."
the_template = Template(the_str)
output_str = the_template.substitute(animal="fox", action="jumped")
print(output_str)
args = {
    "animal": "cow",
    "action": "walked"
}
output_str2 = the_template.substitute(args)
print(output_str2)

"""Format Function"""
foo = "foo"
bar = 123
print("Output: {}, {}".format(foo, bar))

"""String Interpolation"""
import datetime

product = "Widget"
price = 19.99
tax = 0.07
nyd = datetime.datetime(2021, 1, 1)

print(f"{product} has a price of {price} with tax {tax:.2%} the total is {round(price+(price*tax), 2)}")
print(f"But only applicable on {nyd:%B %d %Y}.")
