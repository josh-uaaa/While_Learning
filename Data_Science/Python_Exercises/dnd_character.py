import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolled_values = []
        for i in range(4):
            rolled_values.append(random.randint(1, 6))
        return sum(rolled_values) - min(rolled_values)

def modifier(value):
    return (value - 10) // 2