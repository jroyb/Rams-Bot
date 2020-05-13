import discord
slurs = ['chink', 'nigger', 'nigga']


async def check(message):
    for slur in slurs:
        if slur in message.content.lower() and message.channel.name != 'role-requests':
            await message.delete()
            return
