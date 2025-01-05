import random
import copy 

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
            "pick":ExplorePickCommand(),
        }
    def execute(self, game, dungeon, player):
        print("탐색중...")
        event = dungeon.get_random_element()
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
        elif event.group == "item":
            print("아이템 발견:", event.name)

class ExploreFightCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        enemy = game.enemy[kwargs["enemy_name"]]
        while player.health > 0 and enemy.health > 0:
            sub_input = input("1.공격 2.도망")
            if sub_input == "1":
                print(player.attack)
                print(player.attack_power)
                
                
                player.attack(enemy)
                enemy.attack(player)
            elif sub_input == "2":
                break
            else:
                print("미정의 입력")
                

class ExplorePickCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        item_name = kwargs.get("item_name")
        if item_name == "health_potion":
            player.add_item(HealthPotion())
        elif item_name == "sword":
            player.add_item(Weapon("Steel Sword", 10))

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

