from command.command import Command
from rich.prompt import Prompt

class InventoryCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "show":InventoryShowCommand(),
            "use":InventoryUseCommand(),
        }
        
    def execute(self, game, dungeon, player):
        sub_command = Prompt.ask("[bold cyan]선택해주세요[/bold cyan]\n1.인벤토리 확인 2.아이템 사용")
        if sub_command == "1":
            self.sub_commands["show"].execute(game, dungeon, player)
        elif sub_command == "2":
            self.sub_commands["use"].execute(game, dungeon, player)
        else:
            print("유효하지 않은 커맨드입니다.")

class InventoryShowCommand(Command):
    def execute(self, game, dungeon, player):
        player.show_inventory()

class InventoryUseCommand(Command):
    def execute(self, game, dungeon, player):
        player.show_inventory()
        index = Prompt.ask("[bold cyan]사용할 아이템의 인덱스를 입력하세요[/bold cyan]")
        player.use_item(int(index))
