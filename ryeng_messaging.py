import discord
import ryeng_embed


async def user_mode(client, mod_ch, message):
    if client == None or mod_ch == None or message == None:
        return

    if len(message.content) <= 4 or message.content[3] != ' ':
        await message.channel.send('Invalid format.')
        return

    try:
        embed_1 = await ryeng_embed.user_message(message)
        await mod_ch.send(embed=embed_1)
        await message.channel.send(embed=embed_1)
        await message.delete()
    except Exception as err:
        print('messaging.py user_mode(client, message) Try Except block 1')
        print(err)
        return

    def check(m):
        if len(m.content) >= 13:
            return m.channel == mod_ch and m.content[0:6] == '!reply' and m.content[7:11] == str(message.id)[14:18] and m.content[6] == ' ' and m.content[11] == ' '

    try:
        reply = await client.wait_for('message', check=check)

        embed_2 = await ryeng_embed.admin_reply(str(message.id)[14:18], reply)
        await mod_ch.send(embed=embed_2)
        await message.channel.send(embed=embed_2)
        await reply.delete()

        return
    except Exception as err:
        print('messaging.py user_mode(client, message) Try Except block 2')
        print(err)
        return


async def admin_mode(client, mod_ch, message):
    try:
        member = message.guild.get_member(int(message.content[4:22]))
    except Exception as err:
        print('messaging.py admin_mode(client, message) Try Except block 1')
        print(err)
        return

    if client == None or mod_ch == None or message == None or member == None:
        return

    if len(message.content) <= 23 or message.content[22] != ' ' or message.content[3] != ' ':
        await mod_ch.send('Invalid format.')
        return

    try:
        embed_1 = await ryeng_mbed.admin_message(message)
        await mod_ch.send(embed=embed_1)
        await member.send(embed=embed_1)
        await message.delete()
    except Exception as err:
        print('messaging.py admin_mode(client, message) Try Except block 2')
        print(err)
        return

    def check(m):
        if len(m.content) >= 13:
            return m.author == member and m.content[0:6] == '!reply' and m.content[7:11] == str(message.id)[14:18] and m.content[6] == ' ' and m.content[11] == ' '
    try:
        reply = await client.wait_for('message', check=check)

        embed_2 = await ryeng_embed.user_reply(str(message.id)[14:18], reply)
        await mod_ch.send(embed=embed_2)
        await member.send(embed=embed_2)
        await reply.delete()

        return
    except Exception as err:
        print('messaging.py admin_mode(client, message) Try Except block 3')
        print(err)
        return
