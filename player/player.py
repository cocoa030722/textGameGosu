"""
게임 내 플레이어의 정보와 행동을 정의하는 코드입니다.
"""
from ally.ally import Ally
from entity import Entity
from player.inven import Inventory
from player.party import Party

import utils
from rich.console import Console
from rich.tree import Tree

class Player(Entity):
    """
    플레이어가 가지는 정보와 가능한 행동들을 담은 클래스입니다.
    """
    def __init__(self, name:str, health:int, attack_power:int, defense_power:int, exp:int, mp:int, max_mp:int, speed:int, behavior_list:list):
        super().__init__(name, health, attack_power, defense_power, exp, mp, max_mp, speed, behavior_list)
        self._inven:Inventory = Inventory()
        self._party:Party = Party()
        self.passive_control_enabled:bool = False
        
        self.level = 1
        self.level_data = utils.load_json("json/level_data.json")
        self.focus_points = 0
        __focus_tree:dict = utils.load_json("json/focus_tree.json")
        self.focus_dict:dict = {focus["id"]: focus for focus in __focus_tree["focus_tree"]}
        self.completed_focuses:list = []
        
    def get_exp_to_level_up(self):
        return self.level_data.get(str(self.level), float('inf'))

    def level_up(self):
        self.level += 1
        self.stats.attack_power += 5
        self.stats.defense_power += 3
        self.focus_points += 1
        self.heal(20)
        print(f"{self.name} 레벨 업! 레벨: {self.level}")
        print(f"공격력: {self.stats.attack_power}, 방어력: {self.stats.defense_power}, 체력: {self.stats.health}, 스킬 포인트: {self.focus_points}")

    def gain_exp(self, amount):
        self.gain_exp(amount)
        print(f"{self.name}는 {amount} 경험치를 얻었습니다! (현재 경험치: {self.stats.exp}/{self.get_exp_to_level_up()})")
        while self.stats.exp >= self.get_exp_to_level_up():
            self.stats.exp -= self.get_exp_to_level_up()
            self.level_up()
            
    def passive_magic_control(self):
        """MP를 소량 소모하여 자동으로 동료들의 저항도를 감소시키고 순응도를 증가시킵니다."""
        if self.stats.mp < 5 or not self.passive_control_enabled:
            return
            
        self.stats.mp -= 5
        for ally in self._party.get_party().values():
            ally.resistance = max(0, ally.resistance - 5)
            ally.compliance = min(100, ally.compliance + 5)
            print(f"{ally.name}의 저항도/순응도가 변화했습니다. (저항도: {ally.resistance}, 순응도: {ally.compliance})")
            
    def martial_law(self):
        """대량의 MP를 소모하여 모든 동료의 순응도를 최대치로, 저항도를 최저치로 만듭니다."""
        if self.stats.mp < 50:
            print("MP가 부족합니다!")
            return
            
        self.stats.mp -= 50
        for ally in self._party.get_party().values():
            ally.martial_law()
            print(f"{ally.name}의 저항도/순응도가 강제 조정되었습니다. (저항도: 0, 순응도: 100)")
            
    def toggle_passive_control(self):
        """자동 제어 기능을 켜고 끕니다."""
        self.passive_control_enabled = not self.passive_control_enabled
        state = "활성화" if self.passive_control_enabled else "비활성화"
        print(f"자동 제어가 {state}되었습니다.")

    """
    인벤토리, 파티 객체는 private->외부 접근 자제
    인벤토리, 파티를 다룰 때는 플레이어의 wrapper 메소드를 통한다
    """
    # inven wrapper 시작
    def add_item(self, item_data:dict):
        self._inven.add_item(item_data)
        
    def use_item(self, index:int):
        self._inven.use_item(index)
            
    def show_inventory(self):
        self._inven.show_inventory()
    # inven wrapper 끝

    # party의 wrapper 시작
    def get_party(self)->dict:
        return self._party.get_party()
        
    def join_party(self, ally:Ally):
        self._party.join_party(ally)

    def show_party(self):
        self._party.show_party()
            
    def call_party_member(self, ally_name) -> Ally:
        return self._party.call_party_member(ally_name)
    # party의 wrapper 끝

    def check_prerequisites(self, completed_focuses)->bool:
        #포커스의 선행 조건 확인
        return all(prerequisite in completed_focuses for prerequisite in self.focus_dict["prerequisites"])

    def get_available_focuses(self)->list:
        #Returns list of available focus names that can be chosen
        available = []
        for focus_name, focus_data in self.focus_dict.items():
            if focus_name not in self.completed_focuses and all(prereq in self.completed_focuses for prereq in focus_data["prerequisites"]):
                available.append(focus_data["id"])
        self.render_focus_tree(self.focus_dict, self.completed_focuses)
        return available

    def render_focus_tree(self, focus_tree, completed_focuses):
        
        #포커스 트리를 Rich Tree로 렌더링
        tree = Tree("Focus Tree")
        
        # 트리 렌더링
        def render_tree(nodes, root_id):
            def add_children(tree, node_id):
                node = nodes[node_id]
                node_label = f"{node['id']}"
                tree_node = tree.add(node_label)
                for child_id in node["children"]:
                    add_children(tree_node, child_id)
                if node["mutual_exclusion"]:
                    mutual_exclusive_label = f"[italic red]Mutual Exclusive: " + ", ".join(node["mutual_exclusion"]) + "[/italic red]"
                    tree_node.add(mutual_exclusive_label)
            root_node = Tree(f"[bold green]{root_id}[/bold green]")
            add_children(root_node, root_id)
            return root_node
        
        # 테스트 데이터 트리 렌더링
        console = Console()
        tree = render_tree(self.focus_dict, "begin_the_game")
        console.print(tree)

    def see_focus_dict(self):
        print(self.focus_dict)

    def complete_focus(self, focus_name:str):
        
        #포커스를 완료하고 효과 적용
        print(f"\n=== Focus Completed: {focus_name} ===")
        print(self.focus_dict[focus_name]["description"])
        # TODO:포커스 효과 적용
        for effect_name, effect_value in self.focus_dict[focus_name]["effect"].items():
            if effect_name == "add_behavior":
                self.behaviors[effect_name] = effect_value["behavior"]
            elif effect_name == "modify_field":
                for field, change in effect_value.items():
                    setattr(self.stats, field, getattr(self.stats, field) + change)
            elif effect_name == "set_field":
                for field, value in effect_value.items():
                    setattr(self.stats, field, value)
        
        # 포커스를 완료 리스트에 추가
        self.completed_focuses.append(self.focus_dict[focus_name]["id"])
        print("Focus effect applied!")
    
    def pre_turn(self):
        super().pre_turn()
        if self.passive_control_enabled:
            self.passive_magic_control()
    