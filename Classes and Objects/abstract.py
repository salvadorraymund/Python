from abc import ABC, abstractmethod

# class GrahicShape serves as a common base class for the
# other classes. It's meant to be instantiated
# because GraphicShape has abstractmethod, it cant be
# instantiated
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass
# we use the pass in methods of base classes for reusability

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

# g = GraphicShape()


c = Circle(10)
print(c.calcArea())
s = Square(5)
print(s.calcArea())
