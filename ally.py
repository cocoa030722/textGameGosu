from entity import Entity

class Ally(Entity):
    def __init__(self, name, health, attack_power, defense_power, resistance, compliance):
        super().__init__(name, health, attack_power, defense_power)
        self.resistance = resistance  # 저항도 (높을수록 반항적)
        self.compliance = compliance  # 순응도 (높을수록 협조적)

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

    