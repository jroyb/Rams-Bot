import discord
import random
import datetime


TOKEN = 'xxxxxxxxxxxxxx'

#   Test Server ID
serverID = 627700379286634536

admins = [
    198938374822821888, 365621509450104851, 295610195923697666,
    130400795668512768, 102642702679576576
]

# this is for the ryEng discord, ids for all the RESOURCE channels
firstYear = 379053997807501312
secondYear = 385609182675468298
thirdYear = 571366462195761152
fourthYear = 571366485969338389
otherRes = 571366540595691552

# test ids for test server 
generalTest = 627700379286634538
testOne = 639956593047371796

#log channel on test server

testLog = 640365215900237826

randColours = [0x00ff00, 0x7569dc, 0xc41a1a, 0xceb10f]

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
          and message.content.startswith('!rolerequest')):
        await roleRequest(message)
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!sendmessage')):
        await sendMessage(message)
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!listadmins')):
        await message.channel.send(
            '```Admin IDs:\n2339\n1214\n3977\n8123\n0264```')
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content.startswith('!commands')):
        await message.channel.send(
            '**__Commands:__**\n**!commands** - lists the commands of this bot\n\n**!listadmins** - lists the anonymous 4 digit IDs of the admins\n\n**!sendmessage <ID>** - Sends a message to a specified admin; use !listadmin to get an ID\n\n**!rolerequest** - Request a role or modification in your roles')  
    elif (isinstance(message.channel, discord.DMChannel) 
          and message.content.startswith('!post')): 
        await message.channel.send('If you want to post a link __**anonymously**__, please type in either "!1y", "!2y", "!3y", "!4y" or "!other" along with a __***link***__')      
    
    #elif message.content.startswith('!hello'):
        #embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        #embed.add_field(name="Field1", value="hi", inline=True)
        #embed.add_field(name="Field2", value="hi2", inline=False)
        #await message.channel.send(embed=embed)
    
    elif(isinstance(message.channel, discord.DMChannel) and message.content.startswith("!1y")):
        #sends it to test server general 
        channel = client.get_channel(firstYear)
        await channel.send(message.content.replace('!1y ' ,'')) 
    
    elif(isinstance(message.channel, discord.DMChannel) and message.content.startswith("!2y")):
        #sends it to test server general 
        channel = client.get_channel(secondYear)
        await channel.send(message.content.replace('!2y ' ,'')) 
    
    elif(isinstance(message.channel, discord.DMChannel) and message.content.startswith("!3y")):
        #sends it to test server general 
        channel = client.get_channel(thirdYear)
        await channel.send(message.content.replace('!3y ' ,'')) 
    
    elif(isinstance(message.channel, discord.DMChannel) and message.content.startswith("!4y")):
        #sends it to test server general 
        channel = client.get_channel(fourthYear)
        await channel.send(message.content.replace('!4y ' ,'')) 

    elif(isinstance(message.channel, discord.DMChannel) and message.content.startswith("!other")):
        #sends it to test server to a test channel
        channel = client.get_channel(otherRes)
        # the .replace replaces the command part of the string
        await channel.send(message.content.replace('!other ',''))
    
    elif (isinstance(message.channel, discord.DMChannel)
          and message.content[0] == '!'):
        await message.channel.send('ValueError Exception: Invalid command.')

@client.event
async def on_message_delete(message):
    #author.mention tags the person who deleted the message ha >:)

    # gets current date and time?
    now = datetime.datetime.now()
    embed = discord.Embed(title = 'Deleted Message', color = random.choice(randColours))
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name = 'Message Content', value = '__**Message**__ ' + str(message.content) + '\n__**User**__ ' + str(message.author.mention), inline = False)
    embed.set_footer(text = str(now.strftime("%Y-%m-%d %H:%M")))
    
    channel = client.get_channel(testLog)
    await channel.send(embed=embed)

@client.event
async def on_message_edit(before, after):
    if(before.content != after.content):
        now = datetime.datetime.now()

        embed = discord.Embed(title = 'Edited Message', color = random.choice(randColours))
        embed.set_thumbnail(url=before.author.avatar_url)
        embed.add_field(name='Message Content', value = '__**Before**__ ' + before.content + '\n__**After**__ ' + after.content + '\n__**User**__ ' + str(before.author.mention), inline = True)
        embed.set_footer(text = str(now.strftime("%Y-%m-%d %H:%M")))
        channel = client.get_channel(testLog)
        await channel.send(embed=embed)
    
@client.event    
async def on_member_update(before, after):
    channel = client.get_channel(testLog)
   
    if(before.nick != after.nick):
        await channel.send(str(before.nick) + ' has changed his nickname to ' + str(after.nick))

@client.event
async def on_guild_role_create(role):
     channel = client.get_channel(testLog)
     await channel.send('The role ' + role.name + ' has been created!'+ '\nAt time ' + str(role.created_at))
     
@client.event 
async def on_guild_role_delete(role):
    channel = client.get_channel(testLog)
    await channel.send('The role ' + role.name + ' has been deleted.')
    

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
                'ValueError Exception of **!sendmessage <ID>**:\nNo target to send to or invalid format.\n!list to list available admins to send to.\n'
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
                    await member.send(str(msg.author))
                    await member.send(msg.content)
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
            admins[4]: '0264',
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
            '0264': admins[4],
        }[id]
    except KeyError:
        return None


# REQUIRES: Discord Username of type String (PeePeePooPoo#1234)
# RETURNS: A member of type Discord.Member. If the discord username
#          passed in the argument matches with a server member.
#          Returns None otherwise.
async def targetMember(username):
    server = client.get_guild(627700379286634536)

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