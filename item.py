
"""
게임에서의 아이템을 구현하는 코드입니다.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:# 타입 검사 시에만 import
    from player import Player

class Item():
    """
    아이템의 정보와 행동을 저장하는 클래스입니다.
    각 아이템을 개별적인 클래스로 구현하는 것이 아닌, Item 클래스의 정보만을 달리하여 각각의 아이템을 구현합니다.
    """
    def __init__(self, name:str, description:str, **item_data):
        self.name:str = name
        self.description:str = description
        self.type = item_data.get("type", "other")
        self.heal_amount = item_data.get("heal_amount", 0)
        self.attack_bonus = item_data.get("attack_bonus", 0)
        self.reduce_resistance = item_data.get("reduce_resistance", 0)
        
    def use(self, player: Player):
        """
        아이템 타입에 따라 다른 효과를 적용합니다.
        """
        if self.type in ["bread", "health_potion"]:
            player.stats.health += self.heal_amount
            print(f"{self.name}을(를) 사용하여 체력이 {self.heal_amount} 회복되었습니다!")
            
        elif self.type == "weapon":
            player.stats.attack_power += self.attack_bonus
            print(f"{self.name}을(를) 장착하여 공격력이 {self.attack_bonus} 증가했습니다!")
            
        elif self.type == "party":
            for ally in player.get_party().values():
                ally.resistance -= self.reduce_resistance
            print(f"{self.name}을(를) 사용하여 파티원들의 저항이 {self.reduce_resistance} 감소했습니다!")

        else:
            print(f"{self.name}은(는) 특별한 효과가 없습니다.")

"""
elif "reduce_resistance" in self.__dict__:
"""
