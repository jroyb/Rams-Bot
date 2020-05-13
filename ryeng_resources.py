import discord
import ryeng_embed


async def send(guild, log_ch, message):
    rsrc_ch = None

    # If any of the channels cannot be referenced, return
    if(guild == None or log_ch == None or message == None):
        return

    # Checks if the message has contents...
    # No Attachment, Has Text
    if (message.attachments == []):
        if len(message.content) <= 7 or message.content[6] != ' ':
            await message.channel.send('Invalid format.')
            return

        try:
            rsrc_ch = guild.get_channel(await resource_channel_id(int(message.content[5])))
            if rsrc_ch == None:
                return

            await rsrc_ch.send(message.content[7:])
            embed_1 = await ryeng_embed.on_resource_post(message, rsrc_ch)
        except Exception as err:
            print('ryeng_resources.py send(guild, log_ch, message) Try Except block 1')
            print(err)
            return
    else:
        # Has Attachment, Has Text
        if len(message.content) >= 8:
            if (message.content[6] != ' '):
                await message.channel.send('Invalid format.')
                return

            try:
                rsrc_ch = guild.get_channel(await resource_channel_id(int(message.content[5])))
                if rsrc_ch == None:
                    return

                await rsrc_ch.send(message.content[7:])
                for attachment in message.attachments:
                    await rsrc_ch.send(attachment.url)

                embed_1 = await ryeng_embed.on_resource_post(message, rsrc_ch)
            except Exception as err:
                print(
                    'ryeng_resources.py send(guild, log_ch, message) Try Except block 2')
                print(err)
                return
        else:
            try:
                rsrc_ch = guild.get_channel(await resource_channel_id(int(message.content[5])))
                if rsrc_ch == None:
                    return

                for attachment in message.attachments:
                    await rsrc_ch.send(attachment.url)

                embed_1 = await ryeng_embed.on_resource_post(message, rsrc_ch)
            except Exception as err:
                print(
                    'ryeng_resources.py send(guild, log_ch, message) Try Except block 3')
                print(err)
                return

    try:
        await log_ch.send(embed=embed_1)
        await message.channel.send(embed=embed_1)
        return
    except Exception as err:
        print('ryeng_resources.py send(guild, log_ch, message) Try Except block 4')
        print(err)
        return


async def resource_channel_id(choice):
    switch = {
        0: 642403628530925578,
        1: 642403508125040653,
        2: 642403533429145620,
        3: 642403557890588673,
        4: 642403588970119208,
    }
    return switch.get(choice, None)
