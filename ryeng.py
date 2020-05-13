import discord


async def get_ryeng_server(client):
    return client.get_guild(365554916451811341)


async def get_moderators_channel(client):
    return client.get_channel(385625534970986496)


async def get_logs_channel(client):
    return client.get_channel(484401067862392852)

async def get_rolerequests_channel(client):
    return client.get_channel(703436751842050111)
