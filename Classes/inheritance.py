class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound
        # if 'type' in kwargs:
        #     self._type = kwargs['type']
        # if 'name' in kwargs:
        #     self._type = kwargs['name']
        # if 'sound' in kwargs:
        #     self._sound = kwargs['sound']

    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._type
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    def __str__(self):
        return "The {}'s name is {} and it {}.".format(self._type, self._name, self._sound)


class Kitten(Animal):
    def __init__(self, type, name, sound):
        #     self.type = 'kitty'
        #     if 'type' in kwargs:
        #         del kwargs['type']
        super().__init__(type, name, sound)


class Duck(Animal):
    def __init__(self, type, name, sound):
        # self.type = "duck"
        # if "type" in kwargs:
        #     del kwargs["type"]
        super().__init__(type, name, sound)


def main():
    a0 = Kitten("Kitty", "Kat", "meow")
    a1 = Duck("duck", "Donald", "quack")
    print(a0)
    print(a1)


if __name__ == "__main__":
    main()
