class Animal:

    def __init__(self, type, name, sound):
        # the variables below are object variables
        # they only exist when an object is instantiated to a class
        # they do not exist within the class itself
        self._type = type
        self._name = name
        self._sound = sound

    def type(self, t=None):
        if t:
            self._type = type
        return self._type

    def name(self, n=None):
        if n:
            self._name = name
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = sound
        return self._sound

    def __str__(self):
        return "The {}'s name is {} and it {}.".format(self._type, self._name, self._sound)

    # below is an example of a class variable
    # the object doesn't have the data below but is drawing
    # it from the class
    # they are not encapsulated to the object and only exist in the class
    x = [1, 2, 3]


def main():
    a0 = Animal("kitty", "Kat", "meow")
    a1 = Animal("duck", "Donald", "quack")
    print(a0)
    print(a1)
    a0.x[0] = 31
    print(a1.x)


if __name__ == "__main__":
    main()
