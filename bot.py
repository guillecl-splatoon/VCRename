import discord
import asyncio
from config import *

################## START INIT #####################
client = discord.Client()

def cmd(name, perms, description, *aliases):
    def real_decorator(func):
        commands[name] = [func, perms, description.format(BOT_PREFIX)]
        for alias in aliases:
            if alias not in commands:
                commands[alias] = [func, perms, "```\nAlias for {0}{1}.```".format(BOT_PREFIX, name)]
            else:
                print("ERROR: Cannot assign alias {0} to command {1} since it is already the name of a command!".format(alias, name))
        return func
    return real_decorator
	
################### END INIT ######################

############# COMMANDS #############

@cmd('name', [0,0], "```\n{0}Renames a channel.```")
async def cmd_rename(message, parameters):
    if parameters == '':
        return
	else:
		if message.author.voice.voice_channel in VOICE_CHANNELS:
			client.send_message(client.get_channel(LOG_CHANNEL), message.author.display_name + "has changed the name of " + client.get_channel(message.author.voice.voice_channel).name + "to " + parameteres
			client.get.channel(message.author.voice.voice_channel).name = parameters
			
			
@client.event
async def on_voice_state_update(before, after):
	if before.voice.voice_channel is not after.voice.voice_channel:
        if len(before.voice.voice_channel.voice_members) == 0:
			before.voice.voice_channel.name = DEFAULT_NAME


###### RUN ######			
try:
    client.loop.run_until_complete(client.start(TOKEN))
