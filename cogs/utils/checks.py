from discord.ext import commands

'''
Copyright (c) 2020 nizcomix
https://github.com/niztg/CyberTron5000
under the terms of the  MIT LICENSE
'''

def check_admin_or_owner():
    def predicate(ctx):
        if ctx.message.author.id == 670564722218762240:
            return True
        elif ctx.message.author.permissions_in(channel=ctx.message.channel).administrator:
            return True
        else:
            return False
    
    return commands.check(predicate)

def check_mod_server():
    def predicate(ctx):
        if ctx.message.author.id == 670564722218762240:
            return True
        elif ctx.message.guild.id == 292932955653931009:
            return True
        else:
            return False
    
    return commands.check(predicate)