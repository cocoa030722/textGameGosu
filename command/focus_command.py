from command import Command
from rich.prompt import Prompt

from typing import TYPE_CHECKING
if TYPE_CHECKING:# 타입 검사 시에만 import
    from game import Game
    from dungeon import Dungeon
    from player import Player

"""모든 포커스 드리 관련 기능은 후순위 구현"""
class FocusCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "check":FocusCheckCommand(),
            "pick":FocusPickCommand(),
        }

    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        sub_command = Prompt.ask("[bold cyan]선택해주세요[/bold cyan]\n1.체크 2.픽")
        if sub_command == "1":
            self.sub_commands["check"].execute(game, dungeon, player)
        elif sub_command == "2":
            self.sub_commands["pick"].execute(game, dungeon, player)
        else:
            print("유효하지 않은 커맨드입니다.")

class FocusCheckCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        print(player.get_available_focuses())

class FocusPickCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        available_list = player.get_available_focuses()
        focus_node = Prompt.ask("[bold cyan]원하는 중점의 인덱스를 선택하세요(0부터 시작)\n" + str(player.get_available_focuses()) + "[/bold cyan]")
        try: # 범위를 벗어난 입력 대응은 try-except로 처리
            player.complete_focus(available_list[int(focus_node)])
        except IndexError:
            print("유효하지 않은 입력입니다. 다시 시도하세요.")
        