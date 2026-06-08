import os
import discord
from agent import Agent
from tools.orchestrator import Orchestrator

class PokeDiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agent = Agent()
        self.orchestrator = Orchestrator(self.agent)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        response = self.orchestrator.handle_request(message.content)
        await message.channel.send(response)

if __name__ == "__main__":
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        print("Error: DISCORD_BOT_TOKEN not found in environment.")
        exit(1)

    intents = discord.Intents.default()
    intents.message_content = True
    client = PokeDiscordClient(intents=intents)
    client.run(token)
