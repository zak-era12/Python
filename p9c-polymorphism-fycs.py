#9c-polymorphism
'''
In this example, we have an Animal class with a speak method. This method is not implemented in the Animal class, but it is declared with a raise NotImplementedError statement. This means that any subclass of Animal must implement the speak method.

We have two subclasses of Animal: Dog and Cat. Both of these subclasses implement the speak method, returning a string that represents the sound the animal makes.

The animal_speak function takes an Animal object as an argument and calls the speak method on it. This allows us to pass any object that is an instance of a subclass of Animal to the animal_speak function, and it will call the speak method on that object.

Finally, we create a list of Animal objects, where each object is an instance of a subclass of Animal. We then iterate over this list and call the animal_speak function on each object. This demonstrates polymorphism, as the animal_speak function can work with any object that is an instance of a subclass of Animal, even though it doesn't know the specific type of each object.
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def animal_speak(animal):
    print(animal.speak())

animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    animal_speak(animal)
