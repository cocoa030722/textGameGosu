"""
게임의 던전을 구현하는 코드입니다.
"""

from enemy.boss.boss import Boss
from enemy.enemy import Enemy
from ally.ally import Ally
import utils

import random

class Dungeon():
    """
    던전의 정보와 행동을 정의하는 클래스입니다.
    """
    def __init__(self) -> None:
        self.current_floor:int = 1
        """
        dungeon_data는 현재 문자열로 취급하는 숫자를 키값으로 쓰고 있습니다.
        숫자 대신 문자열을 키값으로 쓴 것은 비선형적 맵의 구현으로 확장하기 위한 요소입니다.
        """
        self.dungeon_data:dict = utils.load_json("json/dungeon.json")
        self.MAX_FLOOR:int = len(self.dungeon_data)

    def show_cur_floor_info(self) -> None:
        print(self.dungeon_data[str(self.current_floor)])

    def get_floor_info(self) -> dict:
        return self.dungeon_data[str(self.current_floor)]

    def get_random_element(self) -> 'Event':
        """
        Group, Name 필드를 가지는 랜덤한 이벤트를 생성해 반환합니다.
        """
        # TODO:보스층 로직 분리
        floor_data = self.dungeon_data[str(self.current_floor)]
        total_events = len(floor_data["enemy"]) + len(floor_data["item"])
        if "boss" in floor_data:
            if len(floor_data["boss"]) > 0:
                return Event("boss", floor_data["boss"].pop())
            else:
                return Event("passage", "passage")
        
        total_event_group = [key for key in floor_data if len(floor_data[key]) > 0]
                
        # 전체 이벤트 + passage(1)에 대한 랜덤 선택
        passage_rand = random.randint(1, total_events + 1)
        
        if passage_rand == total_events + 1:
            return Event("passage", "passage")
            
        event_group = random.choice(total_event_group)
        event_name = random.choice(floor_data[event_group])
        event_name = floor_data[event_group].pop(floor_data[event_group].index(event_name))
        event = Event(event_group, event_name)
        return event
        
    def is_here_boss_floor(self) -> bool:
        return "boss" in self.dungeon_data[str(self.current_floor)]

    
    def next_floor(self) -> None:
        """
        현 층이 최대 층이 아닐 시 한 층을 올라갑니다.
        """
        self.current_floor+=1 
        if self.current_floor >=  self.MAX_FLOOR:
            self.current_floor=self.MAX_FLOOR

    def make_boss(self, data):
        return Boss(
                name=data["name"],
                health=data["health"],
                attack_power=data["attack_power"],
                defense_power=data["defense_power"],
                script=data["script"]
        )
        
    
    def make_enemy(self, data):
        return Enemy(
                name=data["name"],
                health=data["health"],
                attack_power=data["attack_power"],
                defense_power=data["defense_power"],
            behavior_list=data["behavior"]
        )

    def make_ally(self, data):
        return Ally(
                name=data["name"],
                health=data["health"],
                attack_power=data["attack_power"],
                defense_power=data["defense_power"],
            resistance=data["resistance"],
            compliance=data["compliance"],
            script=data["script"]
        )
        
class Event:
    """
    게임 내 이벤트 정보를 담은 클래스입니다.
    현재는 문자열열만을 포함하지만, 더 확장할 수도 있습니다.
    """
    def __init__(self, group:str, name:str):
        self.group:str = group
        self.name:str = name
