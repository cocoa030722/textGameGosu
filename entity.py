from status import Status

import random

class Entity:
    """
    모든 객체가 상속할 것을 보장하는 최상위 인터페이스입니다.
    """
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int):
        self.name:str = name
        self.health:int = health
        self.attack_power:int = attack_power
        self.defense_power:int = defense_power
        self.status:Status = Status.NORMAL
        self.mp:int = 100
        self.max_mp:int = 100
        # TODO:미래에 speed에 따른 우선 행동 구현
        self.speed = 100
        self.attack_probability = 100
    def take_damage(self, attack_power:int):
        damege = (attack_power - self.defense_power) if (attack_power - self.defense_power)>0 else 0
        self.health -= damege
        print(f"{self.name} takes {damege} damage!")

    def attack(self, target:"Entity"):
        prob = random.randint(0, 100)
        print("공격 확률:", prob, self.attack_probability)
        
        if prob <= self.attack_probability:
            print(f"{self.name} attacks {target.name}!")
            target.take_damage(self.attack_power)
        else:
            print("공격 실패!")
            
        
    def appear(self) -> None:
        print(f"{self.name} 등장")

    def show_info(self) -> None:
        print(f"이름:{self.name}")
        print(f"hp:{self.health}")
        print(f"공격력:{self.attack_power}")
        print(f"방어력:{self.defense_power}")
        print(f"상태:{self.status}")

    def pre_turn(self):
        if self.status == Status.PARALYSIS:
            self.attack_probability = 10
        else:
            self.attack_probability = 100
            
        self.mp = min(self.max_mp, self.mp + 10)
        
        
    def post_turn(self):
        if self.status == Status.POISON:
            self.health -= 5
        