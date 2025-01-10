from entity import Entity

class Enemy(Entity):
    """
    게임 내 모든 적의 원형이 되는 클래스입니다.
    factory는 json 정보를 기반으로 이 클래스의 인스턴스를 직접 생성합니다.
    """
    def __init__(self, name, health, attack_power, defense_power):
        super().__init__(name, health, attack_power, defense_power)

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def take_damage(self, attack_power):
        super().take_damage(attack_power)
    def appear(self):
        super().appear()
