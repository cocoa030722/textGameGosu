
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:  # 타입 검사 시에만 import
    from entity import Entity
    from ally import Ally

class Behavior(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class AttackBehavior(Behavior):
    @abstractmethod
    def execute(self, attacker: "Entity", target: "Entity", **kwargs) -> dict:
        pass

class SupportBehavior(Behavior):
    @abstractmethod
    def execute(self, supporter: "Ally", allies: List["Entity"], **kwargs) -> dict:
        pass
