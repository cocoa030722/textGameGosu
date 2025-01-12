"""
보스전 이후 생성되는 동료의 정보와 행동을 정의합니다.
"""
from entity import Entity
import time

class Ally(Entity):
    def __init__(self, name, health, attack_power, defense_power, resistance:int, compliance:int, script:dict):
        super().__init__(name, health, attack_power, defense_power)
        self.resistance:int = resistance  # 저항도 (높을수록 반항적)
        self.compliance:int = compliance  # 순응도 (높을수록 협조적)
        self.script:dict = script
        
    def behavior_effect(self) -> dict:
        """동료의 저항도와 순응도에 따른 이익/불이익 계산"""
        if self.compliance > 70:
            print(f"{self.name}은(는) 협조적입니다. 추가 도움을 제공합니다!")
            return {"bonus_damage": 10, "bonus_healing": 5}
        elif self.resistance > 70:
            print(f"{self.name}은(는) 저항적입니다. 문제가 생길 수 있습니다.")
            return {"penalty_damage": -10, "penalty_healing": -5}
        else:
            print(f"{self.name}은(는) 평범하게 행동합니다.")
            return {"bonus_damage": 0, "bonus_healing": 0}
    
    
    def reduce_resistance(self, amount:int):
        self._show_script("reduce_resistance")
        self.resistance -= amount
        print(f"{self.name} 저항도가 {amount} 감소했다.")

    def increase_compliance(self, amount:int):
        self._show_script("increase_compliance")
        self.compliance += amount
        print(f"{self.name} 순응도가 {amount} 증가했다.")

    def martial_law(self):
        self._show_script("martial_law")
        self.resistance = 0
        self.compliance = 100
        
    def _show_script(self, situation):
        for line in self.script[situation]:
            print(line)
            time.sleep(1)

    