import discord
import asyncio
from discord.ext.commands import Bot

BOT_PREFIX = '='
TOKEN = "NDk2NTEwOTMyNDc5MTE1Mjg0.DpRsZQ.xPZPqVxLft6tdhv0LnxNmX004ok"
SERVER = '496104544040910858'
LOG_CHANNEL = '496112192488210432'
VOICE_CHANNELS = ['496118243929620488','496118274908618752']
DEFAULT_NAME = "Otros Juegos "

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
		count = 0
		for channel in client.get_all_channels():
			if str(channel.type) == "voice":
				if channel.id in VOICE_CHANNELS:
					count = count + 1
					if not channel.voice_members:
						await client.edit_channel(channel,name=DEFAULT_NAME + str(count)

@client.command()
async def ping():
	await client.send_message(client.get_channel('496104544040910860'), "Pong!")

@client.command(pass_context=True)
async def test(ctx, arg):
    await client.send_message(ctx.message.channel, arg)

@client.command(pass_context=True)
async def rename(ctx, arg):
	await client.send_message(client.get_channel('496104544040910860'), ctx.message.author.display_name + " ha cambiado el nombre de la sala " + ctx.message.author.voice.voice_channel.name + " a " + arg)
	await client.edit_channel(ctx.message.author.voice.voice_channel,name=arg)
	
client.run(TOKEN)

