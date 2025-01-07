from .boss import Boss
import utils

import time

class Alchemist(Boss):
    def __init__(self, name, health, attack_power, defense_power):
        super().__init__(name, health, attack_power, defense_power)
        self.script:dict = utils.load_json("json/boss_alchemist.json")
        print(self.script)

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def take_damage(self, attack_power):
        super().take_damage(attack_power)
        
    def appear(self):#TODO:상위의 Boss 클래스로 옮기고, 이벤트 상황을 인수로 받아 일반화
        for line in self.script["before_fight"]:
            print(line)
            time.sleep(1)

    def after_fight(self):
        
        for line in self.script["after_fight"]:
            print(line)
            time.sleep(1)
            
    def show_info(self):
        super().show_info()