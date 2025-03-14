from command import Command
from rich.prompt import Prompt

from typing import TYPE_CHECKING
if TYPE_CHECKING:# 타입 검사 시에만 import
    from game import Game
    from dungeon import Dungeon
    from player import Player

class PartyCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "show":PartyShowCommand(),
            "control":PartyControlCommand(),
        }
        
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        sub_command = Prompt.ask("[bold cyan]선택해주세요[/bold cyan]\n1.파티 확인 2.파티 멤버 \"관리\"")
        if sub_command == "1":
            self.sub_commands["show"].execute(game, dungeon, player)
        elif sub_command == "2":
            self.sub_commands["control"].execute(game, dungeon, player)
        else:
            print("유효하지 않은 커맨드입니다.")

class PartyShowCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        player.show_party()

class PartyControlCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        player.show_party()
        
        sub_command = Prompt.ask("[bold cyan]선택해주세요[/bold cyan]\n1.수동 제어 2.자동 제어 설정 3.direct rule_")
        
        if sub_command == "1":
            ally_name = Prompt.ask("[bold cyan]동료 이름을 입력하세요[/bold cyan]")
            player.call_party_member(ally_name).reduce_resistance(10)
            player.call_party_member(ally_name).increase_compliance(10)
        elif sub_command == "2":
            player.toggle_passive_control()
            print(f"현재 MP: {player.get_mp()}")
        elif sub_command == "3":
            player.direct_rule()
            print(f"현재 MP: {player.get_mp()}")
        else:
            print("잘못된 입력입니다.")