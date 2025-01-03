
import pytest
from entity import Entity

class TestEntity(Entity):
    def take_damage(self, amount):
        super().take_damage(amount)

def test_entity_initialization():
    entity = TestEntity("TestEntity", 100)
    assert entity.name == "TestEntity"
    assert entity.health == 100

def test_entity_take_damage():
    entity = TestEntity("TestEntity", 100)
    entity.take_damage(30)
    assert entity.health == 70
