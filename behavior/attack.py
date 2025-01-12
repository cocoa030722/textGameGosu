
from .behavior import AttackBehavior
from status import Status
from entity import Entity

class CommonAttack(AttackBehavior):
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        return {
            "result": f"{attacker.name}의 일반 공격!",
            "damage": attacker.attack_power
        }

class SpreadPoison(AttackBehavior):
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        return {
            "result": f"{attacker.name}:독을 뿌렸다!",
            "status": Status.POISON,
            "damage": attacker.attack_power
        }

class SpreadParalyzingPowder(AttackBehavior):
    def execute(self, attacker: Entity, target: Entity, **kwargs) -> dict:
        return {
            "result": f"{attacker.name}:마비가루를 뿌렸다!",
            "status": Status.PARALYSIS,
            "damage": attacker.attack_power
        }
