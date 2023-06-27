import discord
from discord.ext import commands
import pykeygen
import datashredder
bot_key = open("discordkey.key","r").read()
bot = commands.Bot(command_prefix="!",help_command=None)

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def help(message):
    embed=discord.Embed(title="Help")
    embed.set_thumbnail(url="https://img.icons8.com/fluency/144/000000/help.png")
    embed.add_field(name="Commands", value="`help` `corrupt_cat` `generate`", inline=False)
    await message.send(embed=embed)

@bot.command()
async def corrupt_cat(message):
    datashredder.corrupt("cat_images/cat.jpg","server_storage/output.jpg")
    embed=discord.Embed(title="Datashredder job complete", description="The corrupted image will be attached as `output.jpg`")
    embed.set_thumbnail(url="https://img.icons8.com/fluency/144/000000/ok.png")
    await message.send(embed=embed)
    await message.send(file=discord.File("server_storage/output.jpg"))


@bot.command()
async def generate(message, arg1):
    if int(arg1) > 500:
        embed=discord.Embed(title="Error", color=0xff0000)
        embed.set_thumbnail(url="https://img.icons8.com/fluency/144/000000/cancel.png")
        embed.add_field(name="Message", value="Argument is too big maximum size is 500", inline=False)
        embed.set_footer(text="Bot Error")
        await message.send(embed=embed)
    else:
        embed=discord.Embed(title="PyKeyGen")
        embed.set_thumbnail(url="https://img.icons8.com/fluency/144/000000/key-security.png")
        embed.add_field(name="Here is your generated key", value=pykeygen.generate_key(int(arg1)), inline=True)
        await message.send(embed=embed)

@bot.event
async def on_command_error(message, error):
  
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Error", color=0xff0000)
        embed.set_thumbnail(url="https://img.icons8.com/fluency/144/000000/cancel.png")
        embed.add_field(name="Message", value="Missing arguments in command", inline=False)
        embed.set_footer(text="Dicord.py Error")
        await message.send(embed=embed)

bot.run(bot_key)