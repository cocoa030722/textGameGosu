from entity import Entity
import time

class Alchemist(Entity):
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
        
    def appear(self):#TODO:상위의 Boss 클래스로 올옮기기고, 이벤트 상황을 인수로 받아 일반화
        for line in self.script["before_fight"]:
            print(line)
            time.sleep(0.5)

    def after_fight(self):
        for line in self.script["after_fight"]:
            print(line)
            time.sleep(0.5)
            
    def show_info(self):
        super().show_info()