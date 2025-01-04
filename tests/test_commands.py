
import pytest
from commands import InfoCommand, ExploreCommand, FightCommand, QuitCommand
from game import Game
from dungeon import Dungeon
from player import Player

def test_info_command():
    game = Game()
    command = InfoCommand()
    try:
        command.execute(game, game.dungeon, game.player)
        assert True  # Command executed without errors
    except Exception:
        assert False

def test_explore_command():
    game = Game()
    command = ExploreCommand()
    initial_floor = game.dungeon.current_floor
    command.execute(game, game.dungeon, game.player)
    assert game.dungeon.current_floor >= initial_floor
