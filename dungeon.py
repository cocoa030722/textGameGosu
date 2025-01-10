from enemy.boss.boss import Boss
from enemy.enemy import Enemy
from ally.ally import Ally
import utils

import copy
import random

class Dungeon():
    def __init__(self) -> None:
        self.current_floor = 1
        self.dungeon_data = utils.load_json("json/dungeon.json")
        self.MAX_FLOOR = len(self.dungeon_data)

    def show_cur_floor_info(self) -> None:
        print(self.dungeon_data[str(self.current_floor)])

    def get_floor_info(self) -> dict:
        return self.dungeon_data[str(self.current_floor)]

    def get_random_element(self) -> 'Event':
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
        self.current_floor+=1 
        if self.current_floor >=  self.MAX_FLOOR:
            self.current_floor=self.MAX_FLOOR

    def make_boss(self, data):
        return Boss(
                data["name"],
                data["health"],
                data["attack_power"],
                data["defense_power"],
                data["script"]
        )
        
    
    def make_enemy(self, data):
        return Enemy(
                data["name"],
                data["health"],
                data["attack_power"],
                data["defense_power"]
        )

    def make_ally(self, data):
        return Ally(
                data["name"],
                data["health"],
                data["attack_power"],
                data["defense_power"],
            data["resistance"],
            data["compliance"],
            data["script"]
        )
        
class Event:
    def __init__(self, group, name):
        self.group = group
        self.name = name
