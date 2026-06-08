import discord
from discord.ext import commands
from agent import Agent
from config import Config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
agent = Agent()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        response = agent.run(message.content)
        await message.reply(response)

    await bot.process_commands(message)

if __name__ == '__main__':
    bot.run(Config.DISCORD_TOKEN)
