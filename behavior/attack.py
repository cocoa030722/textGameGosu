
from .behavior import Behavior
from status import Status

class AttackData:
    def __init__(self, result:str, status=Status.NORMAL):
        # 출력할 텍스트
        self.result:str = result
        # 상태이상 등 구현
        self.status = status
        
class AttackBehavior(Behavior):
    def execute(self, enemy, **kwargs)->AttackData:
        return AttackData(
            result=f"{enemy.name}:일반 공격!"
        )
        
class CommonAttack(Behavior):
    def execute(self, enemy, **kwargs)->AttackData:
        return AttackData(
            result=f"{enemy.name}:일반 공격!"
        )

class SpreadPoison(Behavior):
    def execute(self, enemy, **kwargs)->AttackData:
        return AttackData(
            result=f"{enemy.name}:독을 뿌렸다!",
            status=Status.POISON
        )

class SpreadParalyzingPowder(Behavior):
    def execute(self, enemy, **kwargs)->AttackData:
        return AttackData(
            result=f"{enemy.name}:마비가루를 뿌렸다!",
            status=Status.PARALYSIS
        )