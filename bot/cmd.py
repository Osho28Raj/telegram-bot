from telegram import BotCommand
class _BotCommands:
    def __init__(self):
        self.owner = "owner"
        self.start = "start"
        self.gandu = "gandu"
        self.slap = "slap"


info = _BotCommands()


botcmds = [
    BotCommand(f"{info.owner}", "To get owner id"),
    BotCommand(f"{info.start}", "Introduction of the bot"),
    BotCommand(f"{info.gandu}", "Gali sunne ke liye"),
    BotCommand(f"{info.slap}", "Slaps you with random objects")
]
