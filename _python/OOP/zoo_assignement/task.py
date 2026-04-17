# Animal  - paerent class
 
class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
 
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
 
    def feed(self, health_increase=10, happiness_increase=10):
        self.health += health_increase
        self.happiness += happiness_increase
 
 
class Lion(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
 
    def roar(self):
        print(f"{self.name} roars loudly!")
 
    def feed(self):
        return super().feed(health_increase=20, happiness_increase=20)
 
class Monkey(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
 
    def climb(self):
        print(f"{self.name} climbs a tree!")
 
    def feed(self):
        return super().feed(health_increase=5)
 
class Elephant(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
 
    def trumpet(self):
        print(f"{self.name} trumpets loudly!")
 
    def feed(self):
        return super().feed(health_increase=15, happiness_increase=5)
 
# Zoo
 
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
 
   
 
    def add_animal(self, animal):
        self.animals.append(animal)
 
 
    def add_compsition(self, type, name, age, health, happiness):
        if type == "Lion":
            new_animal = Lion(name, age, health, happiness)
        elif type == "Monkey":
            new_animal = Monkey(name, age, health, happiness)
        elif type == "Elephant":
            new_animal = Elephant(name, age, health, happiness)
        else:
            print("Invalid animal type!")
            return
        self.add_animal(new_animal)
 
 
    def print_all_info(self):
        print(f"Welcome to {self.name}!\n")
        for animal in self.animals:
            animal.display_info()
            print("-----------------------------")
 
 
# Create a zoo and add animals
 
zoo = Zoo("City Zoo")
lion = Lion("Leo", 5, 80, 70)
monkey = Monkey("Momo", 3, 60, 80)
elephant = Elephant("Ella", 10, 90, 60)
 
zoo.add_animal(lion)
zoo.add_animal(monkey)
zoo.add_animal(elephant)
 
# Display information about all animals in the zoo
zoo.print_all_info()