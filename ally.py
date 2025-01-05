from entity import Entity
import time

class Ally(Entity):
    def __init__(self, name, health, attack_power, defense_power, resistance, compliance):
        super().__init__(name, health, attack_power, defense_power)
        self.resistance = resistance  # 저항도 (높을수록 반항적)
        self.compliance = compliance  # 순응도 (높을수록 협조적)
        self.script = {
            "reduce_resistance":["저항 감소 대사 1", "저항 감소 대사 2"],
            "increase_compliance":["순응 증가 대사 1", "순응 증가 대사 2"]
        }
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

    
    def take_damage(self, attack_power):
        super().take_damage(attack_power)

    def reduce_resistance(self):
        for line in self.script["reduce_resistance"]:
            print(line)
            time.sleep(1)
        self.resistance -= 10
        print(f"{self.name} 저항도가 {10} 감소했다.")

    def increase_compliance(self):
        for line in self.script["increase_compliance"]:
            print(line)
            time.sleep(1)
        self.compliance -= 10
        print(f"{self.name} 순응도가 {10} 증가했다.")

    