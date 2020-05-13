import discord
import slurcheck
import ryeng
import ryeng_embed
import ryeng_messaging
import ryeng_resources
import ryeng_rolerequest

TOKEN = 'blank'
client = discord.Client()


@client.event
async def on_message(message):
    #######################################################################################
    if(not(isinstance(message.channel, discord.DMChannel))):
        if(message.content.startswith('!rr')):
            try:
                guild = message.guild
                mod_ch = await ryeng.get_moderators_channel(client)
                rr_ch = await ryeng.get_rolerequests_channel(client)
                member = message.guild.get_member(message.author.id)

                await message.delete()
                await ryeng_rolerequest.remove_all_roles(member)
                await ryeng_rolerequest.function(client, guild, mod_ch, rr_ch, member)

                return
            except Exception as err:
                print('rams.py !rr')
                print(err)
                return

#######################################################################################
    if(isinstance(message.channel, discord.DMChannel)):
        if(message.content.startswith('!sm')):
            try:
                mod_ch = await ryeng.get_moderators_channel(client)
                await ryeng_messaging.user_mode(client, mod_ch, message)
                return
            except Exception as err:
                print('rams.py user !sm')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!help')):
            try:
                await message.channel.send(embed=await ryeng_embed.on_help(client))
                return
            except Exception as err:
                print('rams.py user !help')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!post')):
            try:
                guild = await ryeng.get_ryeng_server(client)
                log_ch = await ryeng.get_logs_channel(client)
                await ryeng_resources.send(guild, log_ch, message)
                return
            except Exception as err:
                print('rams.py !post')
                print(err)
                return

        return

#######################################################################################
    if(message.channel.name == 'moderators'):
        if(message.content.startswith('!sm')):
            try:
                mod_ch = await ryeng.get_moderators_channel(client)
                await ryeng_messaging.admin_mode(client, mod_ch, message)
            except Exception as err:
                print('rams.py admin !sm\n')
                print(err)
                return

        elif(message.content.startswith('!help')):
            try:
                await message.channel.send(embed=await ryeng_embed.on_admin_help(client))
                return
            except Exception as err:
                print('rams.py admin !help')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!changenick')):
            try:
                member = message.guild.get_member(int(message.content[12:30]))
                old_nick = member.display_name
                new_nick = str(message.content[31:])
            except Exception as err:
                print('rams.py admin !changenick Try Except block 1')
                print(err)
                return

            if message == None or member == None or old_nick == new_nick:
                return

            for admin in message.channel.members:
                if member.id == admin.id:
                    return

            try:
                await member.edit(nick=new_nick, reason=None)
            except Exception as err:
                print('rams.py admin !changenick Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.on_nick_change(message.author, member, old_nick, new_nick))
                return
            except Exception as err:
                print('rams.py admin !changenick Try Except block 3')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!mute')):
            try:
                member = message.guild.get_member(int(message.content[5:]))
            except Exception as err:
                print('rams.py admin !mute Try Except block 1')
                print(err)
                return

            if message == None or member == None:
                return

            for admin in message.channel.members:
                if member.id == admin.id:
                    return

            for role in member.roles:
                if role.name == 'Muted' or role.name == 'Role Request In Progress':
                    await message.channel.send('The member is already muted or there is a role request in progress.')
                    return

            try:
                for role in member.roles:
                    if role.name != '@everyone' and role.id != 639226974044291102:
                        await member.remove_roles(role, reason=None, atomic=True)

                for role in member.guild.roles:
                    if role.name == 'Muted':
                        await member.add_roles(role, reason=None, atomic=True)
            except:
                print('rams.py admin !mute Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.on_mute(message.author, member))
                return
            except Exception as err:
                print('rams.py admin !mute Try Except block 3')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!unmute')):
            try:
                server = message.guild
                mod_ch = await ryeng.get_moderators_channel(client)
                rr_ch = await ryeng.get_rolerequests_channel(client)
                member = message.guild.get_member(int(message.content[7:]))
            except Exception as err:
                print('rams.py admin !unmute Try Except block 1')
                print(err)
                return

            if message == None or member == None or server == None:
                return
            try:
                mute_role = None
                for role in member.roles:
                    if role.name == 'Muted':
                        mute_role = role

                if mute_role == None:
                    return

                await member.remove_roles(mute_role, reason=None, atomic=True)
            except Exception as err:
                print('rams.py admin !unmute Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.on_unmute(message.author, member))
                await ryeng_rolerequest.function(client, server, mod_ch, rr_ch, member)
                return
            except Exception as err:
                print('rams.py admin !unmute Try Except block 3')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!purge')):
            try:
                target = client.get_channel(int(message.content[7:25]))
                amount = int(message.content[26:])
            except Exception as err:
                print('rams.py admin !purge Try Except block 1')
                print(err)
                return

            if message == None or target == None or amount == None:
                return

            try:
                await target.purge(limit=amount + 1)
            except Exception as err:
                print('rams.py admin !purge Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.on_purge(message.author, target, amount))
                return
            except Exception as err:
                print('rams.py admin !purge Try Except block 3')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!kick')):
            try:
                member = message.guild.get_member(int(message.content[5:]))
            except Exception as err:
                print('rams.py admin !kick Try Except block 1')
                print(err)
                return

            if message == None or member == None:
                return

            for admin in message.channel.members:
                if member.id == admin.id:
                    return

            try:
                for role in member.roles:
                    if role.name == 'Role Request In Progress':
                        await message.channel.send('The member has a role request in progress.')
                        return

                await message.guild.kick(member, reason=None)
            except Exception as err:
                print('rams.py admin !kick Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.member_kick(message.author, member))
                return
            except Exception as err:
                print('rams.py admin !kick Try Except block 2')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!ban')):
            try:
                user = client.get_user(int(message.content[4:]))
            except Exception as err:
                print('rams.py admin !ban Try Except block 1')
                print(err)
                return

            # If no user is found return
            if message == None or user == None:
                return

            for admin in message.channel.members:
                if user.id == admin.id:
                    return

            for ban in await message.guild.bans():
                if ban.user.id == user.id:
                    return

            try:
                for role in member.roles:
                    if role.name == 'Role Request In Progress':
                        await message.channel.send('The member has a role request in progress.')
                        return

                await message.guild.ban(user, reason=None, delete_message_days=0)
            except:
                print('rams.py admin !ban Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.member_ban(message.author, user))
                return
            except Exception as err:
                print('rams.py admin !ban Try Except block 3')
                print(err)
                return

#######################################################################################
        elif(message.content.startswith('!unban')):
            try:
                user = client.get_user(int(message.content[6:]))
            except Exception as err:
                print('rams.py admin !unban Try Except block 1')
                print(err)
                return

            if message == None or user == None:
                return

            try:
                for ban in await message.guild.bans():
                    if ban.user.id == user.id:
                        await message.guild.unban(user)
                        break
            except Exception as err:
                print('rams.py admin !unban Try Except block 2')
                print(err)
                return

            try:
                log_ch = await ryeng.get_logs_channel(client)
                if log_ch == None:
                    return

                await log_ch.send(embed=await ryeng_embed.member_unban(message.author, user))
                return
            except Exception as err:
                print('rams.py admin !unban Try Except block 3')
                print(err)
                return

    await slurcheck.check(message)


@client.event
async def on_member_join(member):
    try:
        mod_ch = await ryeng.get_moderators_channel(client)
        rr_ch = await ryeng.get_rolerequests_channel(client)
        log_ch = await ryeng.get_logs_channel(client)

        if mod_ch == None or rr_ch == None or log_ch == None:
            return

        await log_ch.send(embed=await ryeng_embed.new_member(member))
        await ryeng_rolerequest.function(client, member.guild, mod_ch, rr_ch, member)
        return
    except Exception as err:
        print('rams.py on_member_join(member)')
        print(err)
        return


@client.event
async def on_member_remove(member):
    try:
        log_ch = await ryeng.get_logs_channel(client)
        if log_ch == None:
            return
        await log_ch.send(embed=await ryeng_embed.member_left(member))
        return
    except Exception as err:
        print('rams.py on_member_remove(member)')
        print(err)
        return


@client.event
async def on_message_edit(before, after):
    try:
        if(after.guild.name != 'RyEng'):
            return
    except:
        return

    try:
        log_ch = await ryeng.get_logs_channel(client)
        if log_ch == None:
            return

        if (before.content == after.content):
            return

        await slurcheck.check(after)
        await log_ch.send(embed=await ryeng_embed.on_edit(before, after))
        return
    except Exception as err:
        print('rams.py on_message_edit(before, after)')
        print(err)
        return


@client.event
async def on_message_delete(message):
    try:
        if(message.guild.name != 'RyEng') or message.embeds != []:
            return
    except:
        return

    try:
        log_ch = await ryeng.get_logs_channel(client)
        if log_ch == None:
            return

        await log_ch.send(embed=await ryeng_embed.on_delete(message))
    except Exception as err:
        print('rams.py on_message_delete(message)')
        print(err)
        return


@client.event
async def on_ready():
    print('LOGGED ON: ' + str(client.user.name) + '\nID: ' + str(client.user.id))


client.run(TOKEN)
