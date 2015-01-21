# class Point:
#
#     def __init__(self, first, second):
#         self.first_value = first
#         self.second_value = second
#
#     def __add__(self, other):
#         return self.first_value + self.other
#
#     def __sub__(self, other):
#         return self.first_value - self.other
#
#     def __str__(self):
#         value =
#         return value


class Point:
    """A class implementation of 2-Dimensional point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '( %d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y


point1 = Point(8, 5)
point2 = Point(-6, 1)

print(point1 + point2)
print(point1 - point2)