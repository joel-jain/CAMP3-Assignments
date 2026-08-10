#Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")

class Puppy(Dog):
    def __init__(self, name, breed, age_months):
        super().__init__(name, breed)
        self.age_months = age_months

    def play(self):
        print(f"{self.name} is playing")

obj_puppy = Puppy("Tommy", "Labrador", 3)

obj_puppy.eat()
obj_puppy.bark()
obj_puppy.play()
