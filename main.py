
from graphviz import Digraph
import sys
import entity
import player

class Game:
    def __init__(self):
        self.player = player.Player("Hero", 100)
        self.enemy = entity.Entity("Goblin", 30)

    def run(self):
        print("A wild goblin appears!")
        while self.enemy.health > 0 and self.player.health > 0:
            action = input("Attack or Run? ").lower()
            if action == "attack":
                self.player.attack(self.enemy)
                if self.enemy.health > 0:
                    self.enemy.take_damage(5)
            elif action == "run":
                print("You fled!")
                break
        print("Game Over.")

def visualize_dependencies():
    dot = Digraph(comment="Module Dependency Tree")
    modules = ["main", "entity", "player"]
    
    for module in modules:
        dot.node(module, module)
    
    # Add basic dependencies
    dot.edge("main", "entity")
    dot.edge("main", "player")
    
    dot.render("dependencies", view=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--viz":
        visualize_dependencies()
    else:
        game = Game()
        game.run()
