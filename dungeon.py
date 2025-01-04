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
        print(self.dungeon_data[self.current_floor])
        event_group = random.choice(list(self.dungeon_data[self.current_floor].keys()))
        event = random.choice(self.dungeon_data[self.current_floor][event_group])
        return event
        
    def is_here_boss_floor(self):
        return "boss" in self.dungeon_data[self.current_floor]

    
    def next_floor(self):
        self.current_floor+=1 
        if self.current_floor <=  3:
            self.current_floor=3