class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def stop(self):
        self.speed = 0

    def increase_speed(self):
        if self.started:
            self.speed = self.speed
            print("Vroom!")
        else:
            print("You need to start me first!")


class Car(Vehicle):
    def __init__(self, started, speed, color):
        super().__init__(started, speed)
        self.color = color

    trunk_open = False

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroom!")

    def check_speed(self):
        print("You are driving", self.speed, "km/h")

    def open_trunk(self):
        trunk_open = True

    def close_trunk(self):
        trunk_open = False


c1 = Car(False, 0, "blue")
c1.start()
c1.increase_speed(20)
c1.check_speed()
