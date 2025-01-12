from command.command import Command
from rich.prompt import Prompt

class FocusCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "check":FocusCheckCommand(),
            "pick":FocusPickCommand(),
        }

    def execute(self, game, dungeon, player, *args):
        sub_command = Prompt.ask("[bold cyan]선택해주세요[/bold cyan]\n1.체크 2.픽")
        if sub_command == "1":
            self.sub_commands["check"].execute(game, dungeon, player)
        elif sub_command == "2":
            self.sub_commands["pick"].execute(game, dungeon, player)
        else:
            print("유효하지 않은 커맨드입니다.")

class FocusCheckCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        print(player.get_available_focuses())

class FocusPickCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        focus_node = Prompt.ask("[bold cyan]" + player.get_available_focuses() + "[/bold cyan]")
        print(player.focus_tree["focus_tree"][focus_node])