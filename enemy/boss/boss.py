from entity import Entity
import time

class Boss(Entity):
    def __init__(self, name, health, attack_power, defense_power):
        super().__init__(name, health, attack_power, defense_power)
        self.script:dict = {
            "before_fight":["전투 전 대사 1", "전투 전 대사 2"],
            "after_fight":["전투 후 대사 1", "전투 후 대사 2"],
        }

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def take_damage(self, attack_power):
        super().take_damage(attack_power)

    def after_fight(self):
        
        for line in self.script["after_fight"]:
            print(line)
            time.sleep(1)

    def show_script(self, situation):
        for line in self.script[situation]:
            print(line)
            time.sleep(1)
    def show_info(self):
        super().show_info()