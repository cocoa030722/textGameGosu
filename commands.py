import random
import copy 
import item

"""
최고 수준의 추상화를 담당하는 부분
세부 로직은 가급적 하위 단위로 옮길 것
"""

class Command:
    def execute(self, game, dungeon, player):
        pass

class InfoCommand(Command):
    def execute(self, game, dungeon, player):
        dungeon.show_cur_floor_info()

class ExploreCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "fight":ExploreFightCommand(),
            "boss_fight":ExploreBossFightCommand(),
            "pick":ExplorePickCommand(),
        }
    def execute(self, game, dungeon, player):
        print("탐색중...")
        event = dungeon.get_random_element()
        print(event.group, event.name)
        if event.group == "passage":
            print("출구 발견!")
            sub_input = input("다음 층으로 넘어가겠습니까?\n1.예 2.아니오")
            if sub_input == "1":
                dungeon.next_floor()
                print("현 층수:",dungeon.current_floor)
            elif sub_input == "2":
                pass
            else:
                print("미정의 입력('아니오'로 간주됨)")
        elif event.group == "enemy":
            print("전투 시작:", event.name)
            self.sub_commands["fight"].execute(game, dungeon, player,  enemy_name=event.name)
        elif event.group == "boss":
            print("보스 전투 시작:", event.name)
            self.sub_commands["boss_fight"].execute(game, dungeon, player,  enemy_name=event.name)
        elif event.group == "item":
            print("아이템 발견:", event.name)

class ExploreFightCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        enemy = copy.deepcopy(game.enemy[kwargs["enemy_name"]])
        enemy.appear()
        enemy.show_info()
        while player.health > 0 and enemy.health > 0:
            sub_input = input("1.공격 2.도망")
            if sub_input == "1":
                player.attack(enemy)
                enemy.attack(player)
            elif sub_input == "2":
                print("무사히 도망쳤다.")
                return
            else:
                print("미정의 입력")
            enemy.show_info()
        if enemy.health <= 0:
            print("플레이어 승리!")
            info = dungeon.get_floor_info()
            info["enemy"].remove(enemy.name)
            dungeon.show_cur_floor_info()
        elif player.health <= 0:
            print("플레이어 패배")
            exit()

class ExploreBossFightCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        enemy = copy.deepcopy(game.enemy[kwargs["enemy_name"]])
        enemy.appear()
        enemy.show_info()
        while player.health > 0 and enemy.health > 0:
            sub_input = input("1.공격") # 퇴각 불가
            if sub_input == "1":
                player.attack(enemy)
                enemy.attack(player)
            else:
                print("미정의 입력")
            enemy.show_info()
        if enemy.health <= 0:
            print("플레이어 승리!")
            info = dungeon.get_floor_info()
            info["boss"].remove(enemy.name)
            dungeon.show_cur_floor_info()
        elif player.health <= 0:
            print("플레이어 패배")
            exit()
        
class ExplorePickCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        item_name = kwargs.get("item_name")
        if item_name == "health_potion":
            player.add_item(item.HealthPotion())
        elif item_name == "sword":
            player.add_item(item.Weapon("Steel Sword", 10))

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
    def execute(self, game, dungeon, player, *args, **kwargs):
        print(player.get_available_focuses())

class FocusPickCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        focus_node = input(player.get_available_focuses())
        print(player.focus_tree["focus_tree"][focus_node])
        
class QuitCommand(Command):
    def execute(self, game, dungeon, player):
        print("Quitting the game...")
        exit()

