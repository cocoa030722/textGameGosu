"""
최고 수준의 추상화를 담당하는 부분
세부 로직은 가급적 하위 단위로 옮길 것
"""
from rich.console import Console
from rich.prompt import Prompt

console = Console()

class Command:
    def execute(self, game, dungeon, player):
        pass

class InfoCommand(Command):
    def execute(self, game, dungeon, player):
        dungeon.show_cur_floor_info()
        player.show_info()
        
class QuitCommand(Command):
    def execute(self, game, dungeon, player):
        print("Quitting the game...")
        exit()