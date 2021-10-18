class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self._length * self._width

    def resize(self, new_length, new_width):
        self._length = new_length
        self._width = new_width


class Square(Rectangle):
    def __init__(self, sides):
        super().__init__(sides, sides)

    def resize(self, new_side_size):
        self.sides = new_side_size


my_rectangle = Rectangle(4, 5)
assert my_rectangle.area == 20
my_square = Square(4)
assert my_square.area == 16
my_rectangle.resize(10, 5)
assert my_rectangle.area == 50
my_square.resize(4)
assert my_square.area == 16
print(f'area of my_square: {my_square.area}')
print('Ok!')
