
import pytest
from game import Game

def test_game_initialization():
    game = Game()
    assert game.player is not None
    assert game.enemy is not None
    assert game.dungeon is not None
    assert game.commands is not None

def test_game_player_health():
    game = Game()
    assert game.player.health == 100
