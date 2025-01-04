
import pytest
from dungeon import Dungeon

def test_dungeon_initialization():
    dungeon = Dungeon()
    assert dungeon.current_floor == 1
    assert "enemy" in dungeon.dungeon_data[1]
    assert "item" in dungeon.dungeon_data[1]

def test_next_floor():
    dungeon = Dungeon()
    initial_floor = dungeon.current_floor
    dungeon.next_floor()
    assert dungeon.current_floor == initial_floor + 1

def test_max_floor():
    dungeon = Dungeon()
    for i in range(dungeon.MAX_FLOOR+10):
        dungeon.next_floor()
    assert dungeon.current_floor == dungeon.MAX_FLOOR
