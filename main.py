import json

from game import Game

if __name__ == "__main__":
    with open("game_data.json") as f:
        data = json.load(f)
    
    game=Game()
    game.run()
