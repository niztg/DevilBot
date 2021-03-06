from discord.ext import commands
import discord, wikipedia
import json
import traceback

class eventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_conn = bot.db_conn

        self.colour = 0xff9300
        self.footer = 'Bot developed by DevilJamJar#0001\nWith a lot of help from ♿nizcomix#7532'
        self.thumb = 'https://styles.redditmedia.com/t5_3el0q/styles/communityIcon_iag4ayvh1eq41.jpg'

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = 'ow!'

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        a = sorted([c for c in guild.text_channels if c.permissions_for(guild.me).send_messages],
                   key=lambda x: x.position)
        channel = a[0]
        inv = await channel.create_invite()
        finalinv = f"https://discord.gg/{inv.code}"

        c = self.bot.get_channel(715744000077725769)

        embed = discord.Embed(colour=0xff9300, title=f'{guild}',
                              description=f"**{guild.id}**\n**{finalinv}**")
        embed.set_thumbnail(url=guild.icon_url)
        await c.send(f"<@!670564722218762240> We joined guild **#{len(self.bot.guilds)}**", embed=embed)

    @commands.Cog.listener(name="on_message")
    async def on_user_mention(self, message):
        if message.content in ("<@!720229743974285312>", "<@720229743974285312>"):
            guildpre = await self.bot.get_prefix(message)
            guildpre = f'{guildpre[2]}'
            appinfo = await self.bot.application_info()
            _commands = []
            for c in self.bot.commands:
                if c.enabled == True:
                    _commands.append(c.name)
            if len(_commands) == len(self.bot.commands):
                currentstatus = f'<:status_online:596576749790429200> `Status:` The Bot is currently **active.**'
            else:
                currentstatus = f'<:status_dnd:596576774364856321> `Status:` The Bot is currently **undergoing maintenance.**'
            embed = discord.Embed(colour=self.colour,
                                  title=f"{appinfo.name} | {appinfo.id}",
                                  description=f":diamond_shape_with_a_dot_inside: `Guild Prefix:` **{guildpre}**\
                                              \n<:owner:730864906429136907> `Owner:` **<@!{appinfo.owner.id}>**\
                                              \n<:text_channel:703726554018086912> `Description:` **{appinfo.description}**\
                                              \n{currentstatus}\
                                              \n\n**Do** `{guildpre}help` **to view a full command list.**\
                                              \n**Do** `{guildpre}help [command]` **to view specific command help.**")
            embed.set_thumbnail(url=self.thumb)
            embed.set_author(name=f'Requested by {message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        # Please ignore this, it's horribly made and only made for a proof of concept, imagine it doesn't exist

        em=discord.Embed(colour=self.colour,
                 title=f'You may have been mentioned in: {message.guild.name}',
                 description=f'`Author:` {message.author.mention}\
                 \n\n`Message:` {message.content}\
                 \n\n`Created At:` {message.created_at}\
                 \n\n**[Jump]({message.jump_url})**')

        if 'devil' in message.content.lower().replace(' ', '').replace('\n', ''):
            owner = self.bot.get_user(670564722218762240)
            if message.author.id != 720229743974285312 and message.author != owner:
                await owner.send(embed=em)
        if 'freagl' in message.content.lower().replace(' ', '').replace('\n', '') or 'petrick' in message.content.lower().replace(' ', '').replace('\n', ''):
            freaglii = self.bot.get_user(370633705091497985)
            if message.author != freaglii:
                await freaglii.send(embed=em)
        if 'chill' in message.content.lower().replace(' ', '').replace('\n', ''):
            chill = self.bot.get_user(689912112386277384)
            if message.author != chill:
                await chill.send(embed=em)
        if 'blitz' in message.content.lower().replace(' ', '').replace('\n', ''):
            blitz = self.bot.get_user(239516219445608449)
            if message.author != blitz:
                await blitz.send(embed=em)
        if 'para ' in message.content.lower():
            para = self.bot.get_user(596079424680493096)
            if message.author.id != 720229743974285312 and message.author != para:
                await para.send(embed=em)
        if 'asti ' in message.content.lower() or 'mos ' in message.content.lower():
            asti = self.bot.get_user(517067779145334795)
            if message.author.id != 720229743974285312:
                if message.guild.id == 621044091056029696:
                    if message.author != asti:
                        await asti.send(embed=em)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        _raise = [
            commands.CheckFailure,
            commands.NotOwner,
            wikipedia.DisambiguationError,
            commands.MissingRequiredArgument
        ]

        skip = [
            commands.CommandNotFound
        ]

        disabled = [
            commands.DisabledCommand
        ]

        if type(error) in skip:
            return
        elif type(error) in _raise:
            return await ctx.send(f'<@!{ctx.author.id}>, something went wrong that I was expecting.\n`{error}`')
        elif type(error) in disabled:
            return await ctx.send(f':warning: <@!{ctx.author.id}> The bot is currently in `maintenance mode.`\nThis means I\'m working on fixing bugs or imperfections and don\'t want you breaking anything. Please be patient.')
        else:
            print(f'An uncaught error occured during the handling of a command, {type(error)} » {error}')
            return await ctx.send(f'<@!{ctx.author.id}>, something went wrong that I wasn\'t expecting.\n`{error}`')

def setup(bot):
    bot.add_cog(eventsCog(bot))
