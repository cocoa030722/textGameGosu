import commands

class CommandFactory:
    @staticmethod
    def create_commands()->dict:
        return {
            "info": commands.InfoCommand(),
            "explore": commands.ExploreCommand(), 
            "quit": commands.QuitCommand(),
            "focus": commands.FocusCommand(),
            "inven": commands.InventoryCommand(),
            "party": commands.PartyCommand()
        }
