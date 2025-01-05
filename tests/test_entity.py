
import pytest
from entity import Entity

class TestEntity(Entity):
    def take_damage(self, attack_power):
        super().take_damage(attack_power)

def test_entity_initialization():
    entity = TestEntity("TestEntity", 100, 10, 10)
    assert entity.name == "TestEntity"
    assert entity.health == 100

def test_entity_take_damage():
    entity = TestEntity("TestEntity", 100, 10, 10)
    entity.take_damage(30)
    assert entity.health == 70
