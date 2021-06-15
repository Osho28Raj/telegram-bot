from telegram import BotCommand as bot
class _BotCommands:
    def __init__(self):
        self.owner = "owner"
        self.start = "start"
        self.gandu = "gandu"
        self.slap = "slap"


info = _BotCommands()


botcmds = [
    bot(f"{info.owner}", "To get owner id"),
    bot(f"{info.start}", "Introduction of the bot"),
    bot(f"{info.gandu}", "Gali sunne ke liye"),
    bot(f"{info.slap}", "Slaps you with random objects")
]
