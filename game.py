from player import Player
from enemy.goblin import Goblin
from factory.command_factory import CommandFactory
from factory.enemy_factory import EnemyFactory
from dungeon import Dungeon

class Game:
    def __init__(self):
        self.player = Player(name="Hero", health=100, attack_power=50, defense_power=50)
        self.enemy = EnemyFactory.create_enemys()
        self.commands = CommandFactory.create_commands()
        self.dungeon = Dungeon()
        
    def run(self):
        print("게임 시작!")
        
        while self.player.health > 0:#게임 루프를 계속할 조건
            action = input("1.정보 2.탐험 3.종료 4.중점").split(" ")
            
            if action[0] == "1":
                self.commands["info"].execute(self, self.dungeon, self.player)
            elif action[0] == "2":
                self.commands["explore"].execute(self, self.dungeon, self.player)
            elif action[0] == "3":
                self.commands["quit"].execute(self, self.dungeon, self.player)
            elif action[0] == "4":
                self.commands["focus"].execute(self, self.dungeon, self.player)
            else:
                print("정의되지 않은 커맨드")
        print("Game Over.")