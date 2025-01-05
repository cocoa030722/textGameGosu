
import pytest
from player import Player

def test_player_initialization():
    player = Player("TestHero", 100, 50, 50)
    assert player.name == "TestHero"
    assert player.health == 100
    assert player.completed_focuses == []

def test_player_take_damage():
    player = Player("TestHero", 100, 50, 50)
    player.take_damage(20)
    assert player.health == 80

def test_get_available_focuses():
    player = Player("TestHero", 100, 50, 50)
    available = player.get_available_focuses()
    assert isinstance(available, list)
