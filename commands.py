import random

class Command:
    def execute(self, game, dungeon, player):
        pass

class StartCommand(Command):
    def execute(self, game, dungeon, player):
        dungeon.cur_floor_info()

class ExploreCommand(Command):
    def execute(self, game, dungeon, player):
        print("탐색중...")
        probability = 30  # 30% 확률로 이벤트 발생
        random_value = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자
        if random_value <= probability:
            print("출구 발견!")
            print("현 층수:",dungeon.current_floor)
            dungeon.next_floor()
        else:
            print("탐색 실패")
            
class FightCommand(Command):
    def execute(self, game, dungeon, player):
        probability = 50  # 50% 확률로 이벤트 발생
        random_value = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자
        if random_value <= probability:
            print("전투 시작!")
        else:
            print("적 발견하지 못함!")

class FocusCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "check":FocusCheckCommand(),
            "pick":FocusPickCommand(),
        }

    def execute(self, game, dungeon, player, *args):
        sub_command = input("1.체크 2.픽")
        if sub_command == "1":
            self.sub_commands["check"].execute(game, dungeon, player, *args[1:])
        elif sub_command == "2":
            
            self.sub_commands["pick"].execute(game, dungeon, player, *args[1:])
        else:
            print("Invalid settings command.")

class FocusCheckCommand(Command):
    def execute(self, game, dungeon, player, *args):
        print(player.get_available_focuses())

class FocusPickCommand(Command):
    def execute(self, game, dungeon, player, *args):
        print(args[0])
        
class QuitCommand(Command):
    def execute(self, game, dungeon, player):
        print("Quitting the game...")
        exit()

