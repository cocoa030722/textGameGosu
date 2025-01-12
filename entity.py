
from status import Status
from stats import Stats
import random

class Entity:
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int):
        self.name:str = name
        self.stats = Stats(health, attack_power, defense_power)
        self.status:Status = Status.NORMAL
        self.mp:int = 100
        self.max_mp:int = 100
        self.speed = 100
        self.attack_probability = 100

    def take_damage(self, attack_power:int):
        damage = self.stats.take_damage(attack_power)
        print(f"{self.name} takes {damage} damage!")

    def attack(self, target:"Entity"):
        prob = random.randint(0, 100)
        print("공격 확률:", prob, self.attack_probability)
        
        if prob <= self.attack_probability:
            print(f"{self.name} attacks {target.name}!")
            target.take_damage(self.stats.attack_power)
        else:
            print("공격 실패!")
            
    def appear(self) -> None:
        print(f"{self.name} 등장")

    def show_info(self) -> None:
        print(f"이름:{self.name}")
        print(f"hp:{self.stats.health}")
        print(f"공격력:{self.stats.attack_power}")
        print(f"방어력:{self.stats.defense_power}")
        print(f"상태:{self.status}")

    def pre_turn(self):
        if self.status == Status.PARALYSIS:
            self.attack_probability = 10
        else:
            self.attack_probability = 100
        self.mp = min(self.max_mp, self.mp + 10)
        
    def post_turn(self):
        if self.status == Status.POISON:
            self.stats.take_damage(5)
