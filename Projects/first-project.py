

def say_hi(name):
    if name == '':
        print("You didn't enter your name")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)

name = input("Please enter your name")
say_hi(name)
