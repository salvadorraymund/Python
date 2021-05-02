def is_palindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        print(reversed_num)
        temp = temp // 10
        # print(temp)

    if num == reversed_num:
        return True
    else:
        return False


print(is_palindrome(131))

# a = []
# a = [x ** 2 for x in range(6, 0, -1)]
# print(a)

# movies = ["Star Wars", "Gandhi", "Gone with the wind", "Citizen Kane",
#           "The Wizard of Oz", "Gattaca", "Ghost in a Shell"]

# list comprehension format:
# title = expression
# followed by the loop
# gmovies = [title for title in movies if title.startswith("G")]
# print(gmovies)

new_movies = [("Citizen Kane", 1941),
              ("Spirited Away", 2001),
              ("Gattaca", 1997), ("No Country for Old Men", 2007),
              ("LOTR", 2001), ("The Aviator", 2004)]

before_millenium_movies = [title for title in new_movies if title[1] < 2000]
print(before_millenium_movies)

pre2k = [title for (title, year) in new_movies if year < 2000]
print(len(pre2k))

# A = [1, 3, 5, 7]
# B = [2, 4, 6, 8]

# cartesian_product = [(a, b) for a in A for b in B]
# print(cartesian_product)
