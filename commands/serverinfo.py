import discord

async def execute(message, args, client, commands):
    server = message.guild

    server_info = {
        'name': server.name,
        'id': server.id,
        'owner': str(server.owner) if server.owner else 'Ei saatavilla (ei oikeuksia)',
        'region': str(client.latency),
        'member_count': server.member_count,
        'creation_date': server.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'verification_level': str(server.verification_level),
        'roles': len(server.roles),
        'channels': {
            'text': len([channel for channel in server.channels if channel.type == discord.ChannelType.text]),
            'voice': len([channel for channel in server.channels if channel.type == discord.ChannelType.voice]),
        },
    }

    server_info_string = (
        f"**Palvelimen Tiedot:**\n"
        f"- Palvelimen nimi: {server_info['name']}\n"
        f"- Palvelimen ID: {server_info['id']}\n"
        f"- Palvelimen omistaa: {server_info['owner']}\n"
        f"- Palvelimen sijainti: {server_info['region']}\n"
        f"- Jäsenienmäärä: {server_info['member_count']}\n"
        f"- Palvelimen luomispäivä: {server_info['creation_date']}\n"
        f"- Vahvistustaso: {server_info['verification_level']}\n"
        f"- Roolit: {server_info['roles']}\n"
        f"- Tekstikanavat: {server_info['channels']['text']}\n"
        f"- Äänikanavat: {server_info['channels']['voice']}\n"
    )

    await message.channel.send(server_info_string)

# Assign the execute function to a 'name' attribute
execute.__command_name__ = 'serverinfo'
