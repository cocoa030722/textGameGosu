
from behavior.behavior import AttackBehavior
from condition import Condition

from typing import TYPE_CHECKING
if TYPE_CHECKING:# 타입 검사 시에만 import
    from entity import Entity

class CommonAttack(AttackBehavior):
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        return {
            "result": f"{attacker.name}의 일반 공격!",
            "damage": attacker.get_attack_power()
        }

class SpreadPoison(AttackBehavior):
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        return {
            "result": f"{attacker.name}:독을 뿌렸다!",
            "status": Condition.POISON,
            "damage": attacker.get_attack_power()
        }

class SpreadParalyzingPowder(AttackBehavior):
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        return {
            "result": f"{attacker.name}:마비가루를 뿌렸다!",
            "status": Condition.PARALYSIS,
            "damage": attacker.get_attack_power()
        }
