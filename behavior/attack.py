from .behavior import Behavior

class CommonAttack(Behavior):
    def execute(self, enemy)->str:
        return f"{enemy.name}:일반 공격!"

class SpreadPoison(Behavior):
    def execute(self, enemy)->str:
        return f"{enemy.name}:독을 뿌렸다!"

class SpreadParalyzingPowder(Behavior):
    def execute(self, enemy)->str:
        return f"{enemy.name}:마비가루를 뿌렸다!"