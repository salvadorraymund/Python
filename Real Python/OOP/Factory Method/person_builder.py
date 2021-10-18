from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def person_method(self):
        pass


class Student(Person):
    def __init__(self):
        self.name = "Student builder"

    def person_method(self):
        print("I am a Student")


class Teacher(Person):
    def __init__(self):
        self.name = "Teacher builder"

    def person_method(self):
        print("I am Teacher")


def person_builder(choice):
    if choice == "Student" or "student":
        return Student()
    elif choice == "Teacher" or "teacher":
        return Teacher()
    else:
        raise ValueError(choice)


if __name__ == "__main__":
    person_type = input("What do you want to be come?\n")
    person = person_builder(person_type)
    person.person_method()
