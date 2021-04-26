class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)


c = C()
c.showprops()


class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def showdeets(self):
        print(self.age)
        print(self.name)


class Dancer:
    def __init__(self, style):
        # super().__init__()
        self.style = style


class Student(Human, Dancer):
    def __init__(self, age, name, style):
        Human.__init__(self, age, name)
        Dancer.__init__(self, style)


John = Student(20, "John", "HipHop")
John.showdeets() 
# this shows that John is not just an object instatiated to class
# Student, but to class Human as well
