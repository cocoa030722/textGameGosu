
import pytest
from enemy.goblin import Goblin
from player import Player

def test_goblin_initialization():
    goblin = Goblin("TestGoblin", 30, 10, 0)
    assert goblin.name == "TestGoblin"
    assert goblin.health == 30

def test_goblin_attack():
    goblin = Goblin("TestGoblin", 30, 10, 0)
    player = Player("TestHero", 100, 50, 50)
    initial_health = player.health
    goblin.attack(player)
    assert player.health < initial_health
