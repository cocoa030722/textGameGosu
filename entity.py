
from condition import Condition
from stats import Stats
from behavior.map import behavior_map

import random

class Entity:
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int, exp:int, mp:int, max_mp:int, speed:int, behavior_list:list):
        self.name:str = name
        self.stats = Stats(health, attack_power, defense_power, exp, mp, max_mp, speed)
        self.condition:Condition = Condition.NORMAL
        self.attack_probability = 100
        self.behaviors:dict = {}
        
        for behavior in behavior_list:
            self.add_behavior(behavior, behavior_map[behavior])

    def get_health(self) -> int:
        return self.stats.health

    def get_attack_power(self) -> int:
        return self.stats.attack_power

    def get_defense_power(self) -> int:
        return self.stats.defense_power

    def get_exp(self) -> int:
        return self.stats.exp

    def get_mp(self)->int:
        return self.stats.mp

    def get_max_mp(self)->int:
        return self.stats.max_mp
        
    def gain_exp(self, amount:int) -> None:
        self.stats.exp += amount
        
    def take_damage(self, attack_power:int) -> None:
        damage = (attack_power - self.stats.defense_power) if (attack_power - self.get_defense_power()) > 0 else 0
        self.stats.health = self.stats.health - damage

    def heal(self, amount:int) -> None:
        self.stats.health = self.stats.health + amount

    def attack(self, target:"Entity"):
        prob = random.randint(0, 100)
        print("공격 확률:", prob, self.attack_probability)
        
        if prob <= self.attack_probability:
            print(f"{self.name} attacks {target.name}!")
            target.take_damage(self.stats.attack_power)
        else:
            print("공격 실패!")
            
    def appear(self) -> None:
        print(f"{self.name} 등장")

    def show_info(self) -> None:
        print(f"이름:{self.name}")
        for field, value in self.stats.__dict__.items():
            print(f"{field}: {value}")

    def add_behavior(self, name, behavior):
        self.behaviors[name] = behavior

    def perform_behavior(self, name, **kwargs):
        if name in self.behaviors:
            result_dict = self.behaviors[name].execute(self, kwargs["target"])
            print(result_dict)
            
            # TODO:특수 케이스의 보편화
            if "target" in kwargs:
                kwargs["target"].take_damage(self.get_attack_power())
                if "status" in result_dict:
                    kwargs["target"].status=result_dict["status"]

            return result_dict["result"]
        else:
            message = f"{self.name} doesn't know how to perform {name}."
            print(message)
            return message
            
    def pre_turn(self):
        if self.condition == Condition.PARALYSIS:
            self.attack_probability = 10
        else:
            self.attack_probability = 100
        self.stats.mp = self.stats.mp + 10
        
    def post_turn(self):
        if self.condition == Condition.POISON:
            self.take_damage(5)
