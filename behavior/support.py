"""
일단 dict를 반환하는 방법으로 구현
DTO로 할지 어쩔지 감이 안잡힘
"""

from .behavior import SupportBehavior #Added SupportBehavior import
from condition import Condition

class HealingSupport(SupportBehavior):
    def execute(self, supporter: "Ally", allies: list["Entity"], **kwargs) -> dict:
        heal_amount = 20
        if hasattr(supporter, 'compliance') and supporter.compliance > 70:
            heal_amount += 10

        return {
            "result": f"{supporter.name}이(가) {heal_amount}만큼 회복해줍니다!",
            "heal_amount": heal_amount
        }

class DefenseBoost(SupportBehavior):
    def execute(self, supporter: "Ally", allies: list["Entity"], **kwargs) -> dict:
        defense_boost = 5
        if hasattr(supporter, 'compliance') and supporter.compliance > 70:
            defense_boost += 5

        return {
            "result": f"{supporter.name}이(가) 방어력을 {defense_boost}만큼 올려줍니다!",
            "defense_boost": defense_boost
        }

class RemovePoison(SupportBehavior):
    def execute(self, supporter: "Ally", allies: list["Entity"], **kwargs) -> dict:
        return {
            "result": f"{supporter.name}이(가) 독을 치료해줍니다!",
            "status": Condition.NORMAL
        }