"""
실질적인 게임의 최상위 제어 흐름을 담당하는 파일입니다.
이상적으로는, 유저 입력은 숫자 패드만으로도 가능하도록 합니다.
이를 위해 유저 입력은 하나의 숫자(반드시 한 자리 숫자일 필요는 없음)를 문자열로서 대조하는 방식으로 처리합니다.
"""
from behavior.behavior import Behavior
from player.player import Player
from factory.command_factory import CommandFactory
from dungeon import Dungeon
import utils
from type_definitions import DungeonType, ItemDict

class Game:
    """
    main.py에서 단 한 번 생성되어 게임의 모든 정보를 포함하는 클래스입니다.
    """
    def __init__(self):
        """
        게임의 하위 객체들을 생성합니다.
        """
        self.player:Player = Player(name="Hero",
                                    health=100,
                                    attack_power=50,
                                    defense_power=50,
                                   exp=0,
                                   mp=100,
                                   max_mp=100,
                                   speed=100,
                                   behavior_list=[])
        self.enemy:dict = utils.load_json("json/enemys.json")
        self.boss:dict = utils.read_all_json("json/boss")
        self.ally:dict = utils.read_all_json("json/ally")
        self.item_list:ItemDict = utils.load_item_dict("json/items.json")
        self.commands:dict = CommandFactory.create_commands()
        self.dungeon:Dungeon = Dungeon()
        self.turn:int = 0
        self.debug:bool = False

    def toggle_debug(self):
        self.debug = not self.debug
        print(f"Debug mode {'enabled' if self.debug else 'disabled'}")

    def debug_command(self, command:str):
        if not self.debug:
            return
            
        args = command.split()
        if args[0] == "floor":
            self.dungeon.current_floor = int(args[1])
            print(f"Moved to floor {args[1]}")
        elif args[0] == "hp":
            self.player.stats.health = int(args[1])
            print(f"Set HP to {args[1]}")
        elif args[0] == "mp":
            self.player.stats.mp = int(args[1])
            print(f"Set MP to {args[1]}")
        elif args[0] == "atk":
            self.player.stats.attack_power = int(args[1])
            print(f"Set attack power to {args[1]}")
        elif args[0] == "def":
            self.player.stats.defense_power = int(args[1])
            print(f"Set defense power to {args[1]}")
        elif args[0] == "exp":
            self.player.stats.exp = int(args[1])
            print(f"Set EXP to {args[1]}")

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
        
        while self.player.stats.health > 0:#게임 루프를 계속할 조건
            # 턴 시작 처리 
            self.process_pre_turn()
            print("현재 턴:", self.turn)
            debug_str = "[Debug Mode]" if self.debug else ""
            action = input(f"{debug_str}1.정보 2.탐험 3.종료 4.중점 5.인벤토리 6.파티 7.디버그 8.저장 9.불러오기").split(" ")
            
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
            elif action[0] == "7":
                if len(action) == 1:
                    self.toggle_debug()
                else:
                    self.debug_command(" ".join(action[1:]))
            elif action[0] == "8":
                self.player.save_game()
            elif action[0] == "9":
                self.player.load_game()
            else:
                self.commands["failsafe"].execute(self, self.dungeon)
            
            # 턴 종료 처리
            self.turn += 1
            self.process_post_turn()
        print("Game Over.")
            
    def process_pre_turn(self):
        """턴 시작 전 처리"""
        self.player.pre_turn()
        for ally in self.player.get_party().values():
            ally.pre_turn()
            
    def process_post_turn(self):
        """턴 종료 후 처리"""
        self.player.post_turn()
        
        for ally in self.player.get_party().values():
            ally.post_turn()
        