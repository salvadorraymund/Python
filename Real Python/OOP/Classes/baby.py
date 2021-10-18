class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, language):
        return "{} is fluent in {}".format(self.name, language)

    def eat(self, favorite_dish):
        return "{} loves to eat {} dishes".format(self.name, favorite_dish)

    def action(self, favorite_sport):
        return "{} enjoys {} during his spare time".format(self.name, favorite_sport)


class Baby(Person):
    description = "baby"

    # def __init__(self, name, age):
    #     super().__init__(name, age)

    def speak(self):
        print("ba ba ba ba")

    def eat(self):
        print("{} eats baby food.".format(self.name))


baby1 = Baby("Dokie", 3)
baby1.speak()
baby1.eat()
print(baby1.name)
