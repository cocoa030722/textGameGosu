class Command:
    def execute(self):
        pass

class StartCommand(Command):
    def execute(self):
        print("Game started!")

class ExploreCommand(Command):
    def execute(self):
        print("Exploring the area...")

class FightCommand(Command):
    def execute(self):
        print("Entering a fight!")

class QuitCommand(Command):
    def execute(self):
        print("Quitting the game...")
        exit()

