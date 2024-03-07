#Write a program to Python program to implement concepts of OOP such as Abstract methods and classes
'''
In this example, we have an Animal class that is an abstract class (using the ABC metaclass). The Animal class has an abstract method speak that is not implemented in the Animal class, but it is declared with the @abstractmethod decorator. This means that any subclass of Animal must implement the speak method.
We have two subclasses of Animal: Dog and Cat. Both of these subclasses implement the speak method, returning a string that represents the sound the animal makes.
The animal_speak function takes an Animal object as an argument and calls the speak method on it.
Finally, we create a list of Animal objects, where each object is an instance of a subclass of Animal. We then iterate over this list and call the animal_speak function on each object. This demonstrates polymorphism, as the animal_speak function can work with any object that is an instance of a subclass of Animal, even though it doesn't know the specific type of each object.
The use of abstract classes and methods in this example ensures that any subclass of Animal must implement the speak method, which enforces a contract for any subclass of Animal. This is a powerful way to ensure that objects of a certain class have certain methods and behavior, and can help prevent
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())

animals = [Dog(), Cat()]

for animal in animals:
    animal_speak(animal)