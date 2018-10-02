import discord
import asyncio
from discord.ext.commands import Bot

BOT_PREFIX = '='
TOKEN = "NDk2NTEwOTMyNDc5MTE1Mjg0.DpRsZQ.xPZPqVxLft6tdhv0LnxNmX004ok"
SERVER = '496104544040910858'
LOG_CHANNEL = '496112192488210432'
VOICE_CHANNELS = ['496118243929620488','496118274908618752']
DEFAULT_NAME = "Otros Juegos"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(before, after):
	if before.voice.voice_channel is not after.voice.voice_channel:
		await client.send_message(client.get_channel('496104544040910860'),  "boop!")
		for channel in client.get_all_channels():
			if str(channel.type) == "voice":
				if channel.id in VOICE_CHANNELS:
					if not channel.voice_members:
						await client.edit_channel(channel,name=DEFAULT_NAME)

##@client.event
##async def on_message(message):
##	if message.content.startswith('=ping'):
##        	await client.send_message(message.channel, 'pong')
##
##	elif message.content.startswith('=rename'):
##		nombre = message.content.split(' ')[1]
##		await client.send_message(message.channel, nombre)
#		if message.author.voice.voice_channel in VOICE_CHANNELS:
#			await client.send_message(client.get_channel(LOG_CHANNEL), message.author.display_name + "has changed the name of " + client.get_channel(message.author.voice.voice_channel).name + "to " + nombre
#			client.get.channel(message.author.voice.voice_channel).name = nombre

@client.command()
async def ping():
	await client.send_message(client.get_channel('496104544040910860'), "Pong!")

@client.command(pass_context=True)
async def test(ctx, arg):
    await client.send_message(ctx.message.channel, arg1)

@client.command(pass_context=True)
async def test2(ctx, arg):
	await client.send_message(ctx.message.channel, ' '.join(arg1))
client.run(TOKEN)

############# BACKUP #############

#def cmd(name, perms, description, *aliases):
#    def real_decorator(func):
#        commands[name] = [func, perms, description.format(BOT_PREFIX)]
#        for alias in aliases:
#            if alias not in commands:
#                commands[alias] = [func, perms, "```\nAlias for {0}{1}.```".format(BOT_PREFIX, name)]
#            else:
#                print("ERROR: Cannot assign alias {0} to command {1} since it is already the name of a command!".format(alias, name))
#        return func
#    return real_decorator

#@cmd('nombre', [0,0], "```\n{0}Renames a channel.```")
#async def cmd_rename(message, parameters):
#    if parameters == '':
#        return
#	else:
#		if message.author.voice.voice_channel in VOICE_CHANNELS:
#			await client.send_message(client.get_channel(LOG_CHANNEL), message.author.display_name + "has changed the name of " + client.get_channel(message.author.voice.voice_channel).name + "to " + parameters
#			client.get.channel(message.author.voice.voice_channel).name = parameters			

#@cmd('ping', [0,0], "```\n{0}Ping.```")
#async def cmd_ping(message, parameters):
#	await reply(message, "ping")					  


