class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def __str__(self):
        return f"{self.name} is a {self.species}"
    def __repr__(self):
        return f"Animal(name={self.name},species={self.species})"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name,species="Dog")
        self.breed=breed
    def __str__(self):
        return f"{self.name}is a {self.species}({self.breed})"
    
rex = Dog("Rex","Labrador")
print(rex)
print(repr(rex))