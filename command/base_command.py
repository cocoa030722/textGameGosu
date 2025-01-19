"""
최고 수준의 추상화를 담당하는 부분
세부 로직은 가급적 하위 단위로 옮길 것
"""
from rich.console import Console

from typing import TYPE_CHECKING
if TYPE_CHECKING:# 타입 검사 시에만 import
    from game import Game
    from dungeon import Dungeon
    from player import Player

console = Console()

class Command:
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        pass

class InfoCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        dungeon.show_cur_floor_info()
        player.show_info()
        
class QuitCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        print("Quitting the game...")
        exit()

class FailSafeCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        print("정의되지 않은 동작 또는 입력입니다. 입력은 무시되었습니다.")