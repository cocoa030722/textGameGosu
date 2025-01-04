import random

class Command:
    def execute(self, game, dungeon, player):
        pass

class InfoCommand(Command):
    def execute(self, game, dungeon, player):
        dungeon.show_cur_floor_info()

class ExploreCommand(Command):
    def execute(self, game, dungeon, player):
        print("탐색중...")
        event = dungeon.get_random_element()
        print(event)
        
        if event == "passage":
            print("출구 발견!")
            sub_command = input("다음 층으로 넘어가겠습니까?\n1.예 2.아니오")
            if sub_command == "1":
                dungeon.next_floor()
                print("현 층수:",dungeon.current_floor)
            elif sub_command == "2":
                pass
            else:
                print("미정의 입력")
        else:
            print("탐색 실패")

class FocusCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "check":FocusCheckCommand(),
            "pick":FocusPickCommand(),
        }

    def execute(self, game, dungeon, player, *args):
        sub_command = input("1.체크 2.픽")
        if sub_command == "1":
            self.sub_commands["check"].execute(game, dungeon, player)
        elif sub_command == "2":
            
            self.sub_commands["pick"].execute(game, dungeon, player)
        else:
            print("Invalid settings command.")

class FocusCheckCommand(Command):
    def execute(self, game, dungeon, player, *args):
        print(player.get_available_focuses())

class FocusPickCommand(Command):
    def execute(self, game, dungeon, player, *args):
        focus_node = input(player.get_available_focuses())
        print(player.focus_tree["focus_tree"][focus_node])
        
class QuitCommand(Command):
    def execute(self, game, dungeon, player):
        print("Quitting the game...")
        exit()

