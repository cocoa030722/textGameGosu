from entity import Entity
from rich.tree import Tree
from rich.console import Console
import utils

class Player(Entity):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        self.focus_tree = utils.load_json("focus_tree.json")
        self.completed_focuses = []
        
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(10)
        
    def take_damage(self, amount):
        super().take_damage(amount)

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
    
        focus_dict = {focus["id"]: focus for focus in self.focus_tree["focus_tree"]}
        rendered_focuses = set()

        def add_focus_to_tree(tree, focus_id):
            if focus_id in rendered_focuses:
                return
            focus = focus_dict[focus_id]
            if focus["prerequisites"]:
                for prerequisite in focus["prerequisites"]:
                    if prerequisite not in rendered_focuses:
                        add_focus_to_tree(tree, prerequisite)
            focus_label = (
                f"[green]{focus['name']}[/green]" if focus_id in self.completed_focuses else focus["name"]
            )
            focus_node = tree.add(focus_label)
            rendered_focuses.add(focus_id)
            return focus_node

        for focus in self.focus_tree["focus_tree"]:
            if len(focus["prerequisites"]) > 0:
                add_focus_to_tree(tree, focus["id"])

        console = Console()
        console.print(tree)
    def complete_focus(self, focus):
        """포커스를 완료하고 효과 적용"""
        print(f"\n=== Focus Completed: {focus['name']} ===")
        print(focus["description"])
        
        # 포커스 효과 적용
        
        
        # 포커스를 완료 리스트에 추가
        self.completed_focuses.append(focus["id"])
        print("Focus effect applied!")