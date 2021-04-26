class Car:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Car started, let's go!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroom!")
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print("Halting")


# car = Car()
# car.increase_speed(10)
# car.start()
# car.increase_speed(40)

car1 = Car()
car2 = Car(started=True, speed=10)
car1.start()
car1.increase_speed(10)
car2.stop()


# print ("car.py__name__ = %s" % __name__)

# if __name__ == "__main__":
#     print("car.py is run directly")
# else:
#     print("car.py is being imported")

print(car1)
print(car1.speed)
