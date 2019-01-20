class Circle(object):
    @staticmethod
    def area(radius):
        return (22/7.0)*radius*radius
area = Circle.area(10)
print(area)
# Output: 314.285714286