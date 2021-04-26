class Dog:
        # the below is an example of a class variable
        # useful if you want to use variables that will be repeatedly referenced within a class
    DOGS = []

    def __init__(self, name):
        # example of instance attribute
        self.name = name
        self.DOGS.append(name)

    def setName(self, newname):
        self.name = newname

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print("Bark!")


tim = Dog("Tim")
jim = Dog("Jim")

tim(Dog.setName("Josh"))
