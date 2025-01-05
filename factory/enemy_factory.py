from enemy import goblin
from enemy.boss import alchemist
class EnemyFactory:
    @staticmethod
    def create_enemys():
        return {
            "goblin": goblin.Goblin(name="goblin", health=30, attack_power=10, defense_power=0),
            "alchemist": alchemist.Alchemist(name="alchemist", health=200, attack_power=10, defense_power=0)
        }