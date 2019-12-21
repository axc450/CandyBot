from candybot.interface import database
from candybot.commands.framework import CandySettingsCommand, ArgumentSpec, CandyArgument, TextArgument


class MessageCandyCommand(CandySettingsCommand):
    name = "message"
    help = "Changes the candy drop message."
    aliases = ["candymessage", "candymsg"]
    examples = ["🍎 Apples appeared!", "apple Apples appeared!"]
    argument_spec = ArgumentSpec([CandyArgument, TextArgument], False)
    clean = True
    ignore = False

    async def _run(self):
        database.set_settings_candy_message(self.server_id, self.candy.id, self.text)
        await self.send(f"{self.candy} drop message has been changed")
