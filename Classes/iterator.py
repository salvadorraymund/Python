class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f"Expect 1 argument to be given, got {numargs}")
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self.stop, self._step) = args
        else:
            raise TypeError(f"maximum of three arguments, got {numargs}")

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r


def main():
    for x in inclusive_range(25):
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
