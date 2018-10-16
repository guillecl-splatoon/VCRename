import discord
import asyncio
from config import *
from discord.ext.commands import Bot

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
		for channel in client.get_all_channels():
			if str(channel.type) == "voice":
				if channel.id in VOICE_CHANNELS:
					if not channel.voice_members:
						await client.edit_channel(channel,name=DEFAULT_NAME + str(VOICE_CHANNELS[channel.id]))

@client.command(pass_context=True)
async def ping(ctx):
	if ctx.message.author.id == OWNER_ID:
		await client.send_message(ctx.message.channel, "Pong!")

@client.command(pass_context=True)
async def say(ctx, arg):
	if ctx.message.author.id == OWNER_ID:
    		await client.send_message(ctx.message.channel, arg)

@client.command(pass_context=True)
async def rename(ctx, arg):
	if ctx.message.author.voice.voice_channel.id in VOICE_CHANNELS:
		await client.send_message(client.get_channel(LOG_CHANNEL), ctx.message.author.mention + " ha cambiado el nombre de la sala " + str(ctx.message.author.voice.voice_channel) + " a " + arg)
		await client.edit_channel(ctx.message.author.voice.voice_channel,name=arg)
		
client.run(TOKEN)
