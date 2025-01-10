from entity import Entity
from rich.tree import Tree
from rich.console import Console

import utils
from item import Item

class Player(Entity):
    def __init__(self, name, health, attack_power, defense_power):
        super().__init__(name, health, attack_power, defense_power)
        self.inventory = []
        self.max_inventory = 10
        
        self.focus_tree = utils.load_json("json/focus_tree.json")
        self.focus_dict = {focus["id"]: focus for focus in self.focus_tree["focus_tree"]}
        
        self.completed_focuses = []
        self.party = {}
        
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)
        
    def take_damage(self, attack_power):
        super().take_damage(attack_power)

    def appear(self):
        super().appear()

    def show_info(self):
        super().show_info()
        
    def see_focus_tree(self):
        print(self.focus_tree)
        
    def check_prerequisites(self, completed_focuses):
        """포커스의 선행 조건 확인"""
        return all(prerequisite in completed_focuses for prerequisite in self.focus_tree["prerequisites"])

    def get_available_focuses(self):
        """Returns list of available focus names that can be chosen"""
        available = []
        for focus in self.focus_tree["focus_tree"]:
                if focus["id"] not in self.completed_focuses and all(prereq in self.completed_focuses for prereq in focus["prerequisites"]):
                    available.append(focus["id"])
        self.render_focus_tree(self.focus_tree, self.completed_focuses)
        return available

    def render_focus_tree(self, focus_tree, completed_focuses):
        """포커스 트리를 Rich Tree로 렌더링"""
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
        

    def add_item(self, item_data):
        if len(self.inventory) < self.max_inventory:
            #일단 아이템의 보편성 구현을 우선하고, 사용 기능을 일시적으로 삭제함
            item = Item(
                item_data["name"],
                item_data["description"]
                
            )
            self.inventory.append(item)
            print(f"{item.name}  발견! 인벤토리에 추가했다.")
        else:
            print("인벤토리 가득 참!")
        
    def use_item(self, index):
        if 0 <= index < len(self.inventory):
            item = self.inventory.pop(index)
            item.use(self)
        else:
            print("Invalid item index!")
            
    def show_inventory(self):
        if not self.inventory:
            print("Inventory is empty!")
            return
        print("\n=== Inventory ===")
        for i, item in enumerate(self.inventory):
            print(f"{i}. {item.name}: {item.description}")
            
    def complete_focus(self, focus):
        """포커스를 완료하고 효과 적용"""
        print(f"\n=== Focus Completed: {focus['name']} ===")
        print(focus["description"])
        
        # 포커스 효과 적용
        
        
        # 포커스를 완료 리스트에 추가
        self.completed_focuses.append(focus["id"])
        print("Focus effect applied!")
        
    def join_party(self, ally):
        self.party[ally.name] = ally

    def show_party(self):
        print("\n=== 파티 멤버 ===")
        for i, ally in enumerate(self.party):
            print(f"{i}. {self.party[ally].name}/저항도:{self.party[ally].resistance}, 순응도:{self.party[ally].compliance}")
            
    def call_party_member(self, ally_name):
        return self.party[ally_name]

    