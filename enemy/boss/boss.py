"""
Boss는 Enemy의 특수한 확장 개념입니다.
이 코드는 기본 적을 포함하여 보스전에 필요한 정보와 동작을 정의하고 있습니다.
"""
from enemy.enemy import Enemy
from entity import Entity
import time

class Boss(Enemy):
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int, behavior_list:list, script:dict, exp:int):
        super().__init__(name, health, attack_power, defense_power, behavior_list, exp)
        self.script:dict = script

    def attack(self, target:Entity):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def after_fight(self):
        for line in self.script["after_fight"]:
            print(line)
            time.sleep(1)

    def show_script(self, situation):
        for line in self.script[situation]:
            print(line)
            time.sleep(1)
