from entity import Entity
from behavior.map import behavior_map
class Enemy(Entity):
    """
    게임 내 모든 적의 원형이 되는 클래스입니다.
    게임의 로직은 json 정보를 기반으로 이 클래스의 인스턴스를 직접 생성합니다.
    """
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int, behavior_list:list):
        super().__init__(name, health, attack_power, defense_power)
        self.behaviors:dict = {}
        for behavior in behavior_list:
            self.add_behavior(behavior, behavior_map[behavior])
            
    def attack(self, target:Entity):
        self.perform_behavior("common_attack", target=target)

    def add_behavior(self, name, behavior):
        self.behaviors[name] = behavior

    def perform_behavior(self, name, **kwargs):
        if name in self.behaviors:
            result = self.behaviors[name].execute(self)
            print(result)
            
            # Handle attack specific behavior
            if name == "common_attack" and "target" in kwargs:
                kwargs["target"].take_damage(self.attack_power)
            
            return result
        else:
            message = f"{self.name} doesn't know how to perform {name}."
            print(message)
            return message
