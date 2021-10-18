def main():
    with open("newtext.txt", "r+") as f:
        start = 0
        stop = 10
        while start < stop:
            start += 1
            x = start
            f.write(f"{x} This is line {x} \n")
            print(f"{x} This is line {x}")


if __name__ == "__main__":
    main()
