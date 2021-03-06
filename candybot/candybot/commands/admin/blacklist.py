from candybot.interface import database, converters
from candybot.commands.framework import AdminCommand, ArgumentSpec, UserArgument


class BlacklistCommand(AdminCommand):
    name = "blacklist"
    help = "Shows current blacklist or blacklists a user from interacting with CandyBot."
    aliases = ["bl"]
    examples = ["", "@User", "User#1234", "123456789"]
    argument_spec = ArgumentSpec([UserArgument], True)
    clean = True
    ignore = False
    
    async def _run(self):
        user = self.args.get("user")
        blacklist = database.get_blacklist(self.server.id)
        if user is None:
            self.title = ":lock: CandyBot Blacklist"
            blacklist = [(await converters.to_user(str(x), self.message.guild)).mention for x in blacklist]
            await self.send("\n".join(blacklist))
        else:
            if user.id in blacklist:
                database.set_blacklist(self.server.id, user.id, remove=True)
                await self.send(f"{user.mention} was removed from the CandyBot blacklist")
            else:
                database.set_blacklist(self.server.id, user.id, remove=False)
                await self.send(f"{user.mention} was added to the CandyBot blacklist")
