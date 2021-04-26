class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True
        print(self.name + " is sitting down.")

    def stand_up(self):
        self.isSitting = False
        print(self.name + " is standing up.")

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "red"
# r2.weight = 40


r1 = Robot("Raymund", "red", 30)
r2 = Robot("Mela", "blue", 40)

r1.introduce_self()
r2.introduce_self()

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)
p1.sit_down()
p1.stand_up()

p1.robot_owned = r2
p2.robot_owned = r1
