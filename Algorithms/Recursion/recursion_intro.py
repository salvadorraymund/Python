def countdown(x):
    if x < 0:
        raise Exception("Input has to be positive!")
    if (x == 0):
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)

# non-recursive version
def count_down(x):
    while x > 0:
        print(x, "...")
        x -= 1


count_down(10)
