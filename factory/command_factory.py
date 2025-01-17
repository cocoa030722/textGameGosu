import command
from command import InfoCommand, ExploreCommand, QuitCommand, FocusCommand, InventoryCommand, PartyCommand, \
    FailSafeCommand


class CommandFactory:
    @staticmethod
    def create_commands()->dict:
        return {
            "info": InfoCommand(),
            "explore": ExploreCommand(),
            "quit": QuitCommand(),
            "focus": FocusCommand(),
            "inven": InventoryCommand(),
            "party": PartyCommand(),
            "failsafe": FailSafeCommand()
        }
