class Book:
        # the init function is called when the instance is created and ready
        # to be initialized
    # below is an example of instance method
    def __init__(self, title, author, page, price):
        # below is an example of instance attributes
        self.title = title
        self.author = author
        self.page = page
        self.price = price
        self.__secret = "This is a secret"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    # this is another example of an instance attribute
    def setdiscount(self, amount):
        self._discount = amount
        # underscore to begin the name of the method gives a hint to other developers that this method only
        # exist in this class and cannot be called out outside of it

    # def printsecret(self):
    #     print(self.__secret)


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.99)
b2 = Book("The Catcher in the Rye", "JD Sullinger", 243, 29.99)

print(b1.getprice())
print(b2.getprice())
b2.setdiscount(.25)
print(b2.getprice())
