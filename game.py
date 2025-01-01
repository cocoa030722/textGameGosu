from player import Player
from npc.goblin import Goblin
import commands
import utils

class Game:
    def __init__(self):
        focus_tree = utils.load_json("focus_tree.json")
        self.player = Player("Hero", 100, focus_tree)
        self.enemy = Goblin("Goblin", 30)
        self.commands = {
            "start": commands.StartCommand(),
            "explore": commands.ExploreCommand(),
            "fight": commands.FightCommand(),
            "quit": commands.QuitCommand()
        }
        self.current_floor = 1

    def run(self):
        print("게임 시작!")
        
        while self.player.health > 0:#게임 루프를 계속할 조건
            action = int(input("1.시작 2.탐험 3.싸움 4.종료"))
            if action == 1:
                self.commands["start"].execute()
            elif action == 2:
                self.commands["explore"].execute()
            elif action == 3:
                self.commands["fight"].execute(game=self)
            elif action == 4:
                self.commands["quit"].execute()
            else:
                print("정의되지 않은 커맨드")
        print("Game Over.")