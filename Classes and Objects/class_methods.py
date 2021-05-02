class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    # _ at the beginning indicates that it's a private variable and should not be editted
    def type(self, t=None):
        if t:
            self._type = t
        return self.type

    def name(self, n=None):
        if n:
            self._name = n
        return self.name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self.sound

    def __str__(self):
        return ("The {}'s name is {} and it {}".format(self._type, self._name, self._sound))


def main():
    a0 = Animal("kitty", "Kat", "meow")
    a1 = Animal("duck", "Donald", "quacks")
    a0.sound("bark")
    print(a0)
    print(a1)


if __name__ == "__main__":
    main()
