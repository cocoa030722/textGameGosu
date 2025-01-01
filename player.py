from entity import Entity

class Player(Entity):
    def __init__(self, name, health, focus_tree):
        self.name = name
        self.health = health
        self.focus_tree = focus_tree
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

    def complete_focus(self, focus):
        """포커스를 완료하고 효과 적용"""
        print(f"\n=== Focus Completed: {focus['name']} ===")
        print(focus["description"])
        
        # 포커스 효과 적용
        
        
        # 포커스를 완료 리스트에 추가
        self.completed_focuses.append(focus["id"])
        print("Focus effect applied!")