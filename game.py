from player import Player
from enemy.goblin import Goblin
from command_factory import CommandFactory
from dungeon import Dungeon

class Game:
    def __init__(self):
        
        self.player = Player("Hero", 100)
        self.enemy = Goblin("Goblin", 30)
        self.commands = CommandFactory.create_commands()
        self.dungeon = Dungeon()
        
    def run(self):
        print("게임 시작!")
        
        while self.player.health > 0:#게임 루프를 계속할 조건
            action = input("1.정보 2.탐험 3.싸움 4.종료 5.중점").split(" ")
            
            if action[0] == "1":
                self.commands["start"].execute(self, self.dungeon, self.player)
            elif action[0] == "2":
                self.commands["explore"].execute(self, self.dungeon, self.player)
            elif action[0] == "3":
                self.commands["fight"].execute(self, self.dungeon, self.player)
            elif action[0] == "4":
                self.commands["quit"].execute(self, self.dungeon, self.player)
            elif action[0] == "5":
                self.commands["focus"].execute(self, self.dungeon, self.player)
            else:
                print("정의되지 않은 커맨드")
        print("Game Over.")