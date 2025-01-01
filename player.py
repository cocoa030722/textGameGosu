import entity

class Player(entity.Entity):
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(10)