class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def print_name(self):
        print(f"名前: {self.name}")
        
    def print_species(self):
        print(f"種類: {self.species}")

animals = []

for i in range(3):
    name = input(f"{i+1}匹目の動物の名前を入力してください:")
    
    species = input(f"{i+1}匹目の動物の種類を入力してください:")
    
    new_animal = Animal(name, species)
    animals.append(new_animal)
    
for animal in animals:
    animal.print_name()
    animal.print_species()