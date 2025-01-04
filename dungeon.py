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
                "boss":"alchemist",
            },
        }

    def show_cur_floor_info(self):
        print(self.dungeon_data[self.current_floor])

    def get_floor_info(self):
        return self.dungeon_data[self.current_floor]

    def get_random_element(self):
        floor_data = self.dungeon_data[self.current_floor]
        total_events = len(floor_data["enemy"]) + len(floor_data["item"])
        
        # 전체 이벤트 + passage(1)에 대한 랜덤 선택
        if random.randint(1, total_events + 1) == total_events + 1:
            return "passage"
            
        event_group = random.choice(list(floor_data.keys()))
        event = random.choice(floor_data[event_group])
        return event
        
    def is_here_boss_floor(self):
        return "boss" in self.dungeon_data[self.current_floor]

    
    def next_floor(self):
        self.current_floor+=1 
        if self.current_floor <=  3:
            self.current_floor=3