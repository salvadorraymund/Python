def main():
    seq = range(11)
    seq2 = {i: i ** 2 for i in seq}
    print_list(seq)
    print(seq2)


def print_list(o):
    for x in o:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
