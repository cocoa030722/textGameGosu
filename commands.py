import random

class Command:
    def execute(self, game=None):
        pass

class StartCommand(Command):
    def execute(self, game=None):
        print("Game started!")

class ExploreCommand(Command):
    def execute(self, game=None):
        print("탐색중...")
        probability = 30  # 30% 확률로 이벤트 발생
        random_value = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자
        if random_value <= probability:
            print("출구 발견!")
            print("현 층수:",game.current_floor)
            game.current_floor+=1
        else:
            print("탐색 실패")
            
            

class FightCommand(Command):
    def execute(self, game=None):
        probability = 50  # 50% 확률로 이벤트 발생
        random_value = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자
        if random_value <= probability:
            print("전투 시작!")
        else:
            print("적 발견하지 못함!")
            
class QuitCommand(Command):
    def execute(self, game=None):
        print("Quitting the game...")
        exit()

