
import commands

class CommandFactory:
    @staticmethod
    def create_commands():
        return {
            "start": commands.StartCommand(),
            "explore": commands.ExploreCommand(), 
            "fight": commands.FightCommand(),
            "quit": commands.QuitCommand(),
            "focus": commands.FocusCommand(),
        }
