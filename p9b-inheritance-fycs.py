#p9b-Write a program to Python program to implement concepts of OOP such as Inheritance

#Single Inheritance

'''
This program defines an Animal class that has the following attributes:

name: The name of the animal.
species: The species of the animal.
The Animal class also has a make_sound method that can be implemented differently by subclasses. The eat method is common to all animals.

The Dog class inherits from the Animal class and has the following attributes:

name: The name of the animal.
species: The species of the animal.
breed: The breed of the dog.
The Dog class overrides the make_sound method to produce the appropriate sound.

In the main part of the program, a Dog object is created, and its attributes and methods are accessed and called. The make_sound method is called, and the appropriate sound is produced for the dog. The eat method is also called, and the result is printed to the console.
'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, "Canine")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")

    print(my_dog.name, my_dog.species, my_dog.breed)
    my_dog.make_sound()
    my_dog.eat()

#Multi level Inheritance
'''
This program defines an Animal class that has the following attributes:

name: The name of the animal.
species: The species of the animal.
The Animal class also has a make_sound method that can be implemented differently by subclasses. The eat method is common to all animals.

The Dog class inherits from the Animal class and has the following attributes:

name: The name of the animal.
species: The species of the animal.
breed: The breed of the dog.
The Dog class overrides the make_sound method to produce the appropriate sound.

The Puppy class inherits from the Dog class and has the following attributes:

name: The name of the animal.
species: The species of the animal.
breed: The breed of the dog.
age: The age of the puppy.
The Puppy class has a play method that is specific to puppies.

In the main part of the program, a Puppy object is created, and its attributes and methods are accessed and called. The make_sound method is called, and the appropriate sound is produced for the puppy. The eat and play methods are also called, and the results are printed to the console.
'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, "Canine")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Puppy(Dog):
    def __init__(self, name, breed, age):
        Dog.__init__(self, name, breed)
        self.age = age

    def play(self):
        print(f"{self.name} is playing.")

if __name__ == "__main__":
    my_puppy = Puppy("Buddy", "Golden Retriever", 2)

    print(my_puppy.name, my_puppy.species, my_puppy.breed, my_puppy.age)
    my_puppy.make_sound()
    my_puppy.eat()
    my_puppy.play()


#Heirarchical Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, "Canine")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name, "Feline")
        self.color = color

    def make_sound(self):
        print("Meow!")

if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")
    my_cat = Cat("Whiskers", "Gray")

    print(my_dog.name, my_dog.species, my_dog.breed)
    my_dog.make_sound()
    my_dog.eat()

    print(my_cat.name, my_cat.species, my_cat.color)
    my_cat.make_sound()
    my_cat.eat()
'''
This program defines an Animal class that has the following attributes:

name: The name of the animal.
species: The species of the animal.
The Animal class also has a make_sound method that can be implemented differently by subclasses. The eat method is common to all animals.

The Dog and Cat classes inherit from the Animal class and have the following attributes:

name: The name of the animal.
species: The species of the animal.
The Dog and Cat classes override the make_sound method to produce the appropriate sound.

In the main part of the program, a Dog and a Cat object are created, and their attributes and methods are accessed and called. The make_sound method is called, and the appropriate sound is produced for each animal. The eat method is also called, and the result is printed to the console.

In this example, the Animal class is the parent class, and the Dog and Cat classes are child classes. The Dog and Cat classes inherit from the Animal class, but they do not inherit from each other. This is an example of hierarchical inheritance.'''


#Multiple Inheritance 
'''

In this example, we have three classes: First, Second, and MultipleInheritance. The MultipleInheritance class inherits from both First and Second classes.

In the MultipleInheritance class, we call the constructors of both parent classes using First.__init__(self) and Second.__init__(self). This is important because if we don't do this, the parent class attributes will not be initialized.

Finally, we create an instance of the MultipleInheritance class, and display the attributes of each class.

Note: In Python, it is recommended to use the super() function instead of calling the parent class constructor directly. This is because super() takes care of the method resolution order (MRO) and calls the appropriate parent class method. However, in some cases, you may need to call the parent class constructor directly, as shown in this example
'''

class First:
    def __init__(self):
        self.part1 = 'This is the first class.'

    def display_part1(self):
        print(self.part1)

class Second:
    def __init__(self):
        self.part2 = 'This is the second class.'

    def display_part2(self):
        print(self.part2)

class MultipleInheritance(First, Second):
    def __init__(self):
        First.__init__(self)
        Second.__init__(self)
        self.part3 = 'This is the third class.'

    def display_part3(self):
        print(self.part3)

# Create an instance of MultipleInheritance
obj = MultipleInheritance()

# Display the attributes of each class
obj.display_part1()
obj.display_part2()
obj.display_part3()






