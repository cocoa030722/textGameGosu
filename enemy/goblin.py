from entity import Entity

class Goblin(Entity):
    def __init__(self, name, health, attack_power, defense_power):
        super().__init__(name, health, attack_power, defense_power)

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def take_damage(self, attack_power):
        super().take_damage(attack_power)
    def appear(self):
        super().appear()

    def show_info(self):
        super().show_info()