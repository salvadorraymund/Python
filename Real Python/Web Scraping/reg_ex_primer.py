import re

# search for the pattern ab*c in the expression ac
# Regular expression ab*c matches any part of the string that begins with an "a"
# and ends with a "c", and has zero instances of "b" between them
# print(re.findall("ab*c", "ac"))
# print(re.findall("ab*c", "abcd"))
# print(re.findall("ab*c", "acc"))
# print(re.findall("ab*c", "abac"))
# print(re.findall("ab*c", "abdc"))
pattern = "ab*c"

# Pattern matching is case sensitive
ex1 = re.findall(pattern, "ABC")
print(ex1)

# pass in re.IGNORECASE as third argument to ignore case sensitivity
ex1 = re.findall(pattern, "ABC", re.IGNORECASE)
print(ex1)

# using period(.) to stand for any single character
# in the example below, finding all the strings that contains the letter "a" and "c" separated by a single character
ex2 = re.findall("a.c", "abc")
print(ex2)

# period(.) can only stand for 1 character
ex3 = re.findall('a.c', 'abbc')
print(ex3)

# The pattern .* inside a regular expression stands for any character repeated any number of times.
pattern2 = "a.*c"
ex4 = re.findall(pattern, "abc")
print(ex4)
ex5 = re.findall(pattern, "abbc")
print(ex5)

match_results = re.search(pattern, 'ABC', re.IGNORECASE)
print(match_results.group())

string = "Everything is <replaced> if it's in <tags>"
my_string = re.sub("<.*>", "ELEPHANTS", string)
print(my_string)

string2 = re.sub("<.*?>", "ELEPHANTS", string)
print(string2)
