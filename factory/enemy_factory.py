from enemy import goblin

class EnemyFactory:
    @staticmethod
    def create_enemys():
        return {
            "goblin": goblin.Goblin(name="Goblin", health=30, attack_power=10, defense_power=0),
        }