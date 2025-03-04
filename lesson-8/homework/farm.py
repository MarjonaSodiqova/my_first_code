class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")
    
    def eat(self, food):
        print(f"{self.name} is eating {food}.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child Classes
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
    
    def lay_egg(self):
        print(f"{self.name} laid an egg!")

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep", "Baa")
    
    def shear(self):
        print(f"{self.name} is being sheared for wool.")

# Example Usage
if __name__ == "__main__":
    cow = Cow("Bessie")
    chicken = Chicken("Henrietta")
    sheep = Sheep("Dolly")
    
    cow.make_sound()
    cow.eat("grass")
    cow.produce_milk()
    
    chicken.make_sound()
    chicken.eat("corn")
    chicken.lay_egg()
    
    sheep.make_sound()
    sheep.eat("hay")
    sheep.shear()
