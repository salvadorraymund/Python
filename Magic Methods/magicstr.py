class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

    def __add__(self, price):
        return self.price + self.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# print(b1)
# print(b2)

print(str(b1))
print(repr(b2))
print(b1 + b2)

mylist = ["NBA", "PBA", "NCAA", "UAAP", "MPBL", "SBP", "CBA"]
# example below is a negative
# read as "start 6 then end at 0 with a step of -2"
myslice = mylist[6:0:-2]
print(myslice)

print(hash(b1))
