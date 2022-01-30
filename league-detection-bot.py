import discord
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Time to find some league players....")

@client.event
async def on_message(message):
    if message.content.startswith('whos playing league rn?'):
        guild = client.get_guild(message.guild.id)
        for member in guild.members:

            #tuple layout [custom bio, spotify, discord, game activity]
            activity_list = member.activities

            if  len(activity_list) != 0:
                activity = activity_list[len(activity_list)-1]

                #if they've been playing league for more than thirty
                #minutes they're going to be pinged
                if activity.name.lower() == "league of legends":
                    await message.channel.send(member.display_name + " is playing " + activity.name)
                    time_start = activity.start
                    time_now = datetime.utcnow()
                    duration = time_now - time_start

                    seconds = duration.total_seconds()
                    minutes = divmod(seconds, 60)[0]
                    print("Minutes: ", minutes)
                    if minutes > 30.0:
                        await message.channel.send("GET A FUCKING JOB YOU DWEEB <@" + str(member.id) + ">")


client.run(os.getenv('TOKEN'))