
from abc import ABC, abstractmethod
from entity import Entity

class Behavior(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class AttackBehavior(Behavior):
    @abstractmethod
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        pass

class SupportBehavior(Behavior):
    @abstractmethod
    def execute(self, supporter: Entity, allies: list[Entity], **kwargs) -> dict:
        pass
