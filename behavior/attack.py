from .behavior import Behavior
from status import Status
class CommonAttack(Behavior):
    def execute(self, enemy, **kwargs)->dict:
        return {
            "result":f"{enemy.name}:일반 공격!"
        }

class SpreadPoison(Behavior):
    def execute(self, enemy, **kwargs)->dict:
        return {
            "result":f"{enemy.name}:독을 뿌렸다!",
            "status":Status.POISON
        }

class SpreadParalyzingPowder(Behavior):
    def execute(self, enemy, **kwargs)->dict:
        return {
            "result":f"{enemy.name}:마비가루를 뿌렸다!",
            "status":Status.PARALYSIS
        }