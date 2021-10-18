class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

    def what_am_i(self):
        return 'Rectangle'


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


class Cube(Square):
    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        # you want to make sure that cube class will not use square class' area method and
        # instead look above the rectangle class for its area method
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return self.what_am_i() + ' child of ' + super().what_am_i()


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


shape2 = Square(4)
print(shape2.area())
shape3 = Cube(3)
print(shape3.surface_area())
print(shape3.family_tree())
shape4 = RightPyramid(2, 3)
print(shape4.area())
