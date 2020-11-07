import discord

from discord.ext import commands
from discord.utils import get
from fluffshit import *
from async_timeout import timeout
from discord.ext import commands


class DiscordRNG(commands.Cog):
	@commands.command(name='--rand-hex=')
	async def rand_hex(ctx, str_cnt = 1, hex_str_len = 2):
		"""generate random hexadecimal numbers"""
		
		for count in range(0, int(str_cnt)):
			result = rand_num.generate_hex_str(True, hex_str_len)
			await ctx.send(f'```java\nYour hexadecimal string is :\n0x{result.upper()}```')
