#p9a-Write a program to Python program to implement concepts of OOP such as Types of Methods
'''
This program defines a Circle class that has the following types of methods:

__init__: A special method that is called when an object is created. It initializes the object with a given radius.
area: A regular method that calculates the area of the circle.
circumference: A regular method that calculates the circumference of the circle.
print_pi: A static method that prints the value of pi.
from_diameter: A class method that creates a circle from a diameter.
The __init__ method is called when an object is created, and it initializes the object with a given radius. The area and circumference methods are regular methods that use the radius attribute to calculate the area and circumference of the circle. The print_pi method is a static method that prints the value of pi. The from_diameter method is a class method that creates a circle from a diameter. It uses the cls argument to create a circle with the correct radius.

In the main part of the program, a Circle object is created with a radius of 5. The area and circumference methods are called, and the results are printed. The print_pi static method is called, and the value of pi is printed. A Circle object is created from a diameter of 10, and the area of the circle is printed.
'''

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.pi * self.radius

    @staticmethod
    def print_pi():
        print("The value of pi is:", Circle.pi)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)


if __name__ == "__main__":
    c = Circle(5)
    print("Area:", c.area())
    print("Circumference:", c.circumference())
    c.print_pi()
    c1 = Circle.from_diameter(10)
    print("Area of c1:", c1.area())
