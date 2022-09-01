import discord
import random
import asyncio
import os
from discord.ext import commands, tasks
from itertools import cycle


intents = discord.Intents.default()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("The BOT game"))
    # change_status.start()
    print("Bot is ready ")


@client.command()
async def hii(ctx):
    await ctx.send("Hello")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')


@client.command()
async def Heyy(ctx, member: discord.Member):
    await ctx.send(f'Have a Good Day {member.mention}')


@client.command()
async def hello(ctx):
    await ctx.author.send(f'Hello {ctx.author.mention}')


@client.command()
async def hellio(ctx, message):
    await ctx.author.send(f'{message}')


@client.command()
async def greet(ctx, greeting, *, name):
    await ctx.send(f"{greeting}, {name}")


@client.command()
async def nick(ctx, member: discord.Member, newname: str):
    perms = ctx.channel.permissions_for(ctx.author)
    if perms.manage_nicknames:
        await member.edit(nick=newname)
    else:
        await ctx.send("Don't  have necessary permissions")


@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"{amount} message cleared sucessfully")

# @clear.error
# async def clear_error(ctx,error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please specify number of messages to delete')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked out {member.mention}')


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.display_name}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# status=cycle(["Status 1","Status 2"])
# @tasks.loop(seconds=10)
# async def change_status():
#     await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    await client.get_channel(848832825783353394).send(f"{member.mention} has joined!")


@client.event
async def on_member_remove(member):
    await client.get_channel(848832825783353394).send(f"I hope {member} had fun!")


@client.command()
async def test(ctx, member: discord.Member):
    await ctx.send(member.display_name)


@client.command()
async def role(ctx, member: discord.Member, role: discord.Role):
    # Give the mentioned person a role
    await member.add_roles(role)


@client.event
async def on_message(message):
    if 'https://' in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Don't send links!")


client.run('ODQ4ODMyODI1NzgzMzUzMzk0.YLSXLA.58Vy3LQokB7jb1-Ow2_CM_haHNQ')
