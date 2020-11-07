import random
import discord
import os

from discord.ext import commands
from discord.utils import get
from fluffshit import *
from Gusic import *
from RandomNumberGenerator import RNG
from Constants import Const

AEON_TOKEN = ''

Aeon = commands.Bot(command_prefix='dvl ', description='Fluffy\'s psychotic expiramental multipurpose bot.')
Aeon.add_cog(Music(Aeon))

@Aeon.event
async def on_ready():
  print(f'Logged in as \nUser : {Aeon.user.name}\nID   : {Aeon.user.id}')
  print(f'Loading {Aeon.command}')

  await Aeon.change_presence(status=discord.Status.online, activity=discord.Game("with your mother's clit"))
  
  print(f'Aeon is ready to go ^,..,^')
  
  
  
@Aeon.event
async def on_member_join(member):
  rand_int = random.randint(0, 5)
  
  for count in range(0, 4):
    if rand_int == 0: 
       await member.create_dm()
       await member.dm_channel.send(f'```css\nThe fuck is up, {member.name}, welcome to the party, ya limy cunt!```')
    
    elif rand_int == 1:
       await member.create_dm()
       await member.dm_channel.send(f'```css\nWelcome to the thunder dome, {member.name}, hope you brought your \"big kid undies\"!```')
    
    elif rand_int == 2: 
       await member.create_dm()
       await member.dm_channel.send(f'```css\n {member.name}...welcome to the server you FUCKIN NERD!```')
    
    elif rand_int == 3: 
       await member.create_dm()
       await member.dm_channel.send(f'```css\nThe fuck you doin\' here, {member.name}, no shooting up in the bathrooms!```')
    
    elif rand_int == 4: 
       await member.create_dm()
       await member.dm_channel.send(f'```css\nGet ready to suck off you 7ft albanian cellmate\'s tic tac, {member.name}, and don\'t drop the soap!```')



@Aeon.command(name="--exit=")
async def shutdown(ctx, arg):
  """shuts down Aeon"""

  id = str(ctx.author.id)
  
  if id == MY_ID():
    await ctx.send(f"```CSS\nShitdown process initiated!\nLogging out and shitting down now...\nexit : {arg}```")
    await ctx.bot.logout()
    print('Aeon has been shut down')
  
  else:
    await ctx.send(f"```CSS\n{ctx.author.name}yooooou're NOT my FUCKING father! E,..,E\nFuck right off with that shit!\n I'm telling on you!```")
    print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to activate : --exit=\nWith value : {arg}\nOperation aborted, wanrning sent to dad')


@Aeon.command(name = '--reset')
async def reset_bot(ctx : commands.Context, arg = 0):
	"""Resets BlackMarket"""
	
	id = str(ctx.author.id)
	usr = ctx. author.name
	bot = Aeon.user.name
	
	if id == MY_ID():
		await ctx.send(Const.Logout.INIT_SHUTDOWN.format(arg))
		await ctx.bot.logout()
		print(f'Resetting {bot} ?,..,?')
		subprocess.call([sys.executable, 'Aeon.py'])
	
	else:
		await ctx.send(ERR.ERR_STR.format(usr))
		print(ERR.WARNING.format(usr, id, Const.CMD.EXT, arg))


@Aeon.command(name="--aeons-dad")
async def father(ctx):
  """discord pings Aeon's creator, Fluffykins"""
  
  id = MY_ID()

  await ctx.send(f'<@{id}>')



@Aeon.command(name = "--help", pass_context = True)
async def Help(ctx):
  embed_1 = discord.Embed(title = "Help (1/3)", description = "This command is for if your're fucking retarded and don't know how to use me. e,..,e", color = 0xAC58FA)
  embed_1.add_field(name = "Help 1", value = "dvl --help", inline = True)
  embed_1.add_field(name = "Help 2", value ="dvl --help-2", inline = True)
  embed_1.add_field(name = "Help 3", value ="dvl --help-3", inline = True)
  embed_1.add_field(name = "CursedBy360noscopefox", value = "dvl --cursed", inline = True)
  embed_1.add_field(name = "Echo", value = "dvl --echo", inline = True)
  embed_1.add_field(name = "Hello", value = "dvl --hello", inline = True)
  embed_1.add_field(name = "Twinkie House!", value = "dvl --twink-house", inline = True)
  embed_1.add_field(name = "Roll Die!", value = "dvl -r [die_type]", inline = True)
  embed_1.add_field(name = "Roll Dice!", value = "dvl --roll= [num] [die_type]", inline = True)
  embed_1.set_footer(text = "Authors : Fluffykins")
  
  await ctx.send(embed = embed_1)  

@Aeon.command(name = "--help-2", pass_context=True)
async def Help2(ctx):
  embed_2 = discord.Embed(title = "Help (2/3)", description = "This command is for if your're fucking retarded and don't know how to use me. e,..,e", color=0x2EFEF7)
  embed_2.add_field(name = 'Aeons Dad', value = "dvl --aeons-dad", inline=True)
  embed_2.add_field(name = "Latency Test", value = "dvl --ping", inline=True)
  embed_2.add_field(name = "Embed Test", value = "dvl --embed-test", inline=True)
  embed_2.add_field(name = "Info", value = "dvl --info", inline=True)
  embed_2.set_footer(text = "Authors : Fluffykins")

  await ctx.send(embed = embed_2)


@Aeon.command(name="--ban-user=")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  """Bans a user from your server"""
  id = str(ctx.author.id)

  if id == MY_ID():
    await member.ban(reason = reason)
    await ctx.send(f"```CSS\nUser {member} got fucking Banished!```")
  else:
    await ctx.send(f'```CSS\n{ctx.author.name}, you are NOT my father, you CANT TELL ME TO DO THAT SHIT YOU PANSY RETARD CUNT! E,..,E\nIm telling dad on you!```')
    print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to activate : --kick-user=\nWith value : {member}\nOperation aborted, wanrning sent to dad')


@Aeon.command(name="--kick-user=")
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
  """Kicks a user from your server"""
  id = str(ctx.author.id)

  if id == MY_ID():
    await member.kick(reason = reason)
    await ctx.send(f"```CSS\nUser {member} got fucking Exiled!")
  
  else:
    await ctx.send(f'```CSS\n{ctx.author.name}, you are NOT my father, you CANT TELL ME TO DO THAT SHIT YOU PANSY SLOWTARD CUNT! E,..,E\nIm telling dad on you!```')
    print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to activate : --kick-user=\nWith value : {member}\nOperation aborted, wanrning sent to dad')


@Aeon.command(name = "--ping")
async def latency_test(ctx):
  """Test Aeon's latency"""
  await ctx.send(f'```py\nPong!\nLatency : {Aeon.latency}```')


@Aeon.command(name = "--embed-test")
async def embed_test(ctx):
  """Test Aeon's embed capabilities"""
  
  test_embed = discord.Embed(title = "Testing the Cunt :stuck_out_tongue:")
  test_embed.add_field(name = "Ebmed Test", value = "Testing your mother's cunt", inline = False)
  test_embed.set_thumbnail(url='https://www.sourpussclothing.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/p/e/period_panties_cunt_dracula_1.jpg')
  test_embed.set_footer(text = "Doin' ya mom, d-d-doin' ya mom!")

  await ctx.send(embed = test_embed)


@Aeon.command(name = "--ping=")
async def ping_spam(ctx, arg_str, member: discord.Member):
  """ping-spam a user and test the latency. over and over. As many times as you like - protected"""
  victim = str(member.id)
  id = str(ctx.author.id)

  if id == MY_ID():
    if arg_str.isnumeric() is True:
      for count in range(int(arg_str)):
        await ctx.send(f'<@{victim}>\n```py\nLatency : {Aeon.latency}```')
    
    else:
      await ctx.send(f'```py\n\"{arg_str}\" is NOT numeric! e,..,e```')

  else:
    await ctx.send(f'```CSS\nFuck off! You can\'t do that, you\'re not dad! E,..,E```')

  await ctx.send(f'```py\nLatency : {Aeon.latency}```')


@Aeon.command(name="--cursed", pass_context=True)
async def cursed(ctx):
    """cursed by 360noscopefox"""
    embed_4 = discord.Embed(title = 'Thaaats Cursed...')
    embed_4.set_thumbnail(url = "https://i.redd.it/wkiykfkyr6p31.jpg")
    embed_4.add_field(name = "Those hands...", value = "Begone!", inline = False)
    
    await ctx.send(embed = embed_4)


@Aeon.command(name = "--cursed=", pass_context=True)
async def cursed_spam(ctx, arg_str):
  """spam cursed - protected"""
  id = str(ctx.author.id)

  if id == MY_ID():  
    if arg_str.isnumeric() is True:
      for count in range(int(arg_str)):
        await cursed(ctx)
    
    else:
      await ctx.send("```CSS\nAre you fucking retarded? e,..,e```")



@Aeon.command(name='--twink-house', pass_context=True)
async def twinkie_house(ctx, member: discord.Member, reason='no reason'):
  """'Twinkie House' someone"""
  embed_5 = discord.Embed(title='Twinkie House!', description='itty bitty baby...itty bitty boat...', color=0xACFA58)
  rand_num = random.randint(0, 5)
  habeeb_it = f"Habeeb it, {member.name}!"
  i_dont = f'{member} : \"I don\'t believe it!\"'
  id = str(member.id)

  await ctx.send('<@{}>'.format(id))

  if rand_num == 5:
    embed_5.set_thumbnail(url='https://64.media.tumblr.com/196fda28bb30dde26ebbddb0c089ecce/tumblr_p0luyz0CQr1vheqneo1_500.png')
    embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)
  
  elif rand_num == 4:
    embed_5.set_thumbnail(url='https://t04.deviantart.net/LbJTfltaaqNm5Hp0GuJZPuNXi1g=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre11/dbf4/th/pre/f/2009/274/4/2/twinkie_house_by_nekoninja12.png')
    embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)
  
  elif rand_num == 3:
    embed_5.set_thumbnail(url='https://external-preview.redd.it/tj_19XlsUL8TUe2RFyWumq7dznJ3ZwNcaFwO0B84mJg.jpg?auto=webp&s=d786b8b0839e7b965bad3761e6d434f11bc9474c')
    embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)

  elif rand_num == 2:
    embed_5.set_thumbnail(url='https://i0.kym-cdn.com/photos/images/original/000/896/675/78e.jpg')
    embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)

  elif rand_num == 1:
    embed_5.set_thumbnail(url='https://i0.kym-cdn.com/photos/images/original/000/022/614/3JJN4VJA7USJQLD5WKCLFJBLC6LJFG5P.png')
    embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)
  
  elif rand_num == 0:
    embed_5.set_thumbnail(url='https://archive.is/XuPos/3d00a03f7329c484f5603186652f754e215aeb2f.jpg')
    embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)

  embed_5.set_footer(text=str(reason))

  await ctx.send(embed=embed_5)


@Aeon.command(name="--twink-house=")
async def twinkie_house_spam(ctx, arg_str, member: discord.Member, reason='no reason'):
  """ 'Twinkie House' someone. Over and over. As many times as you like -protected """
  id = str(ctx.author.id)

  if id == MY_ID():
    if arg_str.isnumeric() is True:
      for count in range(int(arg_str)):
       await twinkie_house(ctx, member, reason)
  
    else:
      await ctx.send("```CSS\nDuuude, that string isn't fucking numeric!\nAre you like...LITERALLY retarded or something? e,..,e\n")
      
  else:
    await ctx.send("```CSS\nYou're not my dad! -,..,-```")
    print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to activate : --kick-user=\nWith value : {arg_str}\nOperation aborted, wanrning sent to dad')


@Aeon.command(name="-r")
async def roll_dice(ctx, arg_str):
  """roll a die!"""
  dice = ['d4', 'd6', 'd8', 'd10', 'd%', 'd12', 'd20', 'd10+d%']
  name = str(ctx.author.id)
  embed_6 = discord.Embed(title="Roll Die!")
  
  if arg_str == dice[0]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'\nYour {dice[0]} roll is :', value=f'{random.randint(1, 4)}')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)
  
  elif arg_str == dice[1]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'\nYour {dice[1]} roll is :', value=f'{random.randint(1, 6)}')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)
    
  elif arg_str == dice[2]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'\nYour {dice[2]} roll is :', value=f'{random.randint(1, 8)}')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)

  elif arg_str == dice[3]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'\nYour {dice[3]} roll is :', value=f'{random.randint(1, 9)}')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)
    
  elif arg_str == dice[4]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'\nYour {dice[4]} roll is :', value=f'{random.randint(1, 9)}0')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)

  elif arg_str == dice[7]:
    d_10 = random.randint(0, 9)
    d_mod = random.randint(0, 9)

    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'\nYour {dice[7]} roll is :', value=f'{d_mod}{d_10}')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)
  
  elif arg_str == dice[5]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'Your {dice[5]} roll is :', value=f'{random.randint(1, 12)}')
    
    await ctx.send(f'<@{name}>')
    await ctx.send(embed=embed_6)
  
  elif arg_str == dice[6]:
    #embed_6.set_thumbnail(url='')
    embed_6.add_field(name=f'Your {dice[6]} roll is :', value=f'{random.randint(1, 20)}')
    
    
    await ctx.send(embed=embed_6)

  else:
    await ctx.send(f'<@{name}>\n```CSS\nAre yous seriously that fucking retarded? -,..,-\"```')



@Aeon.command(name="--roll=")
async def roll_multi(ctx, arg_str_1, arg_str_2):
  """roll several of a specified die type [num][die type] - max 20 dice"""
  if arg_str_1.isnumeric() is True:
    if int(arg_str_1) <= 20:
      for count in range(int(arg_str_1)):
        await roll_dice(ctx, arg_str_2)
  
  else:
    await ctx.send(f'```CSS\nHoly FUCK, you\'re dumb! -,..,-\"```')


@Aeon.command(name="--fizz-buzz=")
async def aeons_fizzbuzzer(ctx, arg_str):
  """'fizz-buzz' up to 100 times"""
  FIZ = "Fizz"
  BUZ = "Buzz"
  MIN = 0
  MAX = 100
  X = 3
  Y = 5
  Z = 15
  id = str(ctx.author.id)
  
  if id == MY_ID():
    if arg_str.isnumeric() is True:
      if int(arg_str) <= MAX:
        for count in range(MIN, int(arg_str)):
          for number in range(MIN, MAX):
            if modulo(number, Z) is MIN:
               await ctx.send(f"```py\n\"{FIZ + BUZ}\"```")

            elif modulo(number, Y) is MIN:
              await ctx.send(f'```py\n\"{BUZ}\"```')
          
            elif modulo(number, X) is MIN:
              await ctx.send(f'```py\n\"{FIZ}\"```')

            else:
              await ctx.send(f'```py\n{number}```')
      
      else:
          await ctx.send(f'```CSS\n{arg_str} is waaay too fucking high of a number, you cunt e,..,0')
          print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to overset : --fizz-buzz=\nWith value : {arg_str}\nOperation aborted, wanrning sent to dad')
    
    else:
      await ctx.send(f'```CSS\n{arg_str} ain\'t even numeric, you fucking slowtard bitch! e,..,e')
      print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to input a non numeric string to : --fizz-buzz=\nWith value : {arg_str}\nOperation aborted, wanrning sent to dad')
  
  else:
    await ctx.send(f'```CSS\n{ctx.author.name}, you are NOT my father, you CANT TELL ME TO DO THAT SHIT YOU PANSY RETARD CUNT! E,..,E\n Im telling dad on you!```')
    print(f'User : {ctx.author.name}\nID : {ctx.author.id}\n This user just tried to activate : --fizz-buzz=\nWith value : {arg_str}\nOperation aborted, wanrning sent to dad')


@Aeon.command(name='--info')
async def aeon_info(ctx : commands.Context):
  await ctx.send(f'```css\nAeon is an expiramental discord bot created by Fluffykins.\nIt is capable of a great many things, most of which are only accessable by the\nbot\'s creator, due the nature of the functions.\n\nHowever, useful features, such as\n\"memeing\", playing music, and rolling dice. For mods/admins, kicking/banning users is\nalso possible with this bot, but these features are restricted to use only by Fluffykins\nat this moment in time. Enjoy Aeon\'s psychotic wirdness! ^,..,^```')

@Aeon.command(name='--rand=')
async def rand_hex(ctx, base = 'dec', str_cnt = 1, str_len = 2):
  """generate random hexadecimal numbers"""
  
  for count in range(0, int(str_cnt)):
    result = RNG.generate(base, str_len)
    
    if base == 'hex':
      await ctx.send(f'```java\nYour numerical string is :\n0x{result.upper()}```')
     
    else:
      await ctx.send(f'```java\nYour numerical string is :\n{result}```')


@Aeon.command(name='--amd-cpu-tutorial')
async def amd_cpu_tutorial(ctx):
  """how to modify an intel mobo to take an amd cpu"""
  
  await ctx.send('https://unixism.xyz/share/amd_guide.mp4')


Aeon.run(AEON_TOKEN)
