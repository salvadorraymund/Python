def main():
    kitten(Buffy="meow", Zilla="grr", Angel="rawr")


def kitten(**kwargs):
         # if len == 0, it's false and it will run the else clause, anything
         # greater than 0 is 1 and it'll return true
    if len(kwargs):
        for k in kwargs:
            print("Kitten {} says {}".format(k, kwargs[k]))
    else:
        print("Meow")


if __name__ == "__main__":
    main()
