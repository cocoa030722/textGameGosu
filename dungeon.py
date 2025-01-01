class Dungeon():
    def __init__(self) -> None:
        self.current_floor = 1
        self.dungeon_data = {
            1:{
                "enemy":["goblin"],
                "goods":["bread"]
            },
            2:{
                "enemy":["goblin"],
                "goods":["bread"]
            },
            3:{
                "enemy":["goblin"],
                "goods":["bread"],
                "boss":"alchemist",
            },
        }

    def cur_floor_info(self):
        print(self.dungeon_data[self.current_floor])
        
    def next_floor(self):
        self.current_floor+=1