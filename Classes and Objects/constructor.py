class Animal:
    def __init__(self, type, name, sound):
    	# underscore at the beginning of each variable denotes that these object variables should not be touched
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def main():
    def animal_sound(o):
        if isinstance(o, Animal):
            print("The {} is named as {} and it {}".format(
                o.type(), o.name(), o.sound()))
        else:
            raise TypeError("This is not an animal")

    a0 = Animal('kitty', 'Kat', 'meows')
    a1 = Animal('duck', 'Donald', 'quacks')
    animal_sound(a0)
    animal_sound(a1)
    animal_sound(Animal("velociraptor", "Verinica", "brrrs"))


if __name__ == "__main__":
    main()
