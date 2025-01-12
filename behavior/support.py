"""
일단 dict를 반환하는 방법으로 구현
DTO로 할지 어쩔지 감이 안잡힘
"""

from .behavior import Behavior
from status import Status

class SupportBehavior:
    def __init__(self, result:str):
        # 출력할 텍스트
        self.result:str = result
        
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


        