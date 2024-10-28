class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def instigate(self, opponent_name):
        print(f"{self.name}: I am going to fight you {opponent_name}")

    def attack(self, opponent): 
        print(f"{self.name} attacks {opponent.name}.")
        print(f"{self.name} deals {self.strength} damage.")
        opponent.health = opponent.health - self.strength
        print(f"{opponent.name} has {opponent.health} health remaining.")



character_1 = Character("Bob", 100, 20)
character_2 = Character("Opal", 150, 15)


# print(character_1.name, character_1.health)
# print(character_2.name, character_2.health)

# character_1.greet()
# character_2.greet()

character_1.instigate(character_2.name)
character_2.instigate(character_1.name)

character_1.attack(character_2)
