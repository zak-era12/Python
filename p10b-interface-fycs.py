#p10b- Interfaces in python
'''
In the example provided, interfaces in Python are implemented using abstract methods in a base class, and concrete classes that inherit from this base class and implement the abstract methods.
In this example, IParser is the interface (abstract base class) that defines the abstract methods load_data_source and extract_text. The concrete classes PdfParser and EmlParser inherit from IParser and implement the abstract methods defined in the interface.
In this example, Animal is the interface (abstract base class) that defines the abstract method speak. The concrete classes Dog, Cat, and Bird inherit from Animal and implement the abstract methods.
When we create a list of animals and iterate over it, each animal's speak method is called, and the animal's sound is printed.
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

class Bird(Animal):
    def speak(self):
        return "Chirp!"

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(animal.speak())


