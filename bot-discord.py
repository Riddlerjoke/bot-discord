import os
import discord
import random

from Quotes import quotes
from discord.ext import commands
from dotenv import load_dotenv



#le fichier .ENV situé en dessous sert a stocker les informations racines du Bot !

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#le prefix de la command permet d'avoir un premier charactere en commun a toutes commandes du Bot, pour facilité l'interactivité !

bot = commands.bot.Bot(command_prefix='!')
client = discord.Client()

#la fonction 'on_ready' permet d'avoir une preuve ecrite du fonctionnement du Bot !

@bot.event
async def on_ready():
    print(f'{bot.user.display_name} has connected to Discord!')

#la fonction on_message permet de repondre a l'utilisateur qui l'a appelé, dans le channel approprié !


async def on_message(message):
    if message.author == bot.user.display_name:
        return

#la command 'punchline', fait appel une bibliotheques de repliques de films, contenue dans le fichier Quotes.py
#avec inclue l'outils random.choice , qui permet de choisir aleatoirement une repliques dans la bibliotheque !


@bot.command(name='punchline', help='command to send reponse with Movie Quotes !')
async def _punchline(ctx):
    ranique = quotes
    response = random.choice(ranique)
    await ctx.send(response)

# la command 'yo', permet au Bot de repondre a l'utilisateur qui l'appel, en le mentionnant dans celle-ci !


@bot.command(name='yo', help='command to send reponse with user mention !')
async def _yo(ctx):
    await ctx.send(f"Hello {format(ctx.message.author.mention)}, une excellente journée à toi !")

# la command 'create-channel', permet au administrateur de creer un voice channel personnalisé a l'utilisateur qui le demande


@bot.command(name='create-channel', help='create voicechannel,with Username, userlimit')
@commands.has_role('Batman')
async def create_voice_channel(ctx):
    guild = ctx.guild
    channel_name = f'channel of : {ctx.message.author}'
    existing_channel = discord.utils.get(guild.voice_channels, name='Squad '+f'{ctx.message.author}', position=2, bitrate=64000, user_limit=4, category=[2])
    new_channel = ctx.guild.categories[2].create_voice_channel(name='Squad '+f'{ctx.message.author}', position=2, bitrate=64000, user_limit=4)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await new_channel



@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.run(TOKEN)
