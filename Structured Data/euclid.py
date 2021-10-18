from math import remainder


def GCD(var1, var2):
    """
    Gets the GCD of var1 and var2
    """
    r = remainder(var1, var2)
    if r != 0:
        while r != 0:
            var1 = var2
            var2 = r
            euclid = remainder(var1, r)
            return euclid
            continue
    else:
        return n


# Apply Euclid's Algortihm to find the GCD of the following pairs:
# 2057 and 1331
# 469 and 3982
# 610 and 377
# 611953 and 541
exercise_list = [(2057, 1331), (469, 3982), (610, 377), (611953, 541)]


def euclid(list):
    """
    Takes a list which has tuple as its elements and get the GCD of each tuple
    """
    for e in exercise_list:
        gcd = GCD(e[0], e[1])
        print(gcd)
        # for i in e:
        #     gcd = GCD(e[0], e[1])
        #     print(f"The greatest common denominator of the following list {exercise_list} are as follows {gcd}.")


euclid = euclid(exercise_list)
