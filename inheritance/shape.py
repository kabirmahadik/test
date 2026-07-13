class Shape:
    def __init__(self):
        print("Shape object created")

    def display(self):
        print("This is a Shape")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def show(self):
        self.display()
        print("Radius :", self.radius)
        print("Area   :", self.area())


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def show(self):
        self.display()
        print("Length  :", self.length)
        print("Breadth :", self.breadth)
        print("Area    :", self.area())


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def show(self):
        self.display()
        print("Base   :", self.base)
        print("Height :", self.height)
        print("Area   :", self.area())


circle = Circle(7)
circle.show()

print("-" * 30)

rectangle = Rectangle(10, 5)
rectangle.show()

print("-" * 30)

triangle = Triangle(8, 6)
triangle.show()