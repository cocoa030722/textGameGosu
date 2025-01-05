from abc import ABC, abstractmethod

class Entity(ABC):
    """
    모든 객체가 상속할 것을 보장하는 최상위 인터페이스
    """
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

    @abstractmethod
    def take_damage(self, attack_power):
        self.health -= (attack_power - self.defense_power)
        print(f"{self.name} takes {(attack_power - self.defense_power)} damage!")
        
        
    """
    attack, appear
    """
        