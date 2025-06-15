import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

colorama.init()

bot = commands.Bot(command_prefix="-", intents=intents)

token = os.getenv("TOKEN")  # Use Render environment variable

@bot.event
async def on_ready():
    print(f"""{Fore.RED}
███████     ████████       ████████████       {Fore.CYAN}████████████    ████████████      {Fore.RED}██          ██
██    ██      ██          ██               ██                  ██                 ██          ██
██    ██      ██          ██               ██                  ██                 ██          ██
██████        ██          ██      █████    ██      █████     █████████        {Fore.CYAN}██████████████
██             ██          ██         ██    ██         ██       ██                 ██          ██
██          ████████       ████████████     ███████████        {Fore.CYAN}████████████       {Fore.RED}██         ██
""")

@bot.command()
async def dm(ctx):
    dm_message = "What you want to send to people here"
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            if member.id == bot.user.id:
                continue
            await member.send(dm_message)
            print(f"✅ Sent to {member}")
            await asyncio.sleep(1)
        except:
            print(f"❌ Couldn't send to {member}")

bot.run(token)
