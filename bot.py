from discord import Intents
from discord.ext.commands import Bot

from utils import SetupUtils, GeneralUtils


class EmoteBot(Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self: Bot):
        print("Bot running with:")
        print("Username: ", self.user.name)
        print("User ID: ", self.user.id)
        print('-----')


bot = EmoteBot()
SetupUtils.importCogs(bot)
SetupUtils.importCache(bot)

try:
    botConfig = GeneralUtils.getConfig('bot')

    if not botConfig:
        raise Exception("Bot config not found.")

    bot_token = botConfig['token']
    if not bot_token:
        raise Exception("TOKEN not found in Bot config")

    bot.run(bot_token)

except Exception as error:
    print(error)
