from player import Player
from npc.goblin import Goblin
import commands
import utils

class Game:
    def __init__(self):
        focus_tree = utils.load_json("focus_tree.json")
        self.player = Player("Hero", 100, focus_tree)
        self.enemy = Goblin("Goblin", 30)
        self.commands = {
            "start": commands.start_game(),
            "explore": commands.explore(),
            "fight": commands.fight(),
            "quit": commands.quit_game()
        }

    def run(self):
        print("A wild goblin appears!")
        while self.player.health > 0:
            action = input("Attack or Run? ").lower()
            if action == "attack":
                self.player.attack(self.enemy)
                if self.enemy.health > 0:
                    self.enemy.take_damage(5)
            elif action == "run":
                print("You fled!")
                break
        print("Game Over.")