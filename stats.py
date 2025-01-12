
class Stats:
    def __init__(self, health:int, attack_power:int, defense_power:int, exp:int=0):
        self.health:int = health
        self.max_health:int = health
        self.attack_power:int = attack_power
        self.defense_power:int = defense_power
        self.exp:int = exp
        
    def take_damage(self, attack_power:int) -> int:
        damage = (attack_power - self.defense_power) if (attack_power - self.defense_power) > 0 else 0
        self.health -= damage
        return damage
    
    def heal(self, amount:int) -> None:
        self.health = min(self.health + amount, self.max_health)
        
    def modify_attack(self, amount:int) -> None:
        self.attack_power += amount
        
    def modify_defense(self, amount:int) -> None:
        self.defense_power += amount
