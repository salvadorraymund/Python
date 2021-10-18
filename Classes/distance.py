class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def x(self, x=0):
        if x:
            self._x = x
        try:
            return self._x
        except AttributeError:
            return None

    def y(self, y=0):
        if y:
            self._y = y
        try:
            return self._y
        except AttributeError:
            return None

    # def p(self, p=0):
    #     if p:
    #         self._p = p

    def __str__(self):
        return "({}, {})".format(self._x, self._y)

    def reflect_x(self):
        if self._x != None:
            return "({}, {})".format(self._x, self._y * -1)

    def slope_from_origin(self):
        return "{}".format(float((0 - self._y) / (0 - self._x)))

    # def __getitem__(self, ind):
    #     return self.p[ind]

    def get_line_to(self, p):

        m = float((p.y() - self._y) / (p.x() - self._x))
        y = p.y()
        x = p.x()
        b = y - (p.x() * m)
        return "({}, {})".format(m, b)
        # How to make an object subscriptable?



# a = Point(4, 10)
# print(a)
# print(a.reflect_x())
# origin = Point()
# print(origin)
# print(a.slope_from_origin())
c = Point(4, 11)
print(c.x())
print(c.y())
print(c.get_line_to(Point(6, 15)))
