from abc import ABC, abstractmethod

class Entity(ABC):
    """
    모든 객체가 상속할 것을 보장하는 최상위 인터페이스입니다.
    """
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int):
        self.name:str = name
        self.health:int = health
        self.attack_power:int = attack_power
        self.defense_power:int = defense_power

    def take_damage(self, attack_power:int):
        damege = (attack_power - self.defense_power) if (attack_power - self.defense_power)>0 else 0
        self.health -= damege
        print(f"{self.name} takes {damege} damage!")

    def attack(self, target:"Entity"):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def appear(self) -> None:
        print(f"{self.name} 등장")

    def show_info(self) -> None:
        print(f"이름:{self.name}")
        print(f"hp:{self.health}")
        print(f"공격력:{self.attack_power}")
        print(f"방어력:{self.defense_power}")
        