from entity import Entity
from behavior.map import behavior_map
class Enemy(Entity):
    """
    게임 내 모든 적의 원형이 되는 클래스입니다.
    게임의 로직은 json 정보를 기반으로 이 클래스의 인스턴스를 직접 생성합니다.
    """
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int, behavior_list:list, exp:int):
        super().__init__(name, health, attack_power, defense_power, exp, mp=100, max_mp=100, speed=20)
        
            
    def attack(self, target:Entity):
        self.perform_behavior("common_attack", target=target)


