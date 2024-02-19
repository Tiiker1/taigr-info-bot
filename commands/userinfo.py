import discord

async def execute(message, args, client, commands):
    # Check if the author has permission to mention users
    if not message.author.guild_permissions.mention_everyone:
        await message.reply('Sinulla ei ole tarvittavia oikeuksia komennon suorittamiseen.')
        return

    # Get the user to get information about
    if not args:
        await message.reply('Lisää käyttäjän tunniste komentoon.')
        return

    try:
        user_id = int(args[0])
        user = await message.guild.fetch_member(user_id)
    except (ValueError, discord.errors.NotFound):
        await message.reply('Virheellinen käyttäjän tunniste.')
        return

    if user:
        embed = discord.Embed(color=user.color)
        embed.add_field(name='käyttäjänimi', value=user.display_name, inline=False)
        embed.add_field(name='käyttäjän tunniste', value=user.id, inline=False)
        embed.add_field(name='Roolit', value=', '.join([role.name for role in user.roles[1:]]), inline=False)
        embed.add_field(name='Liittymispäivä', value=user.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
        
        # Check if the user has an avatar
        if user.avatar:
            avatar_url = user.avatar.url
        else:
            avatar_url = user.default_avatar.url

        embed.set_thumbnail(url=avatar_url)
        await message.channel.send(embed=embed)
    else:
        await message.reply('Käyttäjää ei löytynyt.')

execute.__command_name__ = 'userinfo'