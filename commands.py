import random

class Command:
    def execute(self, *args, **kwargs):
        pass

class StartCommand(Command):
    def execute(self, *args, **kwargs):
        print("Game started!")

class ExploreCommand(Command):
    def execute(self, *args, **kwargs):
        print("Exploring the area...")

class FightCommand(Command):
    def execute(self, *args, **kwargs):
        probability = 1  # 80% 확률로 이벤트 발생
        random_value = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자
        if random_value <= probability:
                print("Entering a fight!")
        else:
            print("출구 발견!")
            if "game" in kwargs:
                print("현 층수:",kwargs["game"].current_floor)
                kwargs["game"].current_floor+=1

class QuitCommand(Command):
    def execute(self, *args, **kwargs):
        print("Quitting the game...")
        exit()

