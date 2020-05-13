import discord
import datetime

# 0x00FFC8 Bright Turquoise (On Member Join)
# 0xFF0055 Bright Red (On Member Leave)
# 0x9900FF Electric Purple (Delete/Edit Message)
# 0x8AFF00 Chartreuse (Nickname Change)
# 0x008080 RyEng Blue (Resource Post)
embedColours = [0x00FFC8, 0xFF0055, 0x9900FF, 0x8AF00, 0x2F67D6, 0xFF0000]


async def new_member(member):
    t = datetime.datetime.now()
    e = discord.Embed(title='New Member Joined',
                      description='**User: **' + str(member) + '\n**Mention: **' + member.mention +
                      '\n**ID: **' + str(member.id),
                      color=embedColours[0])
    e.set_thumbnail(url=member.avatar_url)
    e.set_footer(text=str(t.strftime('%Y-%m-%d %H:%M')))
    return e


async def role_request(message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Role Request #' + str(message.id)[14:19],
                      description='**User: **' + str(message.author) + '\n**Mention: **' + message.author.mention +
                      '\n**ID: **' + str(message.author.id),
                      color=embedColours[0])
    e.set_thumbnail(url=message.author.avatar_url)
    e.add_field(name='**Contents**',
                value=message.content.replace('!rr ', ''),
                inline=False)
    e.set_footer(text=str(t.strftime('%Y-%m-%d %H:%M')))
    return e


async def role_request_successful(message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Role Request #' + str(message.id)[14:19] + ' Confirmation',
                      color=embedColours[0])
    e.add_field(name='**Contents**',
                value='Role request was successful.', inline=False)
    e.set_footer(text=str(t.strftime('%Y-%m-%d %H:%M')))
    return e


async def role_request_unsuccessful(message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Role Request #' + str(message.id)[14:19] + ' Confirmation',
                      color=embedColours[1])
    e.add_field(name='**Contents**',
                value='Role request was not successful. Member might have left during the process.', inline=False)
    e.set_footer(text=str(t.strftime('%Y-%m-%d %H:%M')))
    return e


async def member_left(member):
    t = datetime.datetime.now()
    e = discord.Embed(title='Member Left',
                      description='**User: **' + str(member) +
                      "\n**ID: **" + str(member.id),
                      color=embedColours[1])
    e.set_thumbnail(url=member.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def member_ban(moderator, user):
    t = datetime.datetime.now()
    e = discord.Embed(title='User Banned',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**User: **' + user.name + '#' + user.discriminator +
                      '\n**ID: **' + str(user.id),
                      color=embedColours[1])
    e.set_thumbnail(url=user.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def member_unban(moderator, user):
    t = datetime.datetime.now()
    e = discord.Embed(title='User Unbanned',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**User: **' + user.name + '#' + user.discriminator +
                      '\n**ID: **' + str(user.id),
                      color=embedColours[0])
    e.set_thumbnail(url=user.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_purge(moderator, channel, amount):
    t = datetime.datetime.now()
    e = discord.Embed(title='Channel Purged',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**Target Channel: **' + channel.mention +
                      '\n**Channel ID: **' + str(channel.id) +
                      '\n**Amount: **' + str(amount),
                      color=embedColours[2])
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def member_kick(moderator, member):
    t = datetime.datetime.now()
    e = discord.Embed(title='Member Kicked',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**User: **' + str(member) +
                      '\n**ID: **' + str(member.id),
                      color=embedColours[1])
    e.set_thumbnail(url=member.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_mute(moderator, member):
    t = datetime.datetime.now()
    e = discord.Embed(title='Member Muted',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**User: **' + str(member) +
                      '\n**Mention: **' + member.mention +
                      '\n**ID: **' + str(member.id),
                      color=embedColours[1])
    e.set_thumbnail(url=member.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_unmute(moderator, member):
    t = datetime.datetime.now()
    e = discord.Embed(title='Member Unuted',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**User: **' + str(member) +
                      '\n**Mention: **' + member.mention +
                      '\n**ID: **' + str(member.id),
                      color=embedColours[0])
    e.set_thumbnail(url=member.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_nick_change(moderator, member, old, new):
    t = datetime.datetime.now()
    e = discord.Embed(title='Forced Nickname Change',
                      description='**Moderator: **' + moderator.mention +
                      '\n**Moderator ID: **' + str(moderator.id) +
                      '\n**User: **' + str(member) +
                      '\n**Mention: **' + member.mention +
                      '\n**ID: **' + str(member.id) +
                      '\n**Old Nick: **' + old +
                      '\n**New Nick: **' + new,
                      color=embedColours[2])
    e.set_thumbnail(url=member.avatar_url)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def user_message(message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Member Message #' + str(message.id)[14:18],
                      description='**User: **' + str(message.author) +
                      "\n**Mention: **" + message.author.mention +
                      "\n**ID: **" + str(message.author.id),
                      color=embedColours[4])
    e.set_thumbnail(url=message.author.avatar_url)
    e.add_field(name='**Contents**',
                value=message.content.replace('!sm ', ''),
                inline=False)
    e.set_footer(text='User: ' + str(message.author) + '  |  ' +
                 str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def admin_reply(msg_id, message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Admin Reply #' + msg_id,
                      color=embedColours[4])
    e.add_field(name='**Contents**',
                value=message.content[12:],
                inline=False)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def admin_message(message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Admin Message #' + str(message.id)[14:18],
                      color=embedColours[4])
    e.add_field(name='**Contents**',
                value=message.content[23:] + '\n\n**Reply by doing !reply ' + str(message.id)[14:18] + ' <message>**', inline=False)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def user_reply(msg_id, message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Member Reply #' + msg_id,
                      color=embedColours[4])
    e.set_thumbnail(url=message.author.avatar_url)
    e.add_field(name='**Contents**',
                value=message.content[12:],
                inline=False)
    e.set_footer(text='User: ' + str(message.author) + '  |  ' +
                 str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_resource_post(message, channel):
    t = datetime.datetime.now()

    temp = ""
    for attachment in message.attachments:
        temp += attachment.url + "\n"

    e = discord.Embed(title='Resource Posted',
                      description='**User: **' + str(message.author) +
                      '\n**User Mention: **' + message.author.mention +
                      '\n**User ID: **' + str(message.author.id) +
                      '\n**Channel: **' + channel.mention +
                      '\n**Channel ID: **'+str(channel.id),
                      color=embedColours[4])
    e.set_thumbnail(url=message.author.avatar_url)
    e.add_field(name='**Contents**',
                value=message.content[7:] + "\n" + temp,
                inline=False)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_edit(before, after):
    t = datetime.datetime.now()
    e = discord.Embed(title='Edited Message',
                      description='**User: **' + str(before.author) +
                      '\n**User Mention: **' + before.author.mention +
                      '\n**User ID: **' + str(before.author.id) +
                      '\n**Channel: **' + before.channel.mention +
                      '\n**Channel ID: **'+str(before.channel.id),
                      color=embedColours[2])
    e.set_thumbnail(url=before.author.avatar_url)
    e.add_field(name='**Before**', value=before.content, inline=False)
    e.add_field(name='**After**', value=after.content, inline=False)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_delete(message):
    t = datetime.datetime.now()
    e = discord.Embed(title='Deleted Message',
                      description='**User: **' + str(message.author) +
                      '\n**User Mention: **' + message.author.mention +
                      '\n**User ID: **' + str(message.author.id) +
                      '\n**Channel: **' + message.channel.mention +
                      '\n**Channel ID: **'+str(message.channel.id),
                      color=embedColours[2])
    e.set_thumbnail(url=message.author.avatar_url)
    e.add_field(name='**Contents**',
                value=message.content, inline=False)
    e.set_footer(text=str(t.strftime("%Y-%m-%d %H:%M")))
    return e


async def on_help(client):
    e = discord.Embed(title='Commands', color=0x2F67D6)
    e.set_thumbnail(url=client.get_guild(
        365554916451811341).icon_url)
    e.add_field(name='Command Information',
                value='\n**!help** - lists the commands of this bot\n' +
                '\n**!sm <CONTENTS>** - Sends a message to the admins; the admins can reply back\n' +
                '\n**!rr** - Request a role or modification in your roles. Can be called in any text channel of the server\n' +
                '\n**!post[X] <CONTENTS>** - Posts contents onto the resources channel anonymously for X = [0, 1, 2, 3, 4]',
                inline=False)
    return e


async def on_admin_help(client):
    e = discord.Embed(title='Commands', color=0x2F67D6)
    e.set_thumbnail(url=client.get_guild(
        365554916451811341).icon_url)
    e.add_field(name='Admin Command Information',
                value='\n**!help** - lists the commands of this bot\n' +
                '\n**!sm <ID> <CONTENTS>** - Sends a message to the admins; the admins can reply back\n' +
                '\n**!changenick <ID> <nickname>** - Force change the nickname of a member\n' +
                '\n**!mute <ID>** - Mutes a member; a member may not be muted during a role request\n' +
                '\n**!unmute <ID>** - Unmutes a member; a role request will automatically be called after\n' +
                '\n**!purge <ID> <Amount>** - Purges a channel\n' +
                '\n**!kick <ID>** - Kicks a member; a member may not be kicked during a role request\n' +
                '\n**!ban <ID>** - Bans a member; a member may not be banned during a role request\n',
                inline=False)
    return e
