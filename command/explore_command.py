
from command import Command
from rich.prompt import Prompt

from typing import TYPE_CHECKING
if TYPE_CHECKING:# 타입 검사 시에만 import
    from game import Game
    from dungeon import Dungeon
    from player import Player

class ExploreCommand(Command):
    def __init__(self) -> None:
        self.sub_commands = {
            "fight": ExploreFightCommand(),
            "boss_fight": ExploreBossFightCommand(),
            "pick": ExplorePickCommand(),
        }

    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        print("탐색중...")
        event = dungeon.get_random_element()
        
        if event.group == "passage":
            self._handle_passage_event(dungeon)
        elif event.group in ["enemy", "boss"]:
            self._handle_battle_event(game, dungeon, player, event)
        elif event.group == "item":
            self._handle_item_event(game, dungeon, player, event)

    def _handle_passage_event(self, dungeon):
        sub_input = Prompt.ask("[bold cyan]출구 발견! 다음 층으로 넘어가겠습니까?[/bold cyan]\n1.예 2.아니오")
        if sub_input == "1":
            dungeon.next_floor()
            print("현 층수:", dungeon.current_floor)

    def _handle_battle_event(self, game, dungeon, player, event):
        print(f"{'보스 ' if event.group == 'boss' else ''}전투 시작:", event.name)
        command_key = "boss_fight" if event.group == "boss" else "fight"
        self.sub_commands[command_key].execute(game, dungeon, player, enemy_name=event.name)

    def _handle_item_event(self, game, dungeon, player, event):
        print("아이템 발견:", event.name)
        sub_input = Prompt.ask("[bold cyan]인벤토리에 추가하겠습니까?[/bold cyan]\n1.예 2.아니오")
        if sub_input == "1":
            self.sub_commands["pick"].execute(game, dungeon, player)

class BattleBase(Command):
    def _pre_battle_phase(self, fighter, enemy):
        enemy.pre_turn()
        fighter.pre_turn()

    def _battle_phase(self, fighter, enemy):
        enemy.attack(fighter)
        fighter.attack(enemy)

    def _post_battle_phase(self, fighter, enemy):
        enemy.post_turn()
        fighter.post_turn()

    def _select_fighter(self, player):
        if not player.get_party():
            return player

        player.show_party()
        choice = Prompt.ask("[bold cyan]누구를 보낼까요?[/bold cyan] (0: 직접 싸우기, 1~N: 파티 멤버)")
        if choice.isdigit() and int(choice) > 0 and int(choice) <= len(player.get_party()):
            fighter = list(player.get_party().values())[int(choice)-1]
            print(f"{fighter.name}이(가) 싸움에 나섰다!")
            return fighter
        return player

    def _check_battle_result(self, player, enemy, fighter, dungeon):
        if enemy.get_health() <= 0:
            print("플레이어 승리!")
            dungeon.show_cur_floor_info()
            return True
        elif player.get_health() <= 0:
            print("플레이어 패배")
            exit()
        elif fighter != player and fighter.get_health() <= 0:
            print(f"{fighter.name}이(가) 쓰러졌다!")
            del player.get_party()[fighter.name]
            return True
        return False

class ExploreFightCommand(BattleBase):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        enemy = dungeon.make_enemy(game.enemy[kwargs["enemy_name"]])
        enemy.appear()
        enemy.show_info()
        
        fighter = self._select_fighter(player)

        while True:
            sub_input = Prompt.ask("[bold cyan]행동을 선택하세요[/bold cyan]\n1.공격 2.도망")
            if sub_input == "1":
                self._pre_battle_phase(fighter, enemy)
                self._battle_phase(fighter, enemy)
                self._post_battle_phase(fighter, enemy)
                game.turn += 1
                
                if self._check_battle_result(player, enemy, fighter, dungeon):
                    break
                enemy.show_info()
            elif sub_input == "2":
                print("무사히 도망쳤다.")
                break

class ExploreBossFightCommand(BattleBase):
    def __init__(self) -> None:
        self.sub_commands = {
            "after_boss_fight": AfterBossFightCommand(),
        }

    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        boss = dungeon.make_boss(game.boss[kwargs["enemy_name"]])
        boss.show_script("before_fight")
        boss.show_info()
        
        fighter = player  # 보스전은 플레이어만 가능

        while True:
            sub_input = Prompt.ask("[bold cyan]행동을 선택하세요[/bold cyan]\n1.공격")
            if sub_input == "1":
                self._pre_battle_phase(fighter, boss)
                self._battle_phase(fighter, boss)
                self._post_battle_phase(fighter, boss)
                
                if self._check_battle_result(player, boss, fighter, dungeon):
                    self.sub_commands["after_boss_fight"].execute(game, dungeon, player, boss=boss)
                    break
                boss.show_info()

class ExplorePickCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        item_name = kwargs.get("item_name")
        if item_name in game.item_list:
            player.add_item(game.item_list[item_name])

class AfterBossFightCommand(Command):
    def execute(self, game: "Game", dungeon: "Dungeon", player: "Player", *args, **kwargs):
        boss = kwargs["boss"]
        boss_name = boss.name
        boss.show_script("after_fight")
        
        choice = Prompt.ask("[bold cyan]최후의 일격을 가하시겠습니까, 아니면 동료로 편입시키겠습니까?[/bold cyan]\n(1.최후의 일격/2.\"동료\" 편입)")

        if choice == "1":
            print("보스를 처치했습니다!")
        elif choice == "2":
            new_ally = dungeon.make_ally(game.ally[boss_name])
            player.join_party(new_ally)
            print(f"{boss_name}이(가) 동료로 편입되었습니다!")
            print(f"저항도: {new_ally.resistance}, 순응도: {new_ally.compliance}")
        else:
            print("잘못된 선택입니다. 최후의 일격으로 간주합니다.")
