"""
일단 dict를 반환하는 방법으로 구현
DTO로 할지 어쩔지 감이 안잡힘
"""

from .behavior import Behavior
from status import Status

class SupportData:
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

class HealingSupport(Behavior):
    def execute(self, ally, **kwargs) -> dict:
        heal_amount = 20
        if ally.compliance > 70:
            heal_amount += 10
        
        return {
            "result": f"{ally.name}이(가) {heal_amount}만큼 회복해줍니다!",
            "heal_amount": heal_amount
        }

class DefenseBoost(Behavior):
    def execute(self, ally, **kwargs) -> dict:
        defense_boost = 5
        if ally.compliance > 70:
            defense_boost += 5
            
        return {
            "result": f"{ally.name}이(가) 방어력을 {defense_boost}만큼 올려줍니다!",
            "defense_boost": defense_boost
        }

class RemovePoison(Behavior):
    def execute(self, ally, **kwargs) -> dict:
        return {
            "result": f"{ally.name}이(가) 독을 치료해줍니다!",
            "status": Status.NORMAL
        }
