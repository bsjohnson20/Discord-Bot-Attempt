import json
import logging
from discord import app_commands
from discord.ext import commands
import discord
import requests
import time
from datetime import datetime
import csv

with open('secrets.txt', 'r') as f:
    x = f.readlines()
    for i in x:
        print(i)
    Server_id = int(x[0])
    TOKEN = x[1]

logging.basicConfig(level=logging.INFO)
logging.info('Discord Bot activated!')


def awaitLog(message):
    logging.info(message)
    return True


def fetchWeather(location):
    logging.info(f'Location: {location}')
    x = requests.get(f'http://api.weatherapi.com/v1/current.json?key=0adf8e4333174820955202743221407&q={location}')
    logging.info(x.text)
    json_weather = json.loads(x.text)
    weather = json_weather['current']['condition']['text']
    temp = json_weather['current']['temp_c']
    humidity = json_weather['current']['humidity']
    return f"Weather: {weather}\nTemperature: {str(temp)}°C\nHumidity {str(humidity)}%"


def WhatTimeIsItMrWolf():
    return time.time()


def pong():
    return "Pong!"


def WhatDayisIt():
    logging.info(f'{commands.context}')
    return f"The day is: {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][datetime.today().weekday()]}"


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=">", intents=intents)

    async def setup_hook(self):
        await self.tree.sync(guild=discord.Object(Server_id))
        print(f'Synced slash commands for {self.user}')

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral=True)


bot = Bot()


class HyBridCommands:
    def __init__(self, name, app, description, command, server_id=Server_id, arguments=False):
        super(HyBridCommands, self).__init__()
        self.name = str(name)
        self.app_command = app
        self.desc = description
        self.id = server_id
        self.command = command
        self.arguments = arguments
        if arguments == True:
            self.Main()
        else:
            self.NoArgsMain()

    def Main(self):
        @bot.hybrid_command(name=self.name, with_app_command=self.app_command, description=self.desc)
        @app_commands.guilds(self.id)
        @commands.has_permissions(administrator=True)
        async def main(ctx: commands.Context, arguments):
            await ctx.defer(ephemeral=True)
            await ctx.reply(self.command(self.arguments))
            # await logging.info(f'{commands.context}')

    def NoArgsMain(self):
        @bot.hybrid_command(name=self.name, with_app_command=self.app_command, description=self.desc)
        @app_commands.guilds(self.id)
        @commands.has_permissions(administrator=True)
        async def main(ctx: commands.Context):
            await ctx.defer(ephemeral=True)
            await ctx.reply(self.command())
            # await logging.info(f'{commands.context}')


Weather = HyBridCommands(name='weather',  # Fetches weather using API
                         app=True,
                         description='Returns the weather of location',
                         command=fetchWeather,  # command to run to get results and reply with
                         arguments=True)  # we want things to send to it, idfk what to replace with

Time = HyBridCommands(name='time',
                      app=True,
                      description='Returns the time',
                      command=WhatTimeIsItMrWolf)

day = HyBridCommands(name='day',
                     app=True,
                     description='Returns what day of the week it is',
                     command=WhatDayisIt)

ping = HyBridCommands(name='ping',
                      app=True,
                      description='pong',
                      command=pong)

pony = HyBridCommands(name='pony',
                      app=True,
                      description='pong',
                      command=lambda: 'pony')
pony = HyBridCommands(name='',
                      app=True,
                      description='evil_boss_laughter_commence',
                      command=lambda: '>:)')
pony = HyBridCommands(name='2',
                      app=True,
                      description='pong',
                      command=lambda: '2')
pony = HyBridCommands(name='3',
                      app=True,
                      description='pong',
                      command=lambda: '3')
pony = HyBridCommands(name='4',
                      app=True,
                      description='pong',
                      command=lambda: '4')
bot.run(TOKEN)

# Weather = HyBridCommands(name='weather', app=True, description='Returns the weather of location', command=fetchWeather)
# Weather = HyBridCommands(name='weather', app=True, description='Returns the weather of location', command=fetchWeather)
# Weather = HyBridCommands(name='weather', app=True, description='Returns the weather of location', command=fetchWeather)

'''
@bot.hybrid_command(name='testing', with_app_command=True, description='test my ass')
@app_commands.guilds(Server_id)
@commands.has_permissions(administrator=True)
async def test(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply("Hi!")
    # await logging.info(f'{commands.context}')
'''
'''
@bot.hybrid_command(name='time', with_app_command=True, description='test my ass')
@app_commands.guilds(Server_id)
@commands.has_permissions(administrator=True)
async def test(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply(WhatTimeIsItMrWolf())
    await logging.info(f'{commands.context}')
'''
'''
@bot.hybrid_command(name='day', with_app_command=True, description='test my ass')
@app_commands.guilds(Server_id)
@commands.has_permissions(administrator=True)
async def test(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply(WhatDayisIt())
'''
'''
@bot.hybrid_command(name='ping', with_app_command=True, description='Hello everypony!')
@app_commands.guilds(Server_id)
@commands.has_permissions(administrator=True)
async def Ping(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply("HELLO")
'''
'''
@bot.hybrid_command(name='weather', with_app_command=True, description='GIMME THE DARN WEATHER YOU FOOL!')
@app_commands.guilds(Server_id)
@commands.has_permissions(administrator=True)
async def Weather(ctx: commands.Context, location):
    await ctx.defer(ephemeral=True)
    await ctx.reply(fetchWeather(location))
'''
