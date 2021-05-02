class Duck:
    def __init__(self):
        self.sound = "Quack quack"
        self.movement = "Walks like a duck"

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
        # Donald is the object. It was instantiated to the class Duck
    donald = Duck()
    print(donald.sound)
    donald.move()


if __name__ == "__main__":
    main()
