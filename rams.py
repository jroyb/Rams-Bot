import discord
import random
import datetime

# COPYRIGHT 2019 198938374822821888 & 365621509450104851
# Designed and developed for the RyEng discord server.

TOKEN = ''

# RyEng Server ID
serverID = 365554916451811341

# this is for the ryEng discord, IDs for all the RESOURCE channels
resourceChannels = [
    642403508125040653, 642403533429145620, 642403557890588673,
    642403588970119208, 642403628530925578
]

admins = [
    198938374822821888, 365621509450104851, 295610195923697666,
    276844714844618772, 130400795668512768
]

# Other important channels on RyEng
serverLog = 484401067862392852
admin_inbox = 642345205705474059

# 0x00FFC8 Bright Turquoise (On Member Join)
# 0xFF0055 Bright Red (On Member Leave)
# 0x9900FF Electric Purple (Delete/Edit Message)
# 0x8AFF00 Chartreuse (Nickname Change)
# 0x008080 RyEng Blue (Resource Post)
embedColours = [0x00FFC8, 0xFF0055, 0x9900FF, 0x8AF00, 0x2F67D6]

client = discord.Client()


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Reads a message and runs any specified commands
#          called.
@client.event
async def on_message(message):
    if (isinstance(message.channel, discord.DMChannel)
            and message.content.startswith('!rolerequest')):
        await roleRequest(message)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!sendmessage')):
        await sendMessage(message)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!commands')):
        # Create an embed
        embed = discord.Embed(title='Commands', color=0x2F67D6)
        embed.set_thumbnail(url=client.get_guild(serverID).icon_url)
        embed.add_field(
            name='Command Information',
            value=
            '\n**!commands** - lists the commands of this bot\n\n**!sendmessage <ID>** - Target an admin to send a message to (e.g. !sendmessage 2339 then press enter); use !listadmin to get an ID\n\n**!rolerequest** - Request a role or modification in your roles\n\n**!post[X]y / !postOther** - Posts contents onto the resources channel anonymously for X = [1, 2, 3, 4]',
            inline=False)

        await message.channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post1y")):
        channel = client.get_channel(resourceChannels[0])
        await on_resource_send(message, message.channel, channel)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post2y")):
        channel = client.get_channel(resourceChannels[1])
        await on_resource_send(message, message.channel, channel)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post3y")):
        channel = client.get_channel(resourceChannels[2])
        await on_resource_send(message, message.channel, channel)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post4y")):
        channel = client.get_channel(resourceChannels[3])
        await on_resource_send(message, message.channel, channel)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!postOther")):
        channel = client.get_channel(resourceChannels[4])
        await on_other_resource_send(message, message.channel, channel)

    elif (message.content.startswith('!purge')):
        target = client.get_channel(int(message.content[7:26]))
        amount = int(message.content[26:])

        for admin in admins:
            if (admin == message.author.id):
                await target.purge(limit=amount + 1)
            return

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!")):
        await message.channel.send(
            'ValueError Exception: Invalid command.\n\n!commands to list commands'
        )

    # Auto delete message containing this word
    if ('nigger' in message.content.lower()):
        await message.delete()


# REQUIRES: A Message of type Discord.Message and two Channels
#           of type Discord.Channel
# EFFECTS: Sends an embed to the #server-log channel regarding
#          information on the resource posted.
async def on_resource_send(message, dm, channel):
    log = client.get_channel(serverLog)
    now = datetime.datetime.now()

    # Checks if the message has contents
    if (len(message.content) < 8):
        await message.channel.send(
            'There is no contents in your resource post. Please try again.')
        return

    if (message.content[7] != ' '):
        await message.channel.send(
            'Make sure there is a space inbetween the command and your message. Please try again.'
        )
        return

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Resource Posted',
                          description='**User: **' + message.author.mention +
                          '\n**Channel: **' + channel.mention,
                          color=embedColours[4])
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name='**Contents**',
                    value=message.content[7:],
                    inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    await channel.send(message.content[8:])

    # Send to #admin-inbox
    await log.send(embed=embed)
    # Send a verification to the member
    await dm.send('Resource has been posted.\n\n')
    await dm.send(embed=embed)


# REQUIRES: A Message of type Discord.Message and two Channels
#           of type Discord.Channel
# EFFECTS: Sends an embed to the #server-log channel regarding
#          information on the resource posted.
async def on_other_resource_send(message, dm, channel):
    log = client.get_channel(serverLog)
    now = datetime.datetime.now()

    # Checks if the message has contents
    if (len(message.content) < 11):
        await message.channel.send(
            'There is no contents in your resource post. Please try again.')
        return

    if (message.content[10] != ' '):
        await message.channel.send(
            'Make sure there is a space inbetween the command and your message. Please try again.'
        )
        return

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Resource Posted',
                          description='**User: **' + message.author.mention +
                          '\n**Channel: **' + channel.mention,
                          color=embedColours[4])
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name='**Contents**',
                    value=message.content[10:],
                    inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    await channel.send(message.content[8:])

    # Send to #admin-inbox
    await log.send(embed=embed)
    # Send a verification to the member
    await dm.send('Resource has been posted.\n\n')
    await dm.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs the edited message in the #server-log channel
@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(serverLog)
    if (before.content == after.content):
        return

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Edited Message',
                          description='**User: **' + before.author.mention +
                          '\n**Channel: **' + before.channel.mention,
                          color=embedColours[2])
    embed.set_thumbnail(url=before.author.avatar_url)
    embed.add_field(name='**Before**', value=before.content, inline=False)
    embed.add_field(name='**After**', value=after.content, inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs the deleted message in the #server-log channel
@client.event
async def on_message_delete(message):
    channel = client.get_channel(serverLog)

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Deleted Message',
                          description='**User: **' + message.author.mention +
                          '\n**Channel: **' + message.channel.mention,
                          color=embedColours[2])
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name='**Contents**', value=message.content, inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs a nickname change in the #server-log channel
@client.event
async def on_member_update(before, after):
    if (before.nick != after.nick):
        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        ############################################################################
        embed = discord.Embed(title='Nickname Change',
                              description='**User: **' + before.mention,
                              color=embedColours[3])
        embed.set_thumbnail(url=before.avatar_url)
        embed.add_field(name='**Before**',
                        value=str(before.nick),
                        inline=False)
        embed.add_field(name='**After**', value=str(after.nick), inline=False)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
        ############################################################################

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Sends a message from a server member to #admin-inbox.
#          Admins can then reply once to the specified message
async def sendMessage(message):
    channel = client.get_channel(admin_inbox)

    # Checks if the message has contents
    if (len(message.content) < 13):
        await message.channel.send(
            'There is no contents in your message. Please try again.')
        return

    if (message.content[12] != ' '):
        await message.channel.send(
            'Make sure there is a space inbetween the command and your message. Please try again.'
        )
        return

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Message #' + str(message.id)[14:19],
                          color=embedColours[4])
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name='**Contents**',
                    value=message.content.replace('!sendmessage ', ''),
                    inline=False)
    embed.set_footer(text='User: ' + str(message.author) + '  |  ' +
                     str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    # Send to #admin-inbox
    await channel.send(embed=embed)
    # Send a verification to member
    await message.channel.send('Message has been sent.\n')
    await message.channel.send(embed=embed)

    # Checks that the next message satisfies this format: !reply <msgID> <contents>
    def verifyMessage(msg):
        if (len(msg.content) > 12):
            return msg.channel == channel and msg.content[
                0:6] == '!reply' and msg.content[7:11] == str(
                    message.id
                )[14:19] and msg.content[6] == ' ' and msg.content[11] == ' '

        return False

    # This will be the message that will be used to be sent back to the member
    msg = await client.wait_for('message', check=verifyMessage)

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Reply #' + str(message.id)[14:19],
                          color=embedColours[4])
    embed.add_field(name='**Contents**', value=msg.content[12:], inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    # Send to member's DM
    await message.channel.send(embed=embed)
    # Send a verification to admin-inbox
    await channel.send('Reply has been sent.\n')
    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Sends a message to the #admin-inbox of their specified
#          role request/change.
async def roleRequest(message):
    channel = client.get_channel(admin_inbox)

    # Checks if the message has contents
    if (len(message.content) < 13):
        await message.channel.send(
            'There is no contents in your role request. Please try again.')
        return

    if (message.content[12] != ' '):
        await message.channel.send(
            'Make sure there is a space inbetween the command and your message. Please try again.'
        )
        return

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Role Request',
                          description='**User: **' + message.author.mention,
                          color=embedColours[0])
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name='**Contents**',
                    value=message.content.replace('!rolerequest ', ''),
                    inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    # Send to #admin-inbox
    await channel.send(embed=embed)
    # Send a verification to member
    await message.channel.send('Role request has been sent.\n')
    await message.channel.send(embed=embed)


# REQUIRES: A Member of type Discord.Member
# EFFECTS: Sends a welcoming message to the newly joined member.
#          Sends an embed to #server-log
#          Sends a role request message to #admin-inbox
@client.event
async def on_member_join(member):
    await send_embed_on_member_join(member)
    channel = client.get_channel(admin_inbox)

    await member.send(
        'Welcome ' + member.mention +
        ' to the **__RyEng__** discord server!\n\nPlease type in your year, dicipline, and whether or not you are a ryerson student below:'
    )

    # Checks that the reply is from the joined member and is in the DM Channel
    def check(m):
        return isinstance(m.channel,
                          discord.DMChannel) and (str(member) == str(m.author))

    msg = await client.wait_for('message', check=check)

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Role Request',
                          description='**User: **' + member.mention,
                          color=embedColours[0])
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='**Contents**', value=msg.content, inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    # Send to #admin-inbox
    await channel.send(embed=embed)
    # Send a verification to member
    await member.send('Role request has been sent.\n')
    await member.send(embed=embed)


# REQUIRES: A Memberof type Discord.Member
# EFFECTS: Logs when an user joins the server in the #server-log channel
async def send_embed_on_member_join(member):
    channel = client.get_channel(serverLog)

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='New Member Joined',
                          description='**User: **' + str(member.mention),
                          color=embedColours[0])
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs when a member leaves the server in the #server-log channel
@client.event
async def on_member_remove(member):
    channel = client.get_channel(serverLog)

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    ############################################################################
    embed = discord.Embed(title='Member Left',
                          description='**User: **' + str(member.mention),
                          color=embedColours[1])
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))
    ############################################################################

    await channel.send(embed=embed)


# EFFECTS: Prints out the name and Discord User ID of the bot
#          in the terminal once it has connected and initialized.
@client.event
async def on_ready():
    print('LOGGED ON: ' + str(client.user.name) + '\nID: ' +
          str(client.user.id))


client.run(TOKEN)
