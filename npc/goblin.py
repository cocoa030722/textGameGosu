from npc.entity import Entity

class Goblin(Entity):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(10)
        
    def take_damage(self, amount):
        super().take_damage(amount)