"""
최고 수준의 추상화를 담당하는 부분
세부 로직은 가급적 하위 단위로 옮길 것
"""

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
            "boss_fight":ExploreBossFightCommand(),
            "pick":ExplorePickCommand(),
        }
    def execute(self, game, dungeon, player):
        print("탐색중...")
        event = dungeon.get_random_element()
        if event.group == "passage":
            sub_input = input("출구 발견! 다음 층으로 넘어가겠습니까?\n1.예 2.아니오")
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
            sub_input = input("인벤토리에 추가하겠습니까?\n1.예 2.아니오")
            if sub_input == "1":
                self.sub_commands["pick"].execute(game, dungeon, player,  item_name=event.name)
            elif sub_input == "2":
                pass
            else:
                print("미정의 입력('아니오'로 간주됨)")

class ExploreFightCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        enemy = dungeon.make_enemy(game.enemy[kwargs["enemy_name"]])
        #enemy = copy.deepcopy(game.enemy[kwargs["enemy_name"]])
        enemy.appear()
        enemy.show_info()
        
        fighter = player
        if player.party:
            player.show_party()
            choice = input("누구를 보낼까요? (0: 직접 싸우기, 1~N: 파티 멤버): ")
            if choice.isdigit() and int(choice) > 0 and int(choice) <= len(player.party):
                fighter = list(player.party.values())[int(choice)-1]
                print(f"{fighter.name}이(가) 싸움에 나섰다!")

        while fighter.health > 0 and enemy.health > 0:
            sub_input = input("1.공격 2.도망")
            if sub_input == "1":
                fighter.attack(enemy)
                enemy.attack(fighter)
                if fighter != player and fighter.health <= 0:
                    print(f"{fighter.name}이(가) 쓰러졌다!")
                    del player.party[fighter.name]
                    return
            elif sub_input == "2":
                print("무사히 도망쳤다.")
                return
            else:
                print("미정의 입력")
            enemy.show_info()
        if enemy.health <= 0:
            print("플레이어 승리!")
            dungeon.show_cur_floor_info()
        elif player.health <= 0:
            print("플레이어 패배")
            exit()

class ExploreBossFightCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "after_boss_fight":AfterBossFightCommand(),
        }
    def execute(self, game, dungeon, player, *args, **kwargs):
        boss = dungeon.make_boss(game.boss[kwargs["enemy_name"]])
        #boss = copy.deepcopy(game.boss[kwargs["enemy_name"]])
        boss.show_script("before_fight")
        boss.show_info()
        
        while player.health > 0 and boss.health > 0:
            sub_input = input("1.공격") # 퇴각 불가
            if sub_input == "1":
                player.attack(boss)
                boss.attack(player)
            else:
                print("미정의 입력")
            boss.show_info()
            
        if boss.health <= 0:
            print("플레이어 승리!")
            dungeon.show_cur_floor_info()
            self.sub_commands["after_boss_fight"].execute(game, dungeon, player,  boss=boss)
        elif player.health <= 0:
            print("플레이어 패배")
            exit()

class AfterBossFightCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        boss = kwargs["boss"]
        boss_name = boss.name
        boss.show_script("after_fight")
        
        print("보스를 물리쳤습니다!")
        choice = input("최후의 일격을 가하시겠습니까, 아니면 동료로 편입시키겠습니까?\n(1.최후의 일격/2.\"동료\" 편입): ").strip()

        if choice == "1":
            print("보스를 처치했습니다!")
        elif choice == "2":
            new_ally = dungeon.make_ally(game.ally[boss_name])
            # new_ally = copy.deepcopy(game.ally[boss_name])
            player.join_party(new_ally)
            print(f"{boss_name}이(가) 동료로 편입되었습니다!")
            print(f"저항도: {new_ally.resistance}, 순응도: {new_ally.compliance}")
        else:
            print("잘못된 선택입니다. 최후의 일격으로 간주합니다.")
        
class ExplorePickCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        item_name = kwargs.get("item_name")
        if item_name in game.item_list:
            player.add_item(game.item_list[item_name])#딕셔너리 정보를 전달하여, 아이템 생성과 추가를 플레이어가 하게 함

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
            print("유효하지 않은 커맨드입니다.")

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

class InventoryCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "show":InventoryShowCommand(),
            "use":InventoryUseCommand(),
        }
        
    def execute(self, game, dungeon, player):
        sub_command = input("1.인벤토리 확인 2.아이템 사용")
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
        index = input("사용할 아이템의 인덱스:")
        player.use_item(int(index))

class PartyCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "show":PartyShowCommand(),
            "control":PartyControlCommand(),
        }
        
    def execute(self, game, dungeon, player):
        sub_command = input("1.파티 확인 2.파티 멤버 \"관리\"")
        if sub_command == "1":
            self.sub_commands["show"].execute(game, dungeon, player)
        elif sub_command == "2":
            
            self.sub_commands["control"].execute(game, dungeon, player)
        else:
            print("유효하지 않은 커맨드입니다.")

class PartyShowCommand(Command):
    def execute(self, game, dungeon, player):
        player.show_party()

class PartyControlCommand(Command):
    def execute(self, game, dungeon, player):
        player.show_party()
        
        ally_name = input("동료 이름 입력:")
        player.call_party_member(ally_name).reduce_resistance()
        player.call_party_member(ally_name).increase_compliance()