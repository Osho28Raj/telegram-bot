from typing import Any

from telegram import TelegramObject


class bot(TelegramObject):
    __slots__ = ('description', '_id_attrs', 'command')

    def __init__(self, command: str, description: str, **_kwargs: Any):
        self.command = command
        self.description = description

        self._id_attrs = (self.command, self.description)
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
