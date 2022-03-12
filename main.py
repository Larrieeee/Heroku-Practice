# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os
load_dotenv('.env')
discordToken = os.getenv('TOKEN')

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

bot = commands.Bot(command_prefix = "!")

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.command(name = "test")
async def test_bot(context, response):
    await context.reply(response)

# Slash Commands --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)