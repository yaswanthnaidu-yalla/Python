from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def __str__(self):
        return f"{self.name} is a {self.species} and says {self.sound()}"
    def __repr__(self):
        return f"Animal(name={self.name},species={self.species})"

def decorator(func):
    def wrapper(
            *args,**kwargs
    ):
        print("wrappers are like adding a function to another function without changing its code.")
        result = func(*args,**kwargs)
        print("now the function that we r going to put this wrapper on will execute in between these messages")
        print("when the function we're applying this decorator to recieves arguments, the decorator should too, so we will be adding *args and **kwargs")
        return result
    return wrapper

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name,species="Dog")
        self.breed=breed
    def sound(self):
        return "Bark"
    def __str__(self):
        return f"{self.name} is a {self.species}({self.breed}) and says {self.sound()}"

class Cat(Animal):
    @decorator
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed
    def sound(self):
        return "Meow"
    
    
rex = Dog("Rex","Labrador")
meow = Cat("meow","Maine coon")
print(meow)
