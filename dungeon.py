import copy
import random

class Dungeon():
    def __init__(self) -> None:
        self.current_floor = 1
        self.dungeon_data = {
            1:{
                "enemy":["goblin"],
                "item":["bread"]
            },
            2:{
                "enemy":["goblin"],
                "item":["bread"]
            },
            3:{
                "enemy":[],
                "item":[],
                "boss":["alchemist"],
            },
        }
        self.MAX_FLOOR = len(self.dungeon_data)

    def show_cur_floor_info(self):
        print(self.dungeon_data[self.current_floor])

    def get_floor_info(self):
        return self.dungeon_data[self.current_floor]

    def get_random_element(self) -> 'Event':
        floor_data = self.dungeon_data[self.current_floor]
        total_events = len(floor_data["enemy"]) + len(floor_data["item"])
        if "boss" in floor_data:
            return Event("boss", floor_data["boss"])
        
        total_event_group = [key for key in floor_data if len(floor_data[key]) > 0]
                
        # 전체 이벤트 + passage(1)에 대한 랜덤 선택
        passage_rand = random.randint(1, total_events + 1)
        
        if passage_rand == total_events + 1:
            return Event("passage", "passage")
            
        event_group = random.choice(total_event_group)
        event_name = random.choice(floor_data[event_group])
        event = Event(event_group, event_name)
        return event
        
    def is_here_boss_floor(self):
        return "boss" in self.dungeon_data[self.current_floor]

    
    def next_floor(self):
        self.current_floor+=1 
        if self.current_floor >=  self.MAX_FLOOR:
            self.current_floor=self.MAX_FLOOR

class Event:
    def __init__(self, group, name):
        self.group = group
        self.name = name
