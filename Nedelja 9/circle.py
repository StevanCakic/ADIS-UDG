class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * Circle.pi

    def set_radius(self, new_radius):
        self.__radius = new_radius

    def get_radius(self):
        return self.__radius

c = Circle(10)

print(c.area())


c.set_radius(20)

print(c.area())

print(c.get_radius())
