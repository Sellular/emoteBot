from discord import Message
from discord.ext.commands import Cog


class OnMessageCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        bot = self.bot
        channelId = message.channel.id
        emojis = []

        if channelId == bot.guildConfig['starReactChannelId']:
            emojis.append("⭐")
        if channelId == bot.guildConfig['yesNoReactChannelId']:
            emojis.append("✅")
            emojis.append("❌")

        if emojis:
            for emoji in emojis:
                await message.add_reaction(emoji)


def setup(bot):
    bot.add_cog(OnMessageCog(bot))
