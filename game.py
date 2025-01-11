"""
실질적인 게임의 최상위 제어 흐름을 담당하는 파일입니다.
이상적으로는, 유저 입력은 숫자 패드만으로도 가능하도록 합니다.
이를 위해 유저 입력은 하나의 숫자(반드시 한 자리 숫자일 필요는 없음)를 문자열로서 대조하는 방식으로 처리합니다.
"""
from player import Player
from factory.command_factory import CommandFactory
from dungeon import Dungeon
import utils

class Game:
    """
    main.py에서 단 한 번 생성되어 게임의 모든 정보를 포함하는 클래스입니다.
    """
    def __init__(self):
        """
        게임의 하위 객체들을 생성합니다.
        """
        self.player:Player = Player(name="Hero", health=100, attack_power=50, defense_power=50)
        self.enemy:dict = utils.load_json("json/enemys.json")
        self.boss:dict = utils.read_all_json("json/boss")
        self.ally:dict = utils.read_all_json("json/ally")
        self.item_list:dict = utils.load_json("json/items.json")
        self.commands:dict = CommandFactory.create_commands()
        self.dungeon:Dungeon = Dungeon()
        
    def run(self):
        """
        게임의 최상위 로직입니다.
        모든 유저 입력은 아래와 같이
        1.입력
        2.입력값 대조
        3.해당하는 커맨드 실행
        으로 이뤄집니다.
        """
        print("게임 시작!")
        
        while self.player.health > 0:#게임 루프를 계속할 조건
            action = input("1.정보 2.탐험 3.종료 4.중점 5.인벤토리 6.파티").split(" ")
            
            if action[0] == "1":
                self.commands["info"].execute(self, self.dungeon, self.player)
            elif action[0] == "2":
                self.commands["explore"].execute(self, self.dungeon, self.player)
            elif action[0] == "3":
                self.commands["quit"].execute(self, self.dungeon, self.player)
            elif action[0] == "4":
                self.commands["focus"].execute(self, self.dungeon, self.player)
            elif action[0] == "5":
                self.commands["inven"].execute(self, self.dungeon, self.player)
            elif action[0] == "6":
                self.commands["party"].execute(self, self.dungeon, self.player)
            else:
                print("정의되지 않은 커맨드")
        print("Game Over.")