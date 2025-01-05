from entity import Entity
from rich.tree import Tree
from rich.console import Console
import utils

class Player(Entity):
    def __init__(self, name, health, attack_power, defense_power):
        super().__init__(name, health, attack_power, defense_power)
        self.inventory = []
        self.max_inventory = 10
        
        self.focus_tree = utils.load_json("focus_tree.json")
        self.focus_dict = {focus["id"]: focus for focus in self.focus_tree["focus_tree"]}
        
        self.completed_focuses = []
        self.party = []
        
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
        

    def add_item(self, item):
        if len(self.inventory) < self.max_inventory:
            self.inventory.append(item)
            print(f"{item.name} added to inventory!")
        else:
            print("Inventory is full!")
            
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