import discord
import random
import datetime

# COPYRIGHT 2019 198938374822821888 & 365621509450104851
# Designed and developed for the RyEng discord server.

TOKEN = ''

# RyEng Server ID
serverID = 365554916451811341

# 365621509450104851 poofy#6421
# 295610195923697666 kam#2959
# 130400795668512768 Minibeat_UwU#2257
# 198938374822821888 smile#7677
# 276844714844618772 Ryhan#9128
admins = [
    198938374822821888, 365621509450104851, 295610195923697666,
    130400795668512768, 276844714844618772
]

# this is for the ryEng discord, IDs for all the RESOURCE channels
resourceChannels = [
    379053997807501312, 385609182675468298, 571366462195761152,
    571366485969338389, 571366540595691552
]

# #server-log channel on RyEng
serverLog = 484401067862392852

# 0x00FFC8 Bright Turquoise (On Member Join)
# 0xFF0055 Red (On Member Leave)
# 0x9900FF Electric Purple (Delete/Edit Message)
# 0x8AFF00 Chartreuse (Nickname Change)
# 0x008080 Teal (Resource Post)
embedColours = [0x00FFC8, 0xFF0055, 0x9900FF, 0x8AF00, 0x008080]

client = discord.Client()


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Reads a message and runs any specified commands
#          called.
@client.event
async def on_message(message):
    if (isinstance(message.channel, discord.DMChannel)
            and message.content.startswith('!sendid')):
        #   Sends the ID directly to me (smile#7677)
        channel = client.get_channel(627705526167404544)
        await channel.send(str(message.author) + ': ' + str(message.author.id))
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content == '!rolerequest'):
        await roleRequest(message)
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!sendmessage')):
        await sendMessage(message)
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!listadmins')):
        # Create an embed
        embed = discord.Embed(title='Admins', color=0x2F67D6)
        embed.add_field(name='Admin List',
                        value='```\n2339\n1214\n3977\n8123\n4206```',
                        inline=False)

        await message.channel.send(embed=embed)
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!commands')):
        # Create an embed
        embed = discord.Embed(title='Commands', color=0x2F67D6)
        embed.set_thumbnail(url=client.get_guild(serverID).icon_url)
        embed.add_field(
            name='Command Information',
            value=
            '\n**!commands** - lists the commands of this bot\n\n**!listadmins** - lists the anonymous 4 digit IDs of the admins\n\n**!sendmessage <ID>** - Target an admin to send a message to (e.g. !sendmessage 2339 then press enter); use !listadmin to get an ID\n\n**!rolerequest** - Request a role or modification in your roles\n\n**!post[X]y / !postOther** - Posts contents onto the resources channel anonymously for X = [1, 2, 3, 4]',
            inline=False)

        await message.channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post1y")):
        #sends it to test server general
        channel = client.get_channel(resourceChannels[0])
        await channel.send(message.content.replace('!post1y ', ''))

        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        embed = discord.Embed(title='Resource Posted', color=embedColours[4])
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name='1st Year Resource Information',
                        value='__**User:**__ ' + str(message.author.mention) +
                        '\n__**Contents:**__ ' + str(message.content[7:]),
                        inline=False)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post2y")):
        #sends it to test server general
        channel = client.get_channel(resourceChannels[1])
        await channel.send(message.content.replace('!post2y ', ''))

        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        embed = discord.Embed(title='Resource Posted', color=embedColours[4])
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name='2nd Year Resource Information',
                        value='__**User:**__ ' + str(message.author.mention) +
                        '\n__**Contents:**__ ' + str(message.content[7:]),
                        inline=False)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post3y")):
        #sends it to test server general
        channel = client.get_channel(resourceChannels[2])
        await channel.send(message.content.replace('!post3y ', ''))

        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        embed = discord.Embed(title='Resource Posted', color=embedColours[4])
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name='3rd Year Resource Information',
                        value='__**User:**__ ' + str(message.author.mention) +
                        '\n__**Contents:**__ ' + str(message.content[7:]),
                        inline=False)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!post4y")):
        #sends it to test server general
        channel = client.get_channel(resourceChannels[3])
        await channel.send(message.content.replace('!post4y ', ''))

        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        embed = discord.Embed(title='Resource Posted', color=embedColours[4])
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name='4th Year Resource Information',
                        value='__**User:**__ ' + str(message.author.mention) +
                        '\n__**Contents:**__ ' + str(message.content[7:]),
                        inline=False)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!postOther")):
        #sends it to test server to a test channel
        channel = client.get_channel(resourceChannels[4])
        # the .replace replaces the command part of the string
        await channel.send(message.content.replace('!postOther ', ''))

        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        embed = discord.Embed(title='Resource Posted', color=embedColours[4])
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name='Other Resource Information',
                        value='__**User:**__ ' + str(message.author.mention) +
                        '\n__**Contents:**__ ' + str(message.content[10:]),
                        inline=False)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)

    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith("!")):
        await message.channel.send(
            'ValueError Exception: Invalid command.\n\n!commands to list commands'
        )


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs the deleted message in the #server-log channel
@client.event
async def on_message_delete(message):
    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    embed = discord.Embed(title='Deleted Message', color=embedColours[2])
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name='Message Information',
                    value='__**User:**__ ' + str(message.author.mention) +
                    '\n__**Contents:**__ ' + str(message.content),
                    inline=False)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

    channel = client.get_channel(serverLog)
    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs the edited message in the #server-log channel
@client.event
async def on_message_edit(before, after):
    if (before.content == after.content):
        return

    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    embed = discord.Embed(title='Edited Message', color=embedColours[2])
    embed.set_thumbnail(url=before.author.avatar_url)
    embed.add_field(name='Message Information',
                    value='__**User:**__ ' + str(before.author.mention) +
                    '\n__**Before:**__ ' + before.content +
                    '\n__**After:**__ ' + after.content,
                    inline=True)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

    channel = client.get_channel(serverLog)
    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs a nickname change in the #server-log channel
@client.event
async def on_member_update(before, after):
    if (before.nick != after.nick):
        # Gets current date and time
        now = datetime.datetime.now()

        # Create an embed
        embed = discord.Embed(title='Nickname Change', color=embedColours[3])
        embed.set_thumbnail(url=before.avatar_url)
        embed.add_field(name='Change Information',
                        value='__**User:**__ ' + str(before.mention) +
                        '\n__**Before:**__ ' + str(before.nick) +
                        '\n__**After:**__ ' + str(after.nick),
                        inline=True)
        embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

        channel = client.get_channel(serverLog)
        await channel.send(embed=embed)


# REQUIRES: A Memberof type Discord.Member
# EFFECTS: Logs when an user joins the server in the #server-log channel
async def send_embed_on_member_join(member):
    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    embed = discord.Embed(title='New Member Joined', color=embedColours[0])
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='Member Information',
                    value='__**User:**__ ' + str(member.mention),
                    inline=True)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

    channel = client.get_channel(serverLog)
    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Logs when a member leaves the server in the #server-log channel
@client.event
async def on_member_remove(member):
    # Gets current date and time
    now = datetime.datetime.now()

    # Create an embed
    embed = discord.Embed(title='Member Left', color=embedColours[1])
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='Member Information',
                    value='__**User:**__ ' + str(member.mention),
                    inline=True)
    embed.set_footer(text=str(now.strftime("%Y-%m-%d %H:%M")))

    channel = client.get_channel(serverLog)
    await channel.send(embed=embed)


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Sends a message from a server member to a specified
#          admin or from an admin to a specified member.
async def sendMessage(message):
    server = client.get_guild(serverID)
    # Checks if an user is an admin
    if (await isAdmin(message.author.id)):
        member = await targetMember(message.content[13:])
        if (member):
            await message.channel.send('Enter your message:')

            # Checks next message is from the same user and in the DMs; saves the message to msg
            def verifyMessage(m):
                return isinstance(m.channel, discord.DMChannel) and (str(
                    m.author) == str(message.author))

            msg = await client.wait_for('message', check=verifyMessage)

            # Send to the target member of the server
            await member.send(await adminCode(message.author.id) + ': ' +
                              msg.content)

            # Tell user that their message was sent
            await message.channel.send('Message sent.')
        else:
            await message.channel.send(
                'ValueError Exception of **!sendmessage <ID>**: there is no target to send to or invalid format.\n\nMake sure there is no message after !sendmessage <ID>\n\nExample: !sendmessage 2339\n\n!list to list available admins to send to.'
            )
    # Not an admin...
    else:
        #   Get the user ID of an admin
        admin = await targetAdmin(message.content[13:])
        # If it has a value...
        if (admin):
            await message.channel.send('Enter your message:')

            # Checks next message is from the same user and in the DMs; saves the message to msg
            def verifyMessage(m):
                return isinstance(m.channel, discord.DMChannel) and (str(
                    m.author) == str(message.author))

            msg = await client.wait_for('message', check=verifyMessage)

            # Send to an admin...
            for member in server.members:
                if (member.id == admin):
                    await member.send(str(msg.author) + ": " + msg.content)
                    break

            # Tell user that their message was sent
            await message.channel.send('Message sent.')
            return
        # admin value is none (AKA inputted <ID> is invalid)
        else:
            await message.channel.send(
                'ValueError Exception of **!sendmessage <ID>**:\nNo target to send to or invalid format.\n!list to list available admins to send to.\n'
            )


# REQUIRES: A Discord User ID of type Integer
# RETURNS: True if the ID passed matches with an admin
#          Discord User ID from the admins[] array. Returns
#          None otherwise.
async def isAdmin(id):
    isAdmin = None

    for admin in admins:
        if (id == admin):
            isAdmin = True
            break
        else:
            isAdmin = False

    return isAdmin


# REQUIRES: A Discord User ID of type Iinteger
# RETURNS: A string containing the 4 digit admin code of the
#          specified admin.
async def adminCode(id):
    try:
        return {
            admins[0]: '2339',
            admins[1]: '1214',
            admins[2]: '3977',
            admins[3]: '8123',
            admins[4]: '4206'
        }[id]
    except KeyError:
        return None


# REQUIRES: A 4 digit admin code of type String
# RETURNS: An Discord User ID of type Integer of an admin if
#          the argument passed matches an admin code. Returns
#          None otherwise.
async def targetAdmin(id):
    try:
        return {
            '2339': admins[0],
            '1214': admins[1],
            '3977': admins[2],
            '8123': admins[3],
            '4206': admins[4]
        }[id]
    except KeyError:
        return None


# REQUIRES: Discord Username of type String (PeePeePooPoo#1234)
# RETURNS: A member of type Discord.Member. If the discord username
#          passed in the argument matches with a server member.
#          Returns None otherwise.
async def targetMember(username):
    server = client.get_guild(serverID)

    for member in server.members:
        if (username == str(member)):
            return member

    return None


# REQUIRES: A Message of type Discord.Message
# EFFECTS: Sends a message to a random admin of their specified
#          role request/change.
async def roleRequest(message):
    server = client.get_guild(serverID)

    await message.channel.send(
        'Please type in your request for a **__ROLE__** or **__ROLECHANGE__** below:'
    )

    # Checks that the reply is from the requesting member and is in the DM Channel
    def check(m):
        return isinstance(m.channel, discord.DMChannel) and (str(
            m.author) == str(message.author))

    msg = await client.wait_for('message', check=check)

    await message.channel.send(
        'Sending request: ' + '"' + msg.content +
        '" to an admin.\n\nIf there are any problems or mistakes in your message above, type in !rolerequest below again.'
    )

    target = admins[random.randrange(0, len(admins))]

    # Messages a random admin the role request of the member
    for member in server.members:
        if (member.id == target):
            print(member.id)
            await member.send('**__ROLE REQUEST/CHANGE__**:\n' +
                              str(msg.author) + ': ' + msg.content)
            # Tell their user their request/change was sent
            await message.channel.send('Role request/change sent.')
            break


# REQUIRES: A Member of type Discord.Member
# EFFECTS: Sends a welcoming message to the newly joined member.
#          Then sends a message to a random admin of their
#          specified role request.
@client.event
async def on_member_join(member):
    await send_embed_on_member_join(member)
    server = client.get_guild(serverID)

    await member.send(
        'Welcome ' + member.mention +
        ' to the **__RyEng__** discord server!\n\nPlease type in your year, dicipline, and whether or not you are a ryerson student below:'
    )

    # Checks that the reply is from the joined member and is in the DM Channel
    def check(m):
        return isinstance(m.channel,
                          discord.DMChannel) and (str(member) == str(m.author))

    msg = await client.wait_for('message', check=check)

    await member.send(
        'Sending request: ' + '"' + msg.content +
        '" to an admin.\n\nIf there are any problems or mistakes in your message above, type in !rolerequest below.\n\n To list commands type in !commands'
    )

    target = admins[random.randrange(0, len(admins))]

    # Messages a random admin the role request of the newly joined member
    for member in server.members:
        if (member.id == target):
            print(member.id)
            await member.send('**__ROLE REQUEST/CHANGE__**:\n' +
                              str(msg.author) + ': ' + msg.content)
            # Tell the user their request was sent
            await msg.channel.send('Role request sent.')
            break


# EFFECTS: Prints out the name and Discord User ID of the bot
#          in the terminal once it has connected and initialized.
@client.event
async def on_ready():
    print('LOGGED ON: ' + str(client.user.name) + '\nID: ' +
          str(client.user.id))


client.run(TOKEN)
