class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!!".format(self.name, sound)


dog1 = Dog("Tuldok", 4)
print(dog1.description())
print(dog1.speak("Gruff gruff"))
