from modulegraph import ModuleGraph
from graphviz import Digraph

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


def visualize_dependencies(entry_point: str):
    mg = ModuleGraph()
    mg.run_script(entry_point)

    dot = Digraph(comment="Module Dependency Tree")
    for node in mg.flatten():
        dot.node(node.identifier, node.identifier)

        for edge in node.imports:
            dot.edge(node.identifier, edge.identifier)

    dot.render("dependencies.gv", view=True)



if __name__ == "__main__":
    #game=Game()
    #game.run()
    # main.py에서 시작하는 의존성 트리 생성
    visualize_dependencies("main.py")