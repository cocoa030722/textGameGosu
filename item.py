
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    @abstractmethod
    def use(self, player):
        pass

class HealthPotion(Item):
    def __init__(self, heal_amount=30):
        super().__init__("Health Potion", "Restores health when consumed")
        self.heal_amount = heal_amount
        
    def use(self, player):
        player.health += self.heal_amount
        print(f"{player.name} restored {self.heal_amount} health!")

class Weapon(Item):
    def __init__(self, name, attack_bonus):
        super().__init__(name, f"Increases attack power by {attack_bonus}")
        self.attack_bonus = attack_bonus
        
    def use(self, player):
        player.attack_power += self.attack_bonus
        print(f"{player.name}'s attack power increased by {self.attack_bonus}!")
