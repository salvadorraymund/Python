def is_leap(year):
    leap = False

    if year % 4 != 0:
        return leap
    else:
        # return True
        if year % 100 == 0 and year % 400 != 0:
            return leap
        else:
            return True


year = int(1800)
print(is_leap(year))
