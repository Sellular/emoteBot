from os import listdir
from discord.ext.commands import Bot

from utils import GeneralUtils


def importCogs(bot: Bot):
    for filename in listdir("./cogs/events"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.events." + cogName)


def importCache(bot: Bot):
    try:
        guildConfig = GeneralUtils.getConfig('guild')

        if not guildConfig:
            raise Exception("Guild config not found.")

        starChannelId = guildConfig['star_react_channel_id']
        yesNoChannelId = guildConfig['yes_no_react_channel_id']

        if not starChannelId:
            raise Exception("STAR_REACT_CHANNEL_ID not found in Guild config")
        if not yesNoChannelId:
            raise Exception(
                "YES_NO_REACT_CHANNEL_ID not found in Guild config.")

        bot.guildConfig = {}
        bot.guildConfig['starReactChannelId'] = int(starChannelId)
        bot.guildConfig['yesNoReactChannelId'] = int(yesNoChannelId)
    except Exception as error:
        print(error)
