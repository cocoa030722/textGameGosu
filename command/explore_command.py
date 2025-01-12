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
            sub_input = Prompt.ask("[bold cyan]출구 발견! 다음 층으로 넘어가겠습니까?[/bold cyan]\n1.예 2.아니오")
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
            sub_input = Prompt.ask("[bold cyan]인벤토리에 추가하겠습니까?[/bold cyan]\n1.예 2.아니오")
            if sub_input == "1":
                self.sub_commands["pick"].execute(game, dungeon, player,  item_name=event.name)
            elif sub_input == "2":
                pass
            else:
                print("미정의 입력('아니오'로 간주됨)")

class ExploreFightCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        enemy = dungeon.make_enemy(game.enemy[kwargs["enemy_name"]])
        enemy.appear()
        enemy.show_info()
        
        fighter = player
        if player.party:
            player.show_party()
            choice = Prompt.ask("[bold cyan]누구를 보낼까요?[/bold cyan] (0: 직접 싸우기, 1~N: 파티 멤버)")
            if choice.isdigit() and int(choice) > 0 and int(choice) <= len(player.party):
                fighter = list(player.party.values())[int(choice)-1]
                print(f"{fighter.name}이(가) 싸움에 나섰다!")

        while fighter.health > 0 and enemy.health > 0:
            sub_input = Prompt.ask("[bold cyan]행동을 선택하세요[/bold cyan]\n1.공격 2.도망")
            if sub_input == "1":
                """
                공격 전 로직
                """
                enemy.pre_turn()
                fighter.pre_turn()
                enemy.attack(fighter)
                fighter.attack(enemy)
                """
                공격 후 로직
                """
                enemy.post_turn()
                fighter.post_turn()
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
        boss.show_script("before_fight")
        boss.show_info()
        
        while player.health > 0 and boss.health > 0:
            sub_input = Prompt.ask("[bold cyan]행동을 선택하세요[/bold cyan]\n1.공격") # 퇴각 불가
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
        
class ExplorePickCommand(Command):
    def execute(self, game, dungeon, player, *args, **kwargs):
        item_name = kwargs.get("item_name")
        if item_name in game.item_list:
            player.add_item(game.item_list[item_name])

