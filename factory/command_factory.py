from command import command, explore_command, focus_command, inven_command, party_command


class CommandFactory:
    @staticmethod
    def create_commands()->dict:
        return {
            "info": command.InfoCommand(),
            "explore": explore_command.ExploreCommand(), 
            "quit": command.QuitCommand(),
            "focus": focus_command.FocusCommand(),
            "inven": inven_command.InventoryCommand(),
            "party": party_command.PartyCommand()
        }
