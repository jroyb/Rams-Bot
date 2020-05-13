import discord
import asyncio
import ryeng_embed

mod_ch = None
rr_ch = None
rr_role_id = 703758222221377538
nb_role_id = 639226974044291102


async def function(client, guild, mod_ch, rr_ch, member):
    if client == None or guild == None or mod_ch == None or rr_ch == None or member == None:
        return

    def verify_reply(m):
        return m.channel == rr_ch and member.id == m.author.id

    try:
        rr_msg = await rr_ch.send(member.mention + ', please type in your year, dicipline, and whether or not you are a ryerson student below:')
        reply = await client.wait_for('message', timeout=300.0, check=verify_reply)

        await member.add_roles(guild.get_role(rr_role_id), reason=None, atomic=True)

        await mod_ch.send(embed=await ryeng_embed.role_request(reply))
        rr_embed = await rr_ch.send(embed=await ryeng_embed.role_request(reply))
    except asyncio.TimeoutError:
        try:
            await guild.kick(member, reason=None)
            await rr_msg.delete()
        except Exception as err:
            print('rolerequest.py Nested Try Except block in Try Except block 1')
            print(err)
            return
        return
    except Exception as err:
        print('rolerequest.py function(client, guild, member) Try Except block 1')
        print(err)
        return

    def check1(reaction, user):
        return reaction.message.channel == mod_ch and reaction.message.id == year_msg.id and user.id != client.user.id and (str(reaction.emoji) == '0️⃣' or str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣'
                                                                                                                            or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣' or str(reaction.emoji) == '👨‍🎓'
                                                                                                                            or str(reaction.emoji) == '🧙‍♂️')

    def check2(reaction, user):
        return reaction.message.channel == mod_ch and reaction.message.id == program_msg.id and user.id != client.user.id and (str(reaction.emoji) == '✈️' or str(reaction.emoji) == '⛑️' or str(reaction.emoji) == '🧪'
                                                                                                                               or str(reaction.emoji) == '🚧' or str(reaction.emoji) == '🖥️' or str(reaction.emoji) == '🔌'
                                                                                                                               or str(reaction.emoji) == '🏬' or str(reaction.emoji) == '⚙️' or str(reaction.emoji) == '🤷‍♂️'
                                                                                                                               or str(reaction.emoji) == '🖌️' or str(reaction.emoji) == '🩹' or str(reaction.emoji) == '📠'
                                                                                                                               or str(reaction.emoji) == '🗼' or str(reaction.emoji) == '📜' or str(reaction.emoji) == '🧬'
                                                                                                                               or str(reaction.emoji) == '💵')

    def check3(reaction, user):
        return reaction.message.channel == mod_ch and reaction.message.id == rams_msg.id and user.id != client.user.id and (str(reaction.emoji) == '🟦' or str(reaction.emoji) == '🟥')

    def check4(reaction, user):
        return reaction.message.channel == mod_ch and reaction.message.id == verify_msg.id and user.id != client.user.id

    try:
        year_msg = await mod_ch.send('Student Year/Alumni/Faculty?')
        await year_msg.add_reaction('0️⃣')
        await year_msg.add_reaction('1️⃣')
        await year_msg.add_reaction('2️⃣')
        await year_msg.add_reaction('3️⃣')
        await year_msg.add_reaction('4️⃣')
        await year_msg.add_reaction('👨‍🎓')
        await year_msg.add_reaction('🧙‍♂️')

        while True:
            reaction, user = await client.wait_for('reaction_add', check=check1)
            if(str(reaction.emoji) == '0️⃣'):
                await member.add_roles(guild.get_role(await ryeng_role_id('0️⃣')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '1️⃣'):
                await member.add_roles(guild.get_role(await ryeng_role_id('1️⃣')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '2️⃣'):
                await member.add_roles(guild.get_role(await ryeng_role_id('2️⃣')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '3️⃣'):
                await member.add_roles(guild.get_role(await ryeng_role_id('3️⃣')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '4️⃣'):
                await member.add_roles(guild.get_role(await ryeng_role_id('4️⃣')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '👨‍🎓'):
                await member.add_roles(guild.get_role(await ryeng_role_id('👨‍🎓')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🧙‍♂️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🧙‍♂️')), reason=None, atomic=True)
                break

        program_msg = await mod_ch.send('Program?')
        await program_msg.add_reaction('✈️')
        await program_msg.add_reaction('⛑️')
        await program_msg.add_reaction('🧪')
        await program_msg.add_reaction('🚧')
        await program_msg.add_reaction('🖥️')
        await program_msg.add_reaction('🔌')
        await program_msg.add_reaction('🏬')
        await program_msg.add_reaction('⚙️')
        await program_msg.add_reaction('🤷‍♂️')
        await program_msg.add_reaction('🖌️')
        await program_msg.add_reaction('🩹')
        await program_msg.add_reaction('📠')
        await program_msg.add_reaction('🗼')
        await program_msg.add_reaction('📜')
        await program_msg.add_reaction('🧬')
        await program_msg.add_reaction('💵')

        while True:
            reaction, user = await client.wait_for('reaction_add', check=check2)
            if(str(reaction.emoji) == '✈️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('✈️')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '⛑️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('⛑️')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🧪'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🧪')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🚧'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🚧')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🖥️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🖥️')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🔌'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🔌')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🏬'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🏬')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '⚙️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('⚙️')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🤷‍♂️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🤷‍♂️')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🖌️'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🖌️')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🩹'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🩹')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '📠'):
                await member.add_roles(guild.get_role(await ryeng_role_id('📠')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🗼'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🗼')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '📜'):
                await member.add_roles(guild.get_role(await ryeng_role_id('📜')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🧬'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🧬')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '💵'):
                await member.add_roles(guild.get_role(await ryeng_role_id('💵')), reason=None, atomic=True)
                break

        rams_msg = await mod_ch.send('Rams?')
        await rams_msg.add_reaction('🟦')
        await rams_msg.add_reaction('🟥')

        while True:
            reaction, user = await client.wait_for('reaction_add', check=check3)
            if(str(reaction.emoji) == '🟦'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🟦')), reason=None, atomic=True)
                break
            elif(str(reaction.emoji) == '🟥'):
                await member.add_roles(guild.get_role(await ryeng_role_id('🟥')), reason=None, atomic=True)
                break

        verify_msg = await mod_ch.send('Verify')
        await verify_msg.add_reaction('✅')

        while True:
            reaction, user = await client.wait_for('reaction_add', check=check4)
            if(str(reaction.emoji) == '✅'):
                await member.add_roles(guild.get_role(await ryeng_role_id('✅')), reason=None, atomic=True)
                break
    except Exception as err:
        print('rolerequest.py function(client, guild, member) Try Except block 2')
        print(err)
        return

    try:
        await member.remove_roles(guild.get_role(rr_role_id), reason=None, atomic=True)

        await mod_ch.send(embed=await ryeng_embed.role_request_successful(reply))
        await member.send(embed=await ryeng_embed.role_request_successful(reply))

        await rr_embed.delete()
        await rr_msg.delete()
        await reply.delete()
    except Exception as err:
        print('rolerequest.py function(client, guild, member) Try Except block 3')
        print(err)
        return


async def ryeng_role_id(role_id):
    switch = {
        '0️⃣': 397163590303350798,
        '1️⃣': 385611207782039554,
        '2️⃣': 385611110293700620,
        '3️⃣': 385611219198803968,
        '4️⃣': 385611227763572739,
        '👨‍🎓': 571316667393638410,
        '🧙‍♂️': 533364571096743936,
        '✈️': 365557635828940810,
        '⛑️': 365557468383805440,
        '🧪': 365557340222783488,
        '🚧': 365557682129862657,
        '🖥️': 365556700654338050,
        '🔌': 365557535203393541,
        '🏬': 365557408409583637,
        '⚙️': 365557859146137600,
        '🤷‍♂️': 366816870608666624,
        '🖌️': 675897342414815252,
        '🩹': 675897382797574145,
        '📠': 675897772322455597,
        '🗼': 675897389978091545,
        '📜': 675897712117415956,
        '🧬': 446007311878717442,
        '💵': 640924064679985152,
        '🟦': 411164852741210122,
        '🟥': 411161716211187714,
        '✅': 571349613638844417
    }
    return switch.get(role_id, None)


async def remove_all_roles(member):
    for role in member.roles:
        if role.name != '@everyone' and role.id != 639226974044291102 and role.name != 'Muted':
            await member.remove_roles(role, reason=None, atomic=True)
    return
