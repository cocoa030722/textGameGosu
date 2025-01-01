from abc import ABC, abstractmethod

class Entity(ABC):
    """
    모든 객체가 상속할 것을 보장하는 최상위 인터페이스
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage!")
        