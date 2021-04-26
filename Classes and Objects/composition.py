class Book:
    def __init__(self, title, price, author=None, section=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

        self.section = section

    def addchapters(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

    def getsection(self, section):
        self.section = section
        return section


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


class Section:
    def __init__(self, genre):
        self.genre = genre

    def __str__(self):
        return f"{self.genre}"


genre = Section("classic")
auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39, auth, genre)

b1.addchapters(Chapter("Chapter 1", 125))
b1.addchapters(Chapter("Chapter 2", 97))
b1.addchapters(Chapter("Chapter 3", 143))

print(b1.getsection(Section("Classic")))

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())


class Basic:
    def __init__(self, x=20, y=8):
        self.x = x
        self.y = y

    def Addition(self):
        return self.x + self.y

    def Subtraction(self):
        return self.x - self.y

    def Times_table(self):
        for i in range(1, self.y):
            print("%i * %i = %i" % (i, self.y, (i * self.y)))


b = Basic(3, 4)
print(b.Addition())
print(b.Subtraction())
b.Times_table()


class Advanced(Basic):
    def __init__(self, x=20, y=8):
        super().__init__(x, y)

    def Multiply(self):
        return self.x * self.y


a = Advanced(5, 6)
a.Times_table()


class Comp:
    def __init__(self):
        self.base = Basic()

    def Multiply(self):
        return self.base.x * self.base.y

    def Times_y(self):
        return self.base.Times_table()

# you cannot add arguments when you try to instantiate an object to the class when using this method
c = Comp()
print(c.Multiply())
