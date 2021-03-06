
import datetime
import subprocess
import uuid

import discord
from discord.ext import commands

from ..bot import EXTENSIONS
from ..storage import Storage


class Developer(commands.Cog):
    @commands.command(help='Load an extension by it\'s module path.')
    @commands.is_owner()
    async def dev_load(self, ctx: commands.Context, name: str):
        ctx.bot.load_extension(name)
        EXTENSIONS.append(name)
        await ctx.send(embed=discord.Embed(
            description=f':ok_hand: Loaded `{name}`',
            color=ctx.bot.colorsg['success']
        ).set_footer(
                text=f'Requested by {ctx.author}',
                icon_url=ctx.author.avatar_url
            ))

    @commands.command(help='Unload an extension by it\'s module path.')
    @commands.is_owner()
    async def dev_unload(self, ctx: commands.Context, name: str):
        ctx.bot.unload_extension(name)
        await ctx.send(embed=discord.Embed(
            description=f':ok_hand: Unloaded `{name}`',
            color=ctx.bot.colorsg['success']
        ).set_footer(
                text=f'Requested by {ctx.author}',
                icon_url=ctx.author.avatar_url
            ))

    @commands.command(help='Reload all extension or one specified by it\'s '
                           'module path.')
    @commands.is_owner()
    async def dev_reload(self, ctx: commands.Context, name: str = None):
        if name is None:
            exts = EXTENSIONS
        else:
            exts = [name]
        for extension in exts:
            ctx.bot.reload_extension(extension)
        await ctx.send(embed=discord.Embed(
            description=f':ok_hand: Reloaded {len(exts)} '
                        f'extension(s).',
            color=ctx.bot.colorsg['success']
        ).set_footer(
                text=f'Requested by {ctx.author}',
                icon_url=ctx.author.avatar_url
            ))

    @commands.command(help='Ping')
    @commands.is_owner()
    async def dev_ping(self, ctx: commands.Context):
        sent = datetime.datetime.utcnow()
        ws_latency = ctx.bot.latency * 1000

        msg = await ctx.send(embed=discord.Embed(
            description=f'Websocket latency: **{ws_latency:.2f}ms**\n'
                        f'API latency: *fetching*',
            color=ctx.bot.colorsg['success']
        ))
        api_latency = (msg.created_at - sent).total_seconds() * 1000
        await msg.edit(embed=discord.Embed(
            description=(
                f'Websocket latency: **{ws_latency:.2f}ms**\n'
                f'API latency: **{api_latency:.2f}ms**'
            ),
            color=ctx.bot.colorsg['success']
        ))

    @commands.command(help='Creates a gift uuid that can be redeemed')
    @commands.is_owner()
    async def dev_gengift(self, ctx: commands.Context, product_id: str):
        storage = ctx.bot.get_storage(ctx.guild)  # type: Storage
        gift = uuid.uuid4()
        await storage[0].set(f'premium-gift:{gift}', product_id)
        return await ctx.send(embed=discord.Embed(
            description=f'UUID: `{gift}`',
            color=ctx.bot.colorsg['success']
        ))

    @commands.command(help='Updates the bot')
    @commands.is_owner()
    async def dev_update(self, ctx: commands.Context):
        await ctx.send('Pulling from git')
        subprocess.call(['git', 'pull'])  # pull updates from github
        await ctx.send('Alright, restarting :)')
        ctx.bot.restart = True
        await ctx.bot.close()

    @commands.command(help='Bans a server from using the bot')
    @commands.is_owner()
    async def dev_ban(self, ctx: commands.Context, guildid: int, *,
                      reason: str):
        storage = ctx.bot.storage / 'guild' / guildid  # type: Storage
        await storage.set('ban', reason)
        await ctx.send(embed=discord.Embed(
            description='Guild has been banned from using the bot.',
            color=ctx.bot.colorsg['success']
        ))

    @commands.command(help='Allows a server to use the bot again')
    @commands.is_owner()
    async def dev_unban(self, ctx: commands.Context, guildid: int):
        storage = ctx.bot.storage / 'guild' / guildid  # type: Storage
        await storage.delete('ban')
        await ctx.send(embed=discord.Embed(
            description='Guild can now use the bot again.',
            color=ctx.bot.colorsg['success']
        ))

    @commands.command(help='Bot leaves the server')
    @commands.is_owner()
    async def dev_leave(self, ctx: commands.Context, guildid: int):
        guild = ctx.bot.get_guild(guildid)
        if guild is None:
            return await ctx.send(embed=discord.Embed(
                description='Guild not found',
                color=ctx.bot.colorsg['failure']
            ))
        await guild.leave()
        await ctx.send(embed=discord.Embed(
            description='Bot left the guild.',
            color=ctx.bot.colorsg['success']
        ))


def setup(bot: commands.Bot):
    bot.add_cog(Developer())
